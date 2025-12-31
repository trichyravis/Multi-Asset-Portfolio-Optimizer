
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
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🏔️ Portfolio Optimizer</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Advanced Multi-Asset Portfolio Optimization</p>
    </div>
    """, unsafe_allow_html=True)

# Quick Model Assumptions Section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>⚡ QUICK MODEL ASSUMPTIONS</h3>
        <p style='color: white;'>Set key parameters or go to Settings page for detailed configuration:</p>
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
        help="Currently ~4.5% (US Treasury 10Y). Adjust based on current market rates."
    )
    st.session_state.risk_free_rate = risk_free

with col2:
    period = st.slider(
        "📅 Investment Period (Years)",
        min_value=1,
        max_value=30,
        value=st.session_state.investment_period,
        step=1,
        help="Your investment horizon. Longer periods allow higher risk tolerance."
    )
    st.session_state.investment_period = period

# Settings link
st.markdown("""
    <div style='background-color: #1a5f7a; padding: 1rem; border-radius: 0.5rem; margin-bottom: 2rem; border-left: 5px solid #FFD700;'>
        <p style='color: white; margin: 0;'>
            📖 <strong>View detailed assumptions:</strong> Go to <strong>⚙️ Settings</strong> page to see asset details and calculation methodology.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Welcome Section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>👋 Welcome to The Mountain Path</h3>
        <p style='color: white;'>A comprehensive portfolio optimization platform for advanced financial analysis.</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h4 style='color: #FFD700; margin-top: 0;'>📊 Multi-Asset</h4>
            <p style='color: white; font-size: 0.9rem;'>
                Select from 20+ global assets including stocks, bonds, commodities, and cryptocurrencies.
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h4 style='color: #FFD700; margin-top: 0;'>⚙️ Customizable</h4>
            <p style='color: white; font-size: 0.9rem;'>
                Adjust risk-free rates, investment periods, and optimization objectives to match your needs.
            </p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h4 style='color: #FFD700; margin-top: 0;'>📈 Advanced Analytics</h4>
            <p style='color: white; font-size: 0.9rem;'>
                Modern Portfolio Theory, Sharpe Ratio optimization, and efficient frontier analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)

# Getting Started Section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>🚀 Getting Started</h3>
        <p style='color: white;'>Follow these steps to optimize your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

steps_html = """
<div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem;'>
    <div style='display: flex; align-items: flex-start; margin-bottom: 1.5rem;'>
        <div style='background-color: #FFD700; color: #003366; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem; flex-shrink: 0;'>1</div>
        <div>
            <h4 style='color: #FFD700; margin: 0 0 0.5rem 0;'>Select Assets</h4>
            <p style='color: white; margin: 0; font-size: 0.95rem;'>Choose 2-6 assets from stocks, bonds, commodities, or cryptocurrencies. Use the sidebar navigation to access asset selection.</p>
        </div>
    </div>
    
    <div style='display: flex; align-items: flex-start; margin-bottom: 1.5rem;'>
        <div style='background-color: #FFD700; color: #003366; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem; flex-shrink: 0;'>2</div>
        <div>
            <h4 style='color: #FFD700; margin: 0 0 0.5rem 0;'>Set Initial Weights</h4>
            <p style='color: white; margin: 0; font-size: 0.95rem;'>Define your current portfolio allocation. These weights will be optimized based on your selected objective.</p>
        </div>
    </div>
    
    <div style='display: flex; align-items: flex-start; margin-bottom: 1.5rem;'>
        <div style='background-color: #FFD700; color: #003366; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem; flex-shrink: 0;'>3</div>
        <div>
            <h4 style='color: #FFD700; margin: 0 0 0.5rem 0;'>Choose Objective</h4>
            <p style='color: white; margin: 0; font-size: 0.95rem;'>Select your optimization goal: Maximize Sharpe Ratio, Maximize Return, or Minimize Volatility.</p>
        </div>
    </div>
    
    <div style='display: flex; align-items: flex-start;'>
        <div style='background-color: #FFD700; color: #003366; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem; flex-shrink: 0;'>4</div>
        <div>
            <h4 style='color: #FFD700; margin: 0 0 0.5rem 0;'>View Results</h4>
            <p style='color: white; margin: 0; font-size: 0.95rem;'>See optimized weights, efficient frontier visualization, and detailed portfolio metrics.</p>
        </div>
    </div>
</div>
"""

