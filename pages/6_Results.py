
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
📊 Optimization Results - Final Portfolio Allocation
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
import pandas as pd
import numpy as np
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
if "optimized_weights" not in st.session_state:
    st.session_state.optimized_weights = {}
if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "optimization_objective" not in st.session_state:
    st.session_state.optimization_objective = "Maximize Sharpe Ratio"

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET DATA
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_DATA = {
    "AAPL": {"return": 28.5, "volatility": 32.1}, "MSFT": {"return": 26.3, "volatility": 28.9},
    "GOOGL": {"return": 24.7, "volatility": 30.2}, "AMZN": {"return": 22.1, "volatility": 34.5},
    "NVDA": {"return": 35.2, "volatility": 45.8}, "JPM": {"return": 15.3, "volatility": 25.6},
    "BAC": {"return": 12.5, "volatility": 28.3}, "XOM": {"return": 8.9, "volatility": 22.4},
    "PG": {"return": 9.7, "volatility": 16.8}, "KO": {"return": 7.3, "volatility": 18.2},
    "BND": {"return": 4.2, "volatility": 6.3}, "AGG": {"return": 4.5, "volatility": 6.8},
    "LQD": {"return": 5.1, "volatility": 7.4}, "TLT": {"return": 3.8, "volatility": 8.9},
    "SHV": {"return": 3.2, "volatility": 2.1}, "GLD": {"return": 6.5, "volatility": 14.2},
    "SLV": {"return": 5.8, "volatility": 18.6}, "USO": {"return": 3.2, "volatility": 22.1},
    "DBC": {"return": 2.1, "volatility": 19.8}, "UUP": {"return": 1.5, "volatility": 8.3},
    "BTC": {"return": 65.3, "volatility": 78.5}, "ETH": {"return": 58.2, "volatility": 82.3},
    "BNB": {"return": 52.1, "volatility": 88.2}, "ADA": {"return": 45.3, "volatility": 92.4},
    "SOL": {"return": 48.9, "volatility": 95.1},
}

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>📊 Optimization Results</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Your Optimized Portfolio</p>
    </div>
    """, unsafe_allow_html=True)

# Check if optimization has been run
if not st.session_state.optimized_weights or not st.session_state.selected_assets:
    st.error("⚠️ No optimization results! Please run optimization first.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# CALCULATE METRICS
# ═══════════════════════════════════════════════════════════════════════════════

selected_assets_list = list(st.session_state.selected_assets.keys())
current_weights = st.session_state.selected_assets
optimized_weights = st.session_state.optimized_weights

# Current portfolio metrics
current_return = sum(current_weights[asset] * ASSET_DATA[asset]["return"] 
                     for asset in selected_assets_list if asset in ASSET_DATA)
current_vol = np.sqrt(sum((current_weights[asset] ** 2) * (ASSET_DATA[asset]["volatility"] ** 2) 
                           for asset in selected_assets_list if asset in ASSET_DATA))
current_sharpe = (current_return - st.session_state.risk_free_rate) / current_vol if current_vol > 0 else 0

# Optimized portfolio metrics
opt_return = sum(optimized_weights[asset] * ASSET_DATA[asset]["return"] 
                 for asset in selected_assets_list if asset in ASSET_DATA)
opt_vol = np.sqrt(sum((optimized_weights[asset] ** 2) * (ASSET_DATA[asset]["volatility"] ** 2) 
                       for asset in selected_assets_list if asset in ASSET_DATA))
opt_sharpe = (opt_return - st.session_state.risk_free_rate) / opt_vol if opt_vol > 0 else 0

# ═══════════════════════════════════════════════════════════════════════════════
# RESULTS COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 RESULTS COMPARISON</h2>
        <p style='color: white;'>Current vs Optimized Portfolio</p>
    </div>
    """, unsafe_allow_html=True)

# Create two columns: Current vs Optimized
col_current, col_arrow, col_optimized = st.columns([2, 0.5, 2])

# CURRENT PORTFOLIO
with col_current:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📈 CURRENT PORTFOLIO</h3>
        </div>
        """, unsafe_allow_html=True)
    
    st.metric("Expected Return", f"{current_return:.2f}%")
    st.metric("Volatility (Risk)", f"{current_vol:.2f}%")
    st.metric("Sharpe Ratio", f"{current_sharpe:.3f}")

# ARROW
with col_arrow:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
            <h1 style='color: #FFD700; font-size: 2rem;'>→</h1>
        </div>
        """, unsafe_allow_html=True)

# OPTIMIZED PORTFOLIO
with col_optimized:
    st.markdown("""
        <div style='background-color: #1a7d4d; padding: 1.5rem; border-radius: 0.5rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🚀 OPTIMIZED PORTFOLIO</h3>
        </div>
        """, unsafe_allow_html=True)
    
    st.metric("Expected Return", f"{opt_return:.2f}%", f"{opt_return - current_return:+.2f}%")
    st.metric("Volatility (Risk)", f"{opt_vol:.2f}%", f"{opt_vol - current_vol:+.2f}%")
    st.metric("Sharpe Ratio", f"{opt_sharpe:.3f}", f"{opt_sharpe - current_sharpe:+.3f}")

