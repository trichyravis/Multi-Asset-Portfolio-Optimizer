
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
🚀 Portfolio Optimization - Run Optimization
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
if "optimization_objective" not in st.session_state:
    st.session_state.optimization_objective = "Maximize Sharpe Ratio"
if "optimized_weights" not in st.session_state:
    st.session_state.optimized_weights = {}
if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5

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
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🚀 Run Optimization</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Execute portfolio optimization</p>
    </div>
    """, unsafe_allow_html=True)

# Check if assets are selected
if not st.session_state.selected_assets:
    st.error("⚠️ No assets selected! Please go back and select assets first.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZATION EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚙️ OPTIMIZATION PARAMETERS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Objective", st.session_state.optimization_objective)

with col2:
    st.metric("🎯 Assets", len(st.session_state.selected_assets))

with col3:
    st.metric("💰 Risk-Free Rate", f"{st.session_state.risk_free_rate:.2f}%")

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZATION LOGIC
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🔄 RUNNING OPTIMIZATION...</h2>
    </div>
    """, unsafe_allow_html=True)

# Run optimization based on objective
selected_assets_list = list(st.session_state.selected_assets.keys())
current_weights = list(st.session_state.selected_assets.values())

# Calculate metrics for current portfolio
current_return = sum(current_weights[i] * ASSET_DATA[asset]["return"] 
                     for i, asset in enumerate(selected_assets_list) if asset in ASSET_DATA)
current_vol = np.sqrt(sum((current_weights[i] ** 2) * (ASSET_DATA[asset]["volatility"] ** 2) 
                           for i, asset in enumerate(selected_assets_list) if asset in ASSET_DATA))
current_sharpe = (current_return - st.session_state.risk_free_rate) / current_vol if current_vol > 0 else 0

# Optimization
if st.session_state.optimization_objective == "Maximize Sharpe Ratio":
    # Allocate more to high sharpe ratio assets
    sharpe_ratios = {}
    for asset in selected_assets_list:
        if asset in ASSET_DATA:
            sharpe = (ASSET_DATA[asset]["return"] - st.session_state.risk_free_rate) / ASSET_DATA[asset]["volatility"]
            sharpe_ratios[asset] = max(sharpe, 0)
    
    total_sharpe = sum(sharpe_ratios.values())
    if total_sharpe > 0:
        optimized_weights = {asset: sharpe_ratios[asset] / total_sharpe for asset in selected_assets_list}
    else:
        optimized_weights = {asset: 1.0 / len(selected_assets_list) for asset in selected_assets_list}

elif st.session_state.optimization_objective == "Minimize Risk":
    # Allocate inversely to volatility
    inv_vols = {}
    for asset in selected_assets_list:
        if asset in ASSET_DATA:
            inv_vols[asset] = 1.0 / ASSET_DATA[asset]["volatility"]
    
    total_inv_vol = sum(inv_vols.values())
    optimized_weights = {asset: inv_vols[asset] / total_inv_vol for asset in selected_assets_list}

elif st.session_state.optimization_objective == "Maximize Return":
    # Allocate 100% to highest return asset
    max_asset = max(selected_assets_list, 
                    key=lambda x: ASSET_DATA[x]["return"] if x in ASSET_DATA else 0)
    optimized_weights = {asset: (1.0 if asset == max_asset else 0.0) for asset in selected_assets_list}

else:  # Equal Weight
    optimized_weights = {asset: 1.0 / len(selected_assets_list) for asset in selected_assets_list}

# Calculate optimized metrics
opt_return = sum(optimized_weights[asset] * ASSET_DATA[asset]["return"] 
                 for asset in selected_assets_list if asset in ASSET_DATA)
opt_vol = np.sqrt(sum((optimized_weights[asset] ** 2) * (ASSET_DATA[asset]["volatility"] ** 2) 
                       for asset in selected_assets_list if asset in ASSET_DATA))
opt_sharpe = (opt_return - st.session_state.risk_free_rate) / opt_vol if opt_vol > 0 else 0

st.session_state.optimized_weights = optimized_weights

# Display success message
st.success("""
✅ **Optimization Complete!**

Optimization has been executed successfully using your selected objective.
""")

# ═══════════════════════════════════════════════════════════════════════════════
# IMPROVEMENT METRICS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📈 OPTIMIZATION RESULTS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

improvement_return = ((opt_return - current_return) / current_return * 100) if current_return != 0 else 0
improvement_sharpe = ((opt_sharpe - current_sharpe) / current_sharpe * 100) if current_sharpe != 0 else 0

with col1:
    st.metric(
        "Return Improvement",
        f"{improvement_return:+.2f}%",
        delta=f"{opt_return - current_return:.2f}%"
    )

with col2:
    st.metric(
        "Volatility Change",
        f"{opt_vol:.2f}%",
        delta=f"{opt_vol - current_vol:.2f}%"
    )

with col3:
    st.metric(
        "Sharpe Improvement",
        f"{improvement_sharpe:+.2f}%",
        delta=f"{opt_sharpe - current_sharpe:.3f}"
    )

# ═══════════════════════════════════════════════════════════════════════════════
# NEXT STEPS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🎯 NEXT STEPS</h2>
    </div>
    """, unsafe_allow_html=True)

st.info("""
📊 **View Results:** Go to sidebar → 📊 **Results** to see detailed optimized portfolio breakdown and comparison with current allocation.
""")

render_footer()
