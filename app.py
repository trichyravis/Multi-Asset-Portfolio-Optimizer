
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
from config_enhanced import PAGE_CONFIG
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

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT - CLEAN & SIMPLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🏔️ Portfolio Optimizer</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Advanced Multi-Asset Portfolio Optimization</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# QUICK MODEL ASSUMPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>⚡ QUICK MODEL ASSUMPTIONS</h3>
        <p style='color: white;'>Set key parameters or go to Settings for detailed configuration:</p>
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
        help="Currently ~4.5% (US Treasury 10Y)"
    )
    st.session_state.risk_free_rate = risk_free

with col2:
    period = st.slider(
        "📅 Investment Period (Years)",
        min_value=1,
        max_value=30,
        value=st.session_state.investment_period,
        step=1,
        help="Your investment horizon"
    )
    st.session_state.investment_period = period

st.info("📖 View detailed assumptions: Go to **⚙️ Settings** page for asset details and calculation methodology.")

# ═══════════════════════════════════════════════════════════════════════════════
# WELCOME & OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h3 style='color: #FFD700; margin: 0;'>👋 Welcome to The Mountain Path</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("""
A comprehensive portfolio optimization platform using Modern Portfolio Theory and advanced financial analytics.
Select assets, set your allocation, and optimize your portfolio with customizable assumptions.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# WORKFLOW GUIDE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h3 style='color: #FFD700; margin: 0;'>🚀 Workflow</h3>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Step 1: Select Assets**
    - Go to sidebar → **📊 Analysis**
    - Choose 2-6 assets from 20+ options
    """)
    st.markdown("""
    **Step 3: Choose Objective**
    - Go to sidebar → **🎯 Objective**
    - Maximize Sharpe Ratio / Return or Minimize Volatility
    """)

with col2:
    st.markdown("""
    **Step 2: Set Initial Weights**
    - Go to sidebar → **⚖️ Weights**
    - Define current portfolio allocation
    """)
    st.markdown("""
    **Step 4: View Results**
    - Go to sidebar → **🚀 Optimize** then **📊 Results**
    - See optimized weights and metrics
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# CURRENT ASSUMPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h3 style='color: #FFD700; margin: 0;'>🔧 Your Current Assumptions</h3>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Risk-Free Rate", f"{st.session_state.risk_free_rate:.2f}%")

with col2:
    st.metric("Investment Period", f"{st.session_state.investment_period} years")

with col3:
    st.metric("Status", "Ready →")

# ═══════════════════════════════════════════════════════════════════════════════
# KEY FEATURES
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h3 style='color: #FFD700; margin: 0;'>✨ Key Features</h3>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write("""
    **📊 Multi-Asset**
    
    Select from 20+ global assets including stocks, bonds, commodities, and cryptocurrencies
    """)

with col2:
    st.write("""
    **⚙️ Customizable**
    
    Adjust risk-free rates, investment periods, and optimization objectives
    """)

with col3:
    st.write("""
    **📈 Advanced Analytics**
    
    Modern Portfolio Theory, Sharpe Ratio optimization, efficient frontier
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# NAVIGATION GUIDE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h3 style='color: #FFD700; margin: 0;'>📍 Sidebar Navigation</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("""
- **⚙️ Settings**: Detailed assumptions and asset information
- **📊 Analysis**: Asset overview and selection
- **⚖️ Weights**: Set initial portfolio allocation  
- **🎯 Objective**: Choose optimization objective
- **🚀 Optimize**: Run portfolio optimization
- **📊 Results**: View optimized portfolio and metrics
""")

st.success("✅ Ready to optimize! Use the sidebar to get started.")

render_footer()