st.markdown(steps_html, unsafe_allow_html=True)

# Key Features
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>✨ Key Features</h3>
    </div>
    """, unsafe_allow_html=True)

features_html = """
<div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;'>
        <div>
            <p style='color: #FFD700; font-weight: bold; margin-bottom: 0.5rem;'>📊 Modern Portfolio Theory</p>
            <p style='color: white; font-size: 0.9rem; margin: 0;'>Based on Markowitz framework for optimal diversification.</p>
        </div>
        <div>
            <p style='color: #FFD700; font-weight: bold; margin-bottom: 0.5rem;'>📈 Sharpe Ratio Optimization</p>
            <p style='color: white; font-size: 0.9rem; margin: 0;'>Maximize risk-adjusted returns using user-defined risk-free rate.</p>
        </div>
        <div>
            <p style='color: #FFD700; font-weight: bold; margin-bottom: 0.5rem;'>🎨 Interactive Visualizations</p>
            <p style='color: white; font-size: 0.9rem; margin: 0;'>Efficient frontier 2D plot showing all possible portfolios.</p>
        </div>
        <div>
            <p style='color: #FFD700; font-weight: bold; margin-bottom: 0.5rem;'>⚙️ Customizable Assumptions</p>
            <p style='color: white; font-size: 0.9rem; margin: 0;'>Adjust risk-free rate and investment period on main page.</p>
        </div>
        <div>
            <p style='color: #FFD700; font-weight: bold; margin-bottom: 0.5rem;'>📋 Detailed Reports</p>
            <p style='color: white; font-size: 0.9rem; margin: 0;'>Weight breakdowns, metrics comparison, and recommendations.</p>
        </div>
        <div>
            <p style='color: #FFD700; font-weight: bold; margin-bottom: 0.5rem;'>📚 Educational Focus</p>
            <p style='color: white; font-size: 0.9rem; margin: 0;'>Perfect for MBA, CFA, and FRM students and professionals.</p>
        </div>
    </div>
</div>
"""

st.markdown(features_html, unsafe_allow_html=True)

# Current Assumptions Display
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>🔧 YOUR CURRENT ASSUMPTIONS</h3>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <p style='color: #FFD700; margin: 0;'>Risk-Free Rate</p>
            <p style='color: white; font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0 0 0;'>{st.session_state.risk_free_rate:.2f}%</p>
            <p style='color: #90EE90; margin: 0.5rem 0 0 0; font-size: 0.85rem;'>Used in Sharpe Ratio calculation</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <p style='color: #FFD700; margin: 0;'>Investment Period</p>
            <p style='color: white; font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0 0 0;'>{st.session_state.investment_period} Year(s)</p>
            <p style='color: #90EE90; margin: 0.5rem 0 0 0; font-size: 0.85rem;'>Your time horizon for investing</p>
        </div>
        """, unsafe_allow_html=True)

# Navigation section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>📍 Navigation</h3>
        <p style='color: white;'>Use the sidebar to navigate through the application:</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
        <p style='color: white; margin: 0.5rem 0;'><strong style='color: #FFD700;'>⚙️ Settings:</strong> Detailed assumptions and asset information</p>
        <p style='color: white; margin: 0.5rem 0;'><strong style='color: #FFD700;'>📊 Analysis:</strong> Asset overview and historical data</p>
        <p style='color: white; margin: 0.5rem 0;'><strong style='color: #FFD700;'>⚖️ Weights:</strong> Set initial portfolio allocation</p>
        <p style='color: white; margin: 0.5rem 0;'><strong style='color: #FFD700;'>🎯 Objective:</strong> Choose optimization objective</p>
        <p style='color: white; margin: 0.5rem 0;'><strong style='color: #FFD700;'>🚀 Optimize:</strong> Run portfolio optimization</p>
        <p style='color: white; margin: 0.5rem 0;'><strong style='color: #FFD700;'>📊 Results:</strong> View optimized portfolio and metrics</p>
    </div>
    """, unsafe_allow_html=True)

render_footer()