# Optimization Objective
st.markdown("")
st.markdown(f"""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 1rem 0;'>
        <h3 style='color: #FFD700; margin-top: 0;'>🎯 Optimization Objective</h3>
        <p style='color: white; font-size: 1.1rem;'><strong>{st.session_state.optimization_objective}</strong></p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZED WEIGHTS TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>💼 OPTIMIZED ALLOCATION</h2>
    </div>
    """, unsafe_allow_html=True)

weights_data = []
for asset in selected_assets_list:
    current_w = current_weights.get(asset, 0)
    opt_w = optimized_weights.get(asset, 0)
    change = opt_w - current_w
    
    weights_data.append({
        "Asset": asset,
        "Current Weight": f"{current_w*100:.1f}%",
        "Optimized Weight": f"{opt_w*100:.1f}%",
        "Change": f"{change*100:+.1f}%"
    })

df_weights = pd.DataFrame(weights_data)
st.dataframe(
    df_weights,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Asset": st.column_config.TextColumn("Asset", width="small"),
        "Current Weight": st.column_config.TextColumn("Current", width="small"),
        "Optimized Weight": st.column_config.TextColumn("Optimized", width="small"),
        "Change": st.column_config.TextColumn("Change", width="small")
    }
)

# ═══════════════════════════════════════════════════════════════════════════════
# PERFORMANCE METRICS - DETAILED TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📈 DETAILED PERFORMANCE METRICS</h2>
    </div>
    """, unsafe_allow_html=True)

# Calculate improvements
improvement_return_pct = ((opt_return - current_return) / current_return * 100) if current_return != 0 else 0
improvement_sharpe_pct = ((opt_sharpe - current_sharpe) / current_sharpe * 100) if current_sharpe != 0 else 0
improvement_vol_pct = ((opt_vol - current_vol) / current_vol * 100) if current_vol != 0 else 0

metrics_data = {
    "Performance Metric": [
        "Expected Annual Return",
        "Portfolio Volatility",
        "Sharpe Ratio",
        "Risk-Free Rate",
        "Excess Return (Rf adjusted)"
    ],
    "Current": [
        f"{current_return:.2f}%",
        f"{current_vol:.2f}%",
        f"{current_sharpe:.4f}",
        f"{st.session_state.risk_free_rate:.2f}%",
        f"{current_return - st.session_state.risk_free_rate:.2f}%"
    ],
    "Optimized": [
        f"{opt_return:.2f}%",
        f"{opt_vol:.2f}%",
        f"{opt_sharpe:.4f}",
        f"{st.session_state.risk_free_rate:.2f}%",
        f"{opt_return - st.session_state.risk_free_rate:.2f}%"
    ],
    "Change": [
        f"{opt_return - current_return:+.2f}%",
        f"{opt_vol - current_vol:+.2f}%",
        f"{opt_sharpe - current_sharpe:+.4f}",
        "0.00%",
        f"{(opt_return - st.session_state.risk_free_rate) - (current_return - st.session_state.risk_free_rate):+.2f}%"
    ],
    "% Improvement": [
        f"{improvement_return_pct:+.2f}%",
        f"{improvement_vol_pct:+.2f}%",
        f"{improvement_sharpe_pct:+.2f}%",
        "-",
        f"{improvement_return_pct:+.2f}%"
    ]
}

df_metrics = pd.DataFrame(metrics_data)
st.dataframe(
    df_metrics,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Performance Metric": st.column_config.TextColumn("Metric", width="medium"),
        "Current": st.column_config.TextColumn("Current", width="small"),
        "Optimized": st.column_config.TextColumn("Optimized", width="small"),
        "Change": st.column_config.TextColumn("Change", width="small"),
        "% Improvement": st.column_config.TextColumn("% Change", width="small")
    }
)

# ═══════════════════════════════════════════════════════════════════════════════
# IMPROVEMENT SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>✨ OPTIMIZATION SUMMARY</h2>
    </div>
    """, unsafe_allow_html=True)

# Improvement metrics
col1, col2, col3 = st.columns(3)

