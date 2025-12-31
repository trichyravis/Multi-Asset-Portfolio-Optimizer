
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
📊 Portfolio Analysis - Current Performance Metrics
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
if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "investment_period" not in st.session_state:
    st.session_state.investment_period = 5

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET DATA - Historical Returns & Volatility (Annualized %)
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_DATA = {
    # Stocks
    "AAPL": {"return": 28.5, "volatility": 32.1, "class": "Stocks"},
    "MSFT": {"return": 26.3, "volatility": 28.9, "class": "Stocks"},
    "GOOGL": {"return": 24.7, "volatility": 30.2, "class": "Stocks"},
    "AMZN": {"return": 22.1, "volatility": 34.5, "class": "Stocks"},
    "NVDA": {"return": 35.2, "volatility": 45.8, "class": "Stocks"},
    "JPM": {"return": 15.3, "volatility": 25.6, "class": "Stocks"},
    "BAC": {"return": 12.5, "volatility": 28.3, "class": "Stocks"},
    "XOM": {"return": 8.9, "volatility": 22.4, "class": "Stocks"},
    "PG": {"return": 9.7, "volatility": 16.8, "class": "Stocks"},
    "KO": {"return": 7.3, "volatility": 18.2, "class": "Stocks"},
    
    # Bonds
    "BND": {"return": 4.2, "volatility": 6.3, "class": "Bonds"},
    "AGG": {"return": 4.5, "volatility": 6.8, "class": "Bonds"},
    "LQD": {"return": 5.1, "volatility": 7.4, "class": "Bonds"},
    "TLT": {"return": 3.8, "volatility": 8.9, "class": "Bonds"},
    "SHV": {"return": 3.2, "volatility": 2.1, "class": "Bonds"},
    
    # Commodities
    "GLD": {"return": 6.5, "volatility": 14.2, "class": "Commodities"},
    "SLV": {"return": 5.8, "volatility": 18.6, "class": "Commodities"},
    "USO": {"return": 3.2, "volatility": 22.1, "class": "Commodities"},
    "DBC": {"return": 2.1, "volatility": 19.8, "class": "Commodities"},
    "UUP": {"return": 1.5, "volatility": 8.3, "class": "Commodities"},
    
    # Cryptocurrencies
    "BTC": {"return": 65.3, "volatility": 78.5, "class": "Cryptocurrencies"},
    "ETH": {"return": 58.2, "volatility": 82.3, "class": "Cryptocurrencies"},
    "BNB": {"return": 52.1, "volatility": 88.2, "class": "Cryptocurrencies"},
    "ADA": {"return": 45.3, "volatility": 92.4, "class": "Cryptocurrencies"},
    "SOL": {"return": 48.9, "volatility": 95.1, "class": "Cryptocurrencies"},
}

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>📊 Portfolio Analysis</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Current Performance Metrics</p>
    </div>
    """, unsafe_allow_html=True)

# Check if assets are selected
if not st.session_state.selected_assets:
    st.error("⚠️ No assets selected! Please go back and select assets first.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# GET PORTFOLIO DATA
# ═══════════════════════════════════════════════════════════════════════════════

selected_assets_list = list(st.session_state.selected_assets.keys())
weights = list(st.session_state.selected_assets.values())

# Calculate portfolio metrics
portfolio_return = 0
portfolio_variance = 0

for i, asset in enumerate(selected_assets_list):
    if asset in ASSET_DATA:
        portfolio_return += weights[i] * ASSET_DATA[asset]["return"]

# Simplified volatility calculation (assumes correlation of 0.3)
for i, asset_i in enumerate(selected_assets_list):
    if asset_i in ASSET_DATA:
        portfolio_variance += (weights[i] ** 2) * (ASSET_DATA[asset_i]["volatility"] ** 2)

# Add cross-product terms with correlation
for i, asset_i in enumerate(selected_assets_list):
    for j, asset_j in enumerate(selected_assets_list):
        if i < j and asset_i in ASSET_DATA and asset_j in ASSET_DATA:
            correlation = 0.3  # Assumed correlation
            portfolio_variance += 2 * weights[i] * weights[j] * ASSET_DATA[asset_i]["volatility"] * ASSET_DATA[asset_j]["volatility"] * correlation

portfolio_volatility = np.sqrt(portfolio_variance)

# Calculate Sharpe Ratio
risk_free_rate = st.session_state.risk_free_rate
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility if portfolio_volatility > 0 else 0

# Calculate Sortino Ratio (simplified - assumes half the downside volatility)
downside_volatility = portfolio_volatility * 0.6
sortino_ratio = (portfolio_return - risk_free_rate) / downside_volatility if downside_volatility > 0 else 0

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO INFORMATION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown(f"""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📋 PORTFOLIO COMPOSITION</h2>
        <p style='color: white;'>Selected {len(selected_assets_list)} assets with current weights</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO METRICS - KEY NUMBERS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📈 KEY METRICS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Expected Return",
        f"{portfolio_return:.2f}%",
        help="Annualized expected return based on historical data"
    )

