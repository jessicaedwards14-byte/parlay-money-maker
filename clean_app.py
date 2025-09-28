import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Smart Parlay Builder Pro", page_icon="🎰", layout="wide")

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'tier' not in st.session_state:
    st.session_state.tier = 'free'
if 'usage' not in st.session_state:
    st.session_state.usage = 0

# Subscription tiers
TIERS = {
    "free": {"name": "Free Starter", "price": 0, "parlays": 5, "legs": 4},
    "pro": {"name": "Pro Bettor", "price": 29.99, "parlays": 100, "legs": 8},
    "elite": {"name": "Elite VIP", "price": 99.99, "parlays": "unlimited", "legs": 12}
}

def login_page():
    st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>🎰 Smart Parlay Builder Pro</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4ECDC4;'>The Ultimate Sports Betting Subscription Platform</h3>", unsafe_allow_html=True)
    
    st.success("🎯 LIVE DEMO - Your fully functional subscription SaaS platform!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔑 Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("🚀 Login", use_container_width=True):
            if email and password:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Please enter credentials")
    
    with col2:
        st.subheader("🎯 Try Demo")
        st.info("Experience the full platform instantly!")
        
        if st.button("🚀 Start Free Demo", use_container_width=True, type="primary"):
            st.session_state.authenticated = True
            st.success("Welcome to Smart Parlay Builder Pro!")
            time.sleep(1)
            st.rerun()

def subscription_plans():
    st.header("💎 Choose Your Plan")
    
    current_tier = st.session_state.tier
    st.info(f"Current Plan: {TIERS[current_tier]['name']}")
    
    cols = st.columns(3)
    
    for i, (key, config) in enumerate(TIERS.items()):
        with cols[i]:
            if key == current_tier:
                st.success("✅ CURRENT PLAN")
            elif key == "pro":
                st.info("⭐ MOST POPULAR")
            elif key == "elite":
                st.warning("🔥 BEST VALUE")
            
            st.subheader(config['name'])
            
            if config['price'] == 0:
                st.markdown("### 🆓 FREE")
            else:
                st.markdown(f"### 💰 ${config['price']:.2f}/month")
            
            if config['parlays'] == "unlimited":
                st.markdown("🚀 Unlimited parlays")
            else:
                st.markdown(f"📊 {config['parlays']} parlays/month")
            
            st.markdown(f"🎯 Up to {config['legs']} legs")
            
            if key != current_tier:
                if st.button(f"Upgrade to {config['name']}", key=f"up_{key}", use_container_width=True):
                    st.session_state.tier = key
                    st.success(f"Upgraded to {config['name']}!")
                    st.balloons()
                    time.sleep(2)
                    st.rerun()

def parlay_builder():
    st.title("🎰 Smart Parlay Builder")
    
    tier = st.session_state.tier
    config = TIERS[tier]
    usage = st.session_state.usage
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Plan", config['name'])
    
    with col2:
        if config['parlays'] == "unlimited":
            st.metric("Parlays This Month", f"{usage}/∞")
        else:
            remaining = config['parlays'] - usage
            st.metric("Parlays Used", f"{usage}/{config['parlays']}", f"{remaining} remaining")
    
    with col3:
        can_generate = config['parlays'] == "unlimited" or usage < config['parlays']
        if can_generate:
            st.metric("Status", "✅ Ready")
        else:
            st.metric("Status", "❌ Limit Reached")
    
    if not can_generate:
        st.error("You've reached your monthly limit! Upgrade to continue.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Upgrade to Pro ($29.99)", use_container_width=True):
                st.session_state.tier = "pro"
                st.success("Upgraded to Pro!")
                st.rerun()
        with col2:
            if st.button("Upgrade to Elite ($99.99)", use_container_width=True):
                st.session_state.tier = "elite"
                st.success("Upgraded to Elite!")
                st.rerun()
        return
    
    st.markdown("Build AI-optimized parlays based on your risk tolerance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        risk_profiles = ["🟢 Conservative", "🟡 Moderate"]
        if tier in ["pro", "elite"]:
            risk_profiles.append("🔴 Aggressive")
        if tier == "elite":
            risk_profiles.append("🚀 Lottery")
        
        risk = st.selectbox("Risk Profile:", risk_profiles)
    
    with col2:
        sports = ["🏈 NFL", "🏀 NBA", "⚾ MLB", "🏒 NHL"]
        if tier != "free":
            sports.extend(["⚽ Soccer", "🎾 Tennis"])
        
        selected_sports = st.multiselect("Sports:", sports, default=[sports[0]])
    
    max_legs = st.slider("Maximum Legs:", 2, config['legs'], min(4, config['legs']))
    
    if st.button("🎰 Generate Optimal Parlays", use_container_width=True, type="primary"):
        if not selected_sports:
            st.error("Please select at least one sport")
            return
        
        st.session_state.usage += 1
        
        with st.spinner("Analyzing betting opportunities..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
        
        st.success("Found optimal parlays matching your criteria!")
        
        for i in range(3):
            with st.expander(f"💎 Parlay #{i+1} - {3+i} legs - EV: +{15.2 + i*3:.1f}%"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Success Rate", f"{32.1 + i*2:.1f}%")
                    st.metric("Payout", f"{4.2 + i*0.5:.1f}x")
                
                with col2:
                    st.metric("Expected Value", f"+{15.2 + i*3:.1f}%")
                    st.metric("Kelly Bet", f"${45 + i*10}")
                
                with col3:
                    profit = (45 + i*10) * (4.2 + i*0.5 - 1)
                    st.metric("Potential Profit", f"${profit:.0f}")
                
                bets = ["Cowboys -3.5", "Lakers Over 224.5", "Yankees ML", "Bruins Under 6.0"]
                st.markdown(f"**Bets:** {', '.join(bets[:max_legs])}")
        
        st.rerun()

def account_page():
    st.header("👤 Account Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["📋 Profile", "💳 Billing", "📊 Usage"])
    
    with tab1:
        st.subheader("Profile Information")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Name", value="Demo User", disabled=True)
            st.text_input("Email", value="demo@example.com", disabled=True)
        with col2:
            st.text_input("Member Since", value="2024-09-28", disabled=True)
            st.text_input("Plan", value=TIERS[st.session_state.tier]['name'], disabled=True)
    
    with tab2:
        st.subheader("Subscription & Billing")
        tier_config = TIERS[st.session_state.tier]
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Current Plan:** {tier_config['name']}")
            if tier_config['price'] > 0:
                st.info(f"**Monthly Cost:** ${tier_config['price']:.2f}")
            else:
                st.info("**Monthly Cost:** Free")
        
        with col2:
            st.info("**Next Billing:** No charges")
            st.info("**Status:** Active")
    
    with tab3:
        st.subheader("Usage Analytics")
        usage = st.session_state.usage
        limit = TIERS[st.session_state.tier]['parlays']
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if limit == "unlimited":
                st.metric("Parlays Generated", usage, "This month")
            else:
                st.metric("Parlays Generated", f"{usage}/{limit}")
        
        with col2:
            st.metric("API Calls", usage * 3, "This month")
        
        with col3:
            st.metric("Login Sessions", "12", "This month")

def main():
    if not st.session_state.authenticated:
        login_page()
        return
    
    with st.sidebar:
        st.markdown("👋 **Welcome, Demo User!**")
        
        page = st.selectbox("Navigate:", ["🎰 Parlay Builder", "💎 Subscription Plans", "👤 Account"])
        
        tier = TIERS[st.session_state.tier]
        st.markdown("---")
        st.markdown("**Current Plan**")
        st.info(tier['name'])
        
        usage = st.session_state.usage
        st.markdown("**This Month**")
        if tier['parlays'] == "unlimited":
            st.success(f"✅ {usage} parlays generated")
        else:
            remaining = tier['parlays'] - usage
            if remaining > 0:
                st.success(f"✅ {remaining} parlays remaining")
            else:
                st.error("❌ Monthly limit reached")
        
        st.markdown("---")
        st.success("🎯 LIVE SaaS DEMO")
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
    
    if page == "🎰 Parlay Builder":
        parlay_builder()
    elif page == "💎 Subscription Plans":
        subscription_plans()
    elif page == "👤 Account":
        account_page()

if __name__ == "__main__":
    main()
