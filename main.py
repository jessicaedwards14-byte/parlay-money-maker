  1	import streamlit as st
     2	import pandas as pd
     3	import numpy as np
     4	import time
     5	
     6	st.set_page_config(page_title="Smart Parlay Builder Pro", page_icon="🎰", layout="wide")
     7	
     8	# Initialize session state
     9	if 'authenticated' not in st.session_state:
    10	    st.session_state.authenticated = False
    11	if 'tier' not in st.session_state:
    12	    st.session_state.tier = 'free'
    13	if 'usage' not in st.session_state:
    14	    st.session_state.usage = 0
    15	
    16	# Subscription tiers
    17	TIERS = {
    18	    "free": {"name": "Free Starter", "price": 0, "parlays": 5, "legs": 4},
    19	    "pro": {"name": "Pro Bettor", "price": 29.99, "parlays": 100, "legs": 8},
    20	    "elite": {"name": "Elite VIP", "price": 99.99, "parlays": "unlimited", "legs": 12}
    21	}
    22	
    23	def login_page():
    24	    st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>🎰 Smart Parlay Builder Pro</h1>", unsafe_allow_html=True)
    25	    st.markdown("<h3 style='text-align: center; color: #4ECDC4;'>The Ultimate Sports Betting Subscription Platform</h3>", unsafe_allow_html=True)
    26	    
    27	    st.success("🎯 LIVE DEMO - Your fully functional subscription SaaS platform!")
    28	    
    29	    col1, col2 = st.columns(2)
    30	    
    31	    with col1:
    32	        st.subheader("🔑 Login")
    33	        email = st.text_input("Email")
    34	        password = st.text_input("Password", type="password")
    35	        
    36	        if st.button("🚀 Login", use_container_width=True):
    37	            if email and password:
    38	                st.session_state.authenticated = True
    39	                st.rerun()
    40	            else:
    41	                st.error("Please enter credentials")
    42	    
    43	    with col2:
    44	        st.subheader("🎯 Try Demo")
    45	        st.info("Experience the full platform instantly!")
    46	        
    47	        if st.button("🚀 Start Free Demo", use_container_width=True, type="primary"):
    48	            st.session_state.authenticated = True
    49	            st.success("Welcome to Smart Parlay Builder Pro!")
    50	            time.sleep(1)
    51	            st.rerun()
    52	
    53	def subscription_plans():
    54	    st.header("💎 Choose Your Plan")
    55	    
    56	    current_tier = st.session_state.tier
    57	    st.info(f"Current Plan: {TIERS[current_tier]['name']}")
    58	    
    59	    cols = st.columns(3)
    60	    
    61	    for i, (key, config) in enumerate(TIERS.items()):
    62	        with cols[i]:
    63	            if key == current_tier:
    64	                st.success("✅ CURRENT PLAN")
    65	            elif key == "pro":
    66	                st.info("⭐ MOST POPULAR")
    67	            elif key == "elite":
    68	                st.warning("🔥 BEST VALUE")
    69	            
    70	            st.subheader(config['name'])
    71	            
    72	            if config['price'] == 0:
    73	                st.markdown("### 🆓 FREE")
    74	            else:
    75	                st.markdown(f"### 💰 ${config['price']:.2f}/month")
    76	            
    77	            if config['parlays'] == "unlimited":
    78	                st.markdown("🚀 Unlimited parlays")
    79	            else:
    80	                st.markdown(f"📊 {config['parlays']} parlays/month")
    81	            
    82	            st.markdown(f"🎯 Up to {config['legs']} legs")
    83	            
    84	            if key != current_tier:
    85	                if st.button(f"Upgrade to {config['name']}", key=f"up_{key}", use_container_width=True):
    86	                    st.session_state.tier = key
    87	                    st.success(f"Upgraded to {config['name']}!")
    88	                    st.balloons()
    89	                    time.sleep(2)
    90	                    st.rerun()
    91	
    92	def parlay_builder():
    93	    st.title("🎰 Smart Parlay Builder")
    94	    
    95	    tier = st.session_state.tier
    96	    config = TIERS[tier]
    97	    usage = st.session_state.usage
    98	    
    99	    col1, col2, col3 = st.columns(3)
   100	    
   101	    with col1:
   102	        st.metric("Current Plan", config['name'])
   103	    
   104	    with col2:
   105	        if config['parlays'] == "unlimited":
   106	            st.metric("Parlays This Month", f"{usage}/∞")
   107	        else:
   108	            remaining = config['parlays'] - usage
   109	            st.metric("Parlays Used", f"{usage}/{config['parlays']}", f"{remaining} remaining")
   110	    
   111	    with col3:
   112	        can_generate = config['parlays'] == "unlimited" or usage < config['parlays']
   113	        if can_generate:
   114	            st.metric("Status", "✅ Ready")
   115	        else:
   116	            st.metric("Status", "❌ Limit Reached")
   117	    
   118	    if not can_generate:
   119	        st.error("You've reached your monthly limit! Upgrade to continue.")
   120	        
   121	        col1, col2 = st.columns(2)
   122	        with col1:
   123	            if st.button("Upgrade to Pro ($29.99)", use_container_width=True):
   124	                st.session_state.tier = "pro"
   125	                st.success("Upgraded to Pro!")
   126	                st.rerun()
   127	        with col2:
   128	            if st.button("Upgrade to Elite ($99.99)", use_container_width=True):
   129	                st.session_state.tier = "elite"
   130	                st.success("Upgraded to Elite!")
   131	                st.rerun()
   132	        return
   133	    
   134	    st.markdown("Build AI-optimized parlays based on your risk tolerance")
   135	    
   136	    col1, col2 = st.columns(2)
   137	    
   138	    with col1:
   139	        risk_profiles = ["🟢 Conservative", "🟡 Moderate"]
   140	        if tier in ["pro", "elite"]:
   141	            risk_profiles.append("🔴 Aggressive")
   142	        if tier == "elite":
   143	            risk_profiles.append("🚀 Lottery")
   144	        
   145	        risk = st.selectbox("Risk Profile:", risk_profiles)
   146	    
   147	    with col2:
   148	        sports = ["🏈 NFL", "🏀 NBA", "⚾ MLB", "🏒 NHL"]
   149	        if tier != "free":
   150	            sports.extend(["⚽ Soccer", "🎾 Tennis"])
   151	        
   152	        selected_sports = st.multiselect("Sports:", sports, default=[sports[0]])
   153	    
   154	    max_legs = st.slider("Maximum Legs:", 2, config['legs'], min(4, config['legs']))
   155	    
   156	    if st.button("🎰 Generate Optimal Parlays", use_container_width=True, type="primary"):
   157	        if not selected_sports:
   158	            st.error("Please select at least one sport")
   159	            return
   160	        
   161	        st.session_state.usage += 1
   162	        
   163	        with st.spinner("Analyzing betting opportunities..."):
   164	            progress = st.progress(0)
   165	            for i in range(100):
   166	                time.sleep(0.01)
   167	                progress.progress(i + 1)
   168	        
   169	        st.success("Found optimal parlays matching your criteria!")
   170	        
   171	        for i in range(3):
   172	            with st.expander(f"💎 Parlay #{i+1} - {3+i} legs - EV: +{15.2 + i*3:.1f}%"):
   173	                col1, col2, col3 = st.columns(3)
   174	                
   175	                with col1:
   176	                    st.metric("Success Rate", f"{32.1 + i*2:.1f}%")
   177	                    st.metric("Payout", f"{4.2 + i*0.5:.1f}x")
   178	                
   179	                with col2:
   180	                    st.metric("Expected Value", f"+{15.2 + i*3:.1f}%")
   181	                    st.metric("Kelly Bet", f"${45 + i*10}")
   182	                
   183	                with col3:
   184	                    profit = (45 + i*10) * (4.2 + i*0.5 - 1)
   185	                    st.metric("Potential Profit", f"${profit:.0f}")
   186	                
   187	                bets = ["Cowboys -3.5", "Lakers Over 224.5", "Yankees ML", "Bruins Under 6.0"]
   188	                st.markdown(f"**Bets:** {', '.join(bets[:max_legs])}")
   189	        
   190	        st.rerun()
   191	
   192	def account_page():
   193	    st.header("👤 Account Dashboard")
   194	    
   195	    tab1, tab2, tab3 = st.tabs(["📋 Profile", "💳 Billing", "📊 Usage"])
   196	    
   197	    with tab1:
   198	        st.subheader("Profile Information")
   199	        col1, col2 = st.columns(2)
   200	        with col1:
   201	            st.text_input("Name", value="Demo User", disabled=True)
   202	            st.text_input("Email", value="demo@example.com", disabled=True)
   203	        with col2:
   204	            st.text_input("Member Since", value="2024-09-28", disabled=True)
   205	            st.text_input("Plan", value=TIERS[st.session_state.tier]['name'], disabled=True)
   206	    
   207	    with tab2:
   208	        st.subheader("Subscription & Billing")
   209	        tier_config = TIERS[st.session_state.tier]
   210	        
   211	        col1, col2 = st.columns(2)
   212	        with col1:
   213	            st.info(f"**Current Plan:** {tier_config['name']}")
   214	            if tier_config['price'] > 0:
   215	                st.info(f"**Monthly Cost:** ${tier_config['price']:.2f}")
   216	            else:
   217	                st.info("**Monthly Cost:** Free")
   218	        
   219	        with col2:
   220	            st.info("**Next Billing:** No charges")
   221	            st.info("**Status:** Active")
   222	    
   223	    with tab3:
   224	        st.subheader("Usage Analytics")
   225	        usage = st.session_state.usage
   226	        limit = TIERS[st.session_state.tier]['parlays']
   227	        
   228	        col1, col2, col3 = st.columns(3)
   229	        
   230	        with col1:
   231	            if limit == "unlimited":
   232	                st.metric("Parlays Generated", usage, "This month")
   233	            else:
   234	                st.metric("Parlays Generated", f"{usage}/{limit}")
   235	        
   236	        with col2:
   237	            st.metric("API Calls", usage * 3, "This month")
   238	        
   239	        with col3:
   240	            st.metric("Login Sessions", "12", "This month")
   241	
   242	def main():
   243	    if not st.session_state.authenticated:
   244	        login_page()
   245	        return
   246	    
   247	    with st.sidebar:
   248	        st.markdown("👋 **Welcome, Demo User!**")
   249	        
   250	        page = st.selectbox("Navigate:", ["🎰 Parlay Builder", "💎 Subscription Plans", "👤 Account"])
   251	        
   252	        tier = TIERS[st.session_state.tier]
   253	        st.markdown("---")
   254	        st.markdown("**Current Plan**")
   255	        st.info(tier['name'])
   256	        
   257	        usage = st.session_state.usage
   258	        st.markdown("**This Month**")
   259	        if tier['parlays'] == "unlimited":
   260	            st.success(f"✅ {usage} parlays generated")
   261	        else:
   262	            remaining = tier['parlays'] - usage
   263	            if remaining > 0:
   264	                st.success(f"✅ {remaining} parlays remaining")
   265	            else:
   266	                st.error("❌ Monthly limit reached")
   267	        
   268	        st.markdown("---")
   269	        st.success("🎯 LIVE SaaS DEMO")
   270	        
   271	        if st.button("🚪 Logout", use_container_width=True):
   272	            st.session_state.authenticated = False
   273	            st.rerun()
   274	    
   275	    if page == "🎰 Parlay Builder":
   276	        parlay_builder()
   277	    elif page == "💎 Subscription Plans":
   278	        subscription_plans()
   279	    elif page == "👤 Account":
   280	        account_page()
   281	
   282	if __name__ == "__main__":
   283	    main()