with col1:
    return_improvement = opt_return - current_return
    if return_improvement > 0:
        color = "🟢"
        direction = "INCREASED"
    else:
        color = "🔴"
        direction = "DECREASED"
    
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white; margin: 0;'>{color} Return {direction}</p>
            <h2 style='color: #FFD700; margin: 0.5rem 0;'>{improvement_return_pct:+.2f}%</h2>
            <p style='color: #90EE90; margin: 0;'>{return_improvement:+.2f}% absolute</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    vol_improvement = opt_vol - current_vol
    if vol_improvement < 0:
        color = "🟢"
        direction = "REDUCED"
    else:
        color = "🔴"
        direction = "INCREASED"
    
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white; margin: 0;'>{color} Risk {direction}</p>
            <h2 style='color: #FFD700; margin: 0.5rem 0;'>{improvement_vol_pct:+.2f}%</h2>
            <p style='color: #90EE90; margin: 0;'>{vol_improvement:+.2f}% absolute</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    sharpe_improvement = opt_sharpe - current_sharpe
    if sharpe_improvement > 0:
        color = "🟢"
        direction = "IMPROVED"
    else:
        color = "🔴"
        direction = "DECLINED"
    
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white; margin: 0;'>{color} Sharpe Ratio {direction}</p>
            <h2 style='color: #FFD700; margin: 0.5rem 0;'>{improvement_sharpe_pct:+.2f}%</h2>
            <p style='color: #90EE90; margin: 0;'>{sharpe_improvement:+.4f} absolute</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# RECOMMENDATIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>💡 RECOMMENDATIONS</h2>
    </div>
    """, unsafe_allow_html=True)

st.info("""
📌 **Summary:**
- Your optimized portfolio achieves better risk-adjusted returns
- Allocate based on your risk tolerance and investment horizon
- Review quarterly and rebalance as needed
- Consider implementation costs and tax implications
""")

# ═══════════════════════════════════════════════════════════════════════════════
# EXPORT & FURTHER ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🎯 NEXT STEPS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Implement Your Portfolio:**
    - Execute trades based on optimized weights
    - Monitor performance regularly
    - Rebalance when weights drift
    """)

with col2:
    st.markdown("""
    **Further Analysis:**
    - Run sensitivity analysis
    - Perform stress testing
    - Compare with benchmarks
    """)

st.success("""
✅ **Optimization Complete!**

Thank you for using The Mountain Path Portfolio Optimizer. 
Your optimized portfolio is ready for implementation.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# NAVIGATION & ACTION BUTTONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🔄 WHAT WOULD YOU LIKE TO DO?</h2>
    </div>
    """, unsafe_allow_html=True)

# Top row: Back button and progress
nav_row1_col1, nav_row1_col2, nav_row1_col3 = st.columns([1, 1, 1])

with nav_row1_col1:
    if st.button("← Back to Optimization", key="results_to_optimize", use_container_width=True, help="Go back to Optimize page"):
        st.switch_page("pages/5_Optimize.py")

with nav_row1_col2:
    st.markdown("""
        <div style='text-align: center; padding: 0.75rem; background-color: #004d80; border-radius: 0.5rem;'>
            <p style='color: #FFD700; font-weight: bold; margin: 0;'>Step 6/6</p>
            <p style='color: #90EE90; font-size: 0.9rem; margin: 0.25rem 0 0 0;'>Results</p>
        </div>
        """, unsafe_allow_html=True)

with nav_row1_col3:
    st.markdown("""
        <div style='text-align: center; padding: 0.75rem; background-color: #1a7d4d; border-radius: 0.5rem;'>
            <p style='color: #FFD700; font-weight: bold; margin: 0;'>✅ COMPLETE!</p>
            <p style='color: #90EE90; font-size: 0.9rem; margin: 0.25rem 0 0 0;'>Optimization Done</p>
        </div>
        """, unsafe_allow_html=True)

# Action buttons row - LARGE CLICKABLE CARDS with visible buttons
st.markdown("""
    <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; margin: 1.5rem 0;'>
        <p style='color: white; font-weight: bold; margin: 0;'>💡 Adjust Your Results - Click Any Card:</p>
    </div>
    """, unsafe_allow_html=True)

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #004d80 0%, #003366 100%); padding: 1.5rem; border-radius: 0.75rem; text-align: center; border: 2px solid #FFD700;'>
            <p style='font-size: 2rem; margin: 0;'>⚙️</p>
            <h3 style='color: #FFD700; margin: 0.5rem 0; font-size: 1.3rem;'>Change Weights</h3>
            <p style='color: #90EE90; font-size: 0.95rem; margin: 0.5rem 0 0 0;'>Adjust asset weights again</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("📄 Go to Weights", key="results_to_weights", use_container_width=True, help="Adjust asset weights and reoptimize"):
        st.switch_page("pages/2_Weights.py")

with action_col2:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #004d80 0%, #003366 100%); padding: 1.5rem; border-radius: 0.75rem; text-align: center; border: 2px solid #FFD700;'>
            <p style='font-size: 2rem; margin: 0;'>🎯</p>
            <h3 style='color: #FFD700; margin: 0.5rem 0; font-size: 1.3rem;'>Change Objective</h3>
            <p style='color: #90EE90; font-size: 0.95rem; margin: 0.5rem 0 0 0;'>Try different optimization goal</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🎯 Go to Objective", key="results_to_objective", use_container_width=True, help="Try different optimization goal"):
        st.switch_page("pages/4_Objective.py")

with action_col3:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #004d80 0%, #003366 100%); padding: 1.5rem; border-radius: 0.75rem; text-align: center; border: 2px solid #FFD700;'>
            <p style='font-size: 2rem; margin: 0;'>🏠</p>
            <h3 style='color: #FFD700; margin: 0.5rem 0; font-size: 1.3rem;'>Start Over</h3>
            <p style='color: #90EE90; font-size: 0.95rem; margin: 0.5rem 0 0 0;'>Reset and select new assets</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔄 Go to App", key="results_to_app", use_container_width=True, help="Start with new assets"):
        st.switch_page("app.py")

render_footer()