with col2:
    st.metric(
        "Volatility",
        f"{portfolio_volatility:.2f}%",
        help="Standard deviation of returns (Risk)"
    )

with col3:
    st.metric(
        "Sharpe Ratio",
        f"{sharpe_ratio:.3f}",
        help=f"Return per unit of risk (RF={risk_free_rate:.2f}%)"
    )

with col4:
    st.metric(
        "Sortino Ratio",
        f"{sortino_ratio:.3f}",
        help="Return per unit of downside risk"
    )

# ═══════════════════════════════════════════════════════════════════════════════
# ASSUMPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚙️ YOUR ASSUMPTIONS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Risk-Free Rate", f"{risk_free_rate:.2f}%")

with col2:
    st.metric("Investment Period", f"{st.session_state.investment_period} years")

with col3:
    st.metric("Assumed Correlation", "30%")

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET BREAKDOWN TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 ASSET BREAKDOWN</h2>
    </div>
    """, unsafe_allow_html=True)

# Create detailed asset table
asset_data_list = []
for asset, weight in st.session_state.selected_assets.items():
    if asset in ASSET_DATA:
        data = ASSET_DATA[asset]
        asset_contribution = weight * data["return"]
        asset_data_list.append({
            "Asset": asset,
            "Weight": f"{weight*100:.1f}%",
            "Return": f"{data['return']:.2f}%",
            "Volatility": f"{data['volatility']:.2f}%",
            "Class": data["class"],
            "Contribution to Portfolio Return": f"{asset_contribution:.2f}%"
        })

df_assets = pd.DataFrame(asset_data_list)
st.dataframe(
    df_assets,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Asset": st.column_config.TextColumn("Asset", width="small"),
        "Weight": st.column_config.TextColumn("Weight", width="small"),
        "Return": st.column_config.TextColumn("Return", width="small"),
        "Volatility": st.column_config.TextColumn("Volatility", width="small"),
        "Class": st.column_config.TextColumn("Class", width="small"),
        "Contribution to Portfolio Return": st.column_config.TextColumn("Contribution", width="medium")
    }
)

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO VISUALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📍 PORTFOLIO ALLOCATION</h2>
    </div>
    """, unsafe_allow_html=True)

# Create pie chart data
pie_data = {asset: weight*100 for asset, weight in st.session_state.selected_assets.items()}

col1, col2 = st.columns([2, 1])

with col1:
    # Simple text-based allocation display
    allocation_text = ""
    for asset, pct in sorted(pie_data.items(), key=lambda x: x[1], reverse=True):
        bar_length = int(pct / 2)  # Scale to fit
        allocation_text += f"{asset:6} {'█' * bar_length} {pct:5.1f}%\n"
    
    st.code(allocation_text, language="text")

with col2:
    st.info(f"""
    **Total Assets:** {len(selected_assets_list)}
    
    **Total Weight:** 100%
    
    **Expected Annual Return:** {portfolio_return:.2f}%
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# NEXT STEPS - NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🚀 NEXT STEPS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Step 6: Choose Objective**
    - Go to 🎯 **Objective**
    - Select optimization goal
    """)

with col2:
    st.markdown("""
    **Step 7: Run Optimization**
    - Go to 🚀 **Optimize**
    - Start optimization
    """)

with col3:
    st.markdown("""
    **Step 8: View Results**
    - Go to 📊 **Results**
    - See optimized portfolio
    """)

# Navigation info with breadcrumb
st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🔄 NAVIGATION</h2>
    </div>
    """, unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])

with nav_col1:
    if st.button("← Back to Weights", key="analysis_to_weights", use_container_width=True):
        st.switch_page("pages/2_Weights.py")

with nav_col2:
    st.markdown("""
        <div style='text-align: center; padding: 0.75rem; background-color: #004d80; border-radius: 0.5rem;'>
            <p style='color: #FFD700; font-weight: bold; margin: 0;'>Step 3/6</p>
            <p style='color: #90EE90; font-size: 0.9rem; margin: 0.25rem 0 0 0;'>Analysis</p>
        </div>
        """, unsafe_allow_html=True)

with nav_col3:
    if st.button("Next: Objective →", key="analysis_to_objective", use_container_width=True):
        st.switch_page("pages/4_Objective.py")

render_footer()
