
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
🎯 Portfolio Objective - Choose Optimization Strategy
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
apply_main_styles()
render_header()

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}
if "optimization_objective" not in st.session_state:
    st.session_state.optimization_objective = "Maximize Sharpe Ratio"

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🎯 Optimization Objective</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Choose how to optimize your portfolio</p>
    </div>
    """, unsafe_allow_html=True)

# Check if assets are selected
if not st.session_state.selected_assets:
    st.error("⚠️ No assets selected! Please go back and select assets first.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# OBJECTIVE SELECTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🎯 SELECT OPTIMIZATION OBJECTIVE</h2>
        <p style='color: white;'>Choose how to optimize your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

# Radio button selection
objective = st.radio(
    "What would you like to optimize?",
    [
        "Maximize Sharpe Ratio",
        "Minimize Risk",
        "Maximize Return",
        "Equal Weight"
    ],
    index=0,
    key="optimization_choice"
)

st.session_state.optimization_objective = objective

# ═══════════════════════════════════════════════════════════════════════════════
# OBJECTIVE DESCRIPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 SELECTED STRATEGY</h2>
    </div>
    """, unsafe_allow_html=True)

# Display objective details
if objective == "Maximize Sharpe Ratio":
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📈 Maximize Sharpe Ratio</h3>
            <p style='color: white;'><strong>⭐ RECOMMENDED</strong></p>
            <p style='color: #90EE90;'>Balanced approach - Optimal risk-adjusted returns</p>
            <p style='color: white; font-size: 0.9rem;'>This strategy finds the portfolio that gives you the best return for each unit of risk taken. It's the most widely used objective in portfolio optimization.</p>
        </div>
        """, unsafe_allow_html=True)
    
elif objective == "Minimize Risk":
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🛡️ Minimize Risk (Global Minimum Variance)</h3>
            <p style='color: white;'><strong>Conservative</strong></p>
            <p style='color: #90EE90;'>Lowest volatility portfolio</p>
            <p style='color: white; font-size: 0.9rem;'>This strategy finds the portfolio with the lowest possible volatility (risk), regardless of returns. Best for risk-averse investors.</p>
        </div>
        """, unsafe_allow_html=True)
    
elif objective == "Maximize Return":
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🚀 Maximize Return</h3>
            <p style='color: white;'><strong>Aggressive</strong></p>
            <p style='color: #90EE90;'>Highest expected return</p>
            <p style='color: white; font-size: 0.9rem;'>This strategy allocates 100% to the highest-returning asset. Best for aggressive investors with high risk tolerance.</p>
        </div>
        """, unsafe_allow_html=True)
    
else:  # Equal Weight
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>⚖️ Equal Weight</h3>
            <p style='color: white;'><strong>Simple</strong></p>
            <p style='color: #90EE90;'>1/N portfolio</p>
            <p style='color: white; font-size: 0.9rem;'>Simple equal weighting (1/N). Keep current weights. Good as a benchmark or default strategy.</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# OBJECTIVES COMPARISON TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📋 OBJECTIVES COMPARISON</h2>
    </div>
    """, unsafe_allow_html=True)

comparison_html = """
<div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; overflow-x: auto;'>
    <table style='width: 100%; border-collapse: collapse; color: white;'>
        <thead>
            <tr style='background-color: #003366;'>
                <th style='padding: 0.75rem; border: 1px solid #FFD700; color: #FFD700;'>Objective</th>
                <th style='padding: 0.75rem; border: 1px solid #FFD700; color: #FFD700;'>Focus</th>
                <th style='padding: 0.75rem; border: 1px solid #FFD700; color: #FFD700;'>Best For</th>
                <th style='padding: 0.75rem; border: 1px solid #FFD700; color: #FFD700;'>Risk Level</th>
            </tr>
        </thead>
        <tbody>
            <tr style='background-color: #003366;'>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>📈 Maximize Sharpe</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Risk-Adjusted Return</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Most Investors ⭐</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Moderate</td>
            </tr>
            <tr style='background-color: #004d80;'>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>🛡️ Minimize Risk</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Lowest Volatility</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Conservative</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Low</td>
            </tr>
            <tr style='background-color: #003366;'>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>🚀 Maximize Return</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Highest Return</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Aggressive</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>High</td>
            </tr>
            <tr style='background-color: #004d80;'>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>⚖️ Equal Weight</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Simple Benchmark</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Baseline</td>
                <td style='padding: 0.75rem; border: 1px solid rgba(255,215,0,0.3);'>Current</td>
            </tr>
        </tbody>
    </table>
</div>
"""

st.markdown(comparison_html, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# NEXT STEPS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🚀 NEXT STEPS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("← Back to Analysis", key="objective_to_analysis", use_container_width=True):
        st.switch_page("pages/3_Analysis.py")

with col2:
    st.markdown("""
        <div style='text-align: center; padding: 0.75rem; background-color: #004d80; border-radius: 0.5rem;'>
            <p style='color: #FFD700; font-weight: bold; margin: 0;'>Step 4/6</p>
            <p style='color: #90EE90; font-size: 0.9rem; margin: 0.25rem 0 0 0;'>Objective</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    if st.button("Next: Optimize →", key="objective_to_optimize", use_container_width=True):
        st.switch_page("pages/5_Optimize.py")

render_footer()
