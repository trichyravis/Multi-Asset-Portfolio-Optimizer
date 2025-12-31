
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
Multi-Asset Portfolio Optimizer - Main Application
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
from config_enhanced import PAGE_CONFIG, ASSET_STATS
from styles_enhanced import apply_main_styles, render_header, render_footer

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)

# ═══════════════════════════════════════════════════════════════════════════════
# APPLY STYLES & RENDER HEADER
# ═══════════════════════════════════════════════════════════════════════════════

apply_main_styles()
render_header()

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "investment_period" not in st.session_state:
    st.session_state.investment_period = 5
if "asset_class" not in st.session_state:
    st.session_state.asset_class = "Stocks"
if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = []
if "asset_weights" not in st.session_state:
    st.session_state.asset_weights = {}

# Define asset classes and their assets
ASSET_CLASSES = {
    "Stocks": ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JPM", "BAC", "XOM", "PG", "KO"],
    "Bonds": ["BND", "AGG", "LQD", "TLT", "SHV"],
    "Commodities": ["GLD", "SLV", "USO", "DBC", "UUP"],
    "Cryptocurrencies": ["BTC", "ETH", "BNB", "ADA", "SOL"]
}

# Asset class descriptions
CLASS_DESCRIPTIONS = {
    "Stocks": "Equity securities - 📈 Higher growth potential, higher volatility",
    "Bonds": "Fixed income securities - 📊 Lower risk, stable returns",
    "Commodities": "Raw materials & precious metals - 🏆 Portfolio diversification",
    "Cryptocurrencies": "Digital assets - ⚡ High volatility, emerging asset class"
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🏔️ Portfolio Optimizer</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Advanced Multi-Asset Portfolio Optimization</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: MODEL ASSUMPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚡ STEP 1: SET YOUR ASSUMPTIONS</h2>
        <p style='color: white;'>Configure risk-free rate and investment period:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    risk_free = st.slider(
        "💰 Risk-Free Rate (%)",
        min_value=0.1,
        max_value=10.0,
        value=st.session_state.risk_free_rate,
        step=0.1,
        help="Default: 4.5% (US Treasury 10Y)"
    )
    st.session_state.risk_free_rate = risk_free

with col2:
    period = st.slider(
        "📅 Investment Period (Years)",
        min_value=1,
        max_value=30,
        value=st.session_state.investment_period,
        step=1,
        help="Default: 5 years"
    )
    st.session_state.investment_period = period

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: SELECT ASSET CLASS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 STEP 2: SELECT ASSET CLASS</h2>
        <p style='color: white;'>Choose the category for your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

asset_class = st.selectbox(
    "Which asset class?",
    list(ASSET_CLASSES.keys()),
    index=list(ASSET_CLASSES.keys()).index(st.session_state.asset_class)
)
st.session_state.asset_class = asset_class

# Show description and available assets
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <p style='color: white; margin: 0;'><strong>About {asset_class}</strong></p>
            <p style='color: #FFD700; margin: 0.5rem 0 0 0; font-size: 0.9rem;'>{CLASS_DESCRIPTIONS[asset_class]}</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    assets_str = ", ".join(ASSET_CLASSES[asset_class][:6])
    if len(ASSET_CLASSES[asset_class]) > 6:
        assets_str += f", +{len(ASSET_CLASSES[asset_class]) - 6} more"
    
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <p style='color: white; margin: 0;'><strong>Available Assets</strong></p>
            <p style='color: #90EE90; margin: 0.5rem 0 0 0; font-size: 0.9rem;'>{assets_str}</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CURRENT ASSUMPTIONS DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🔧 YOUR CURRENT SETTINGS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Risk-Free Rate", f"{st.session_state.risk_free_rate:.2f}%")

with col2:
    st.metric("Investment Period", f"{st.session_state.investment_period} years")

with col3:
    st.metric("Asset Class", st.session_state.asset_class)

# ═══════════════════════════════════════════════════════════════════════════════
# WORKFLOW GUIDE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🚀 WORKFLOW</h2>
        <p style='color: white;'>Follow these steps to optimize your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Step 1: Set Assumptions** ✅ (You are here!)
    - Risk-Free Rate
    - Investment Period
    
    **Step 3: Analyze**
    - Go to sidebar → 📊 **Analysis**
    - View current portfolio performance
    """)

with col2:
    st.markdown("""
    **Step 2: Set Weights**
    - Go to sidebar → ⚖️ **Weights**
    - Select 2-6 assets from chosen class
    - Set weights (100% total)
    
    **Step 4-5: Optimize & Results**
    - Go to sidebar → 🎯 **Objective** → 🚀 **Optimize**
    - Go to 📊 **Results** to view optimized portfolio
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# INFO BOXES
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("")

st.info("""
💡 **Next Step:** Go to **⚖️ Weights** in the sidebar to select specific assets and set their weights.
""")

st.success("""
✅ **Your settings are ready!** Your risk-free rate and investment period will be used in all calculations.
""")

render_footer()
