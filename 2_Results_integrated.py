"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - RESULTS PAGE
Portfolio Optimization Results & Analysis
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import pandas as pd
import numpy as np
from styles import apply_main_styles, render_header, render_footer
from components import Section, MetricsDisplay, TabsDisplay, InfoBox

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="Results - Portfolio Optimizer", layout="wide")
apply_main_styles()
render_header(
    title="📊 Portfolio Results",
    method=st.session_state.mpt_objective if "mpt_objective" in st.session_state else "Maximize Sharpe Ratio"
)

# ═══════════════════════════════════════════════════════════════════════════════
# VERIFY SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if not st.session_state.selected_assets:
    st.error("❌ No portfolio configured. Please go to Home page and set up your portfolio.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# SAMPLE RESULTS DATA (Replace with actual optimization)
# ═══════════════════════════════════════════════════════════════════════════════

# Flatten assets
all_assets = []
for asset_class, assets in st.session_state.selected_assets.items():
    all_assets.extend(assets)

# Create sample results (in production, replace with actual portfolio_analytics results)
original_weights = st.session_state.weights
optimized_weights = {asset: original_weights.get(asset, 0) * np.random.uniform(0.8, 1.2) 
                     for asset in all_assets}
total_optimized = sum(optimized_weights.values())
optimized_weights = {asset: (weight / total_optimized) * 100 for asset, weight in optimized_weights.items()}

# ═══════════════════════════════════════════════════════════════════════════════
# METRICS COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

Section.render("PORTFOLIO METRICS COMPARISON", emoji="📊")

metrics_data = {
    "Metric": ["Annual Return", "Annual Volatility", "Sharpe Ratio", "Sortino Ratio", "Max Drawdown"],
    "Original Portfolio": ["8.5%", "12.3%", "0.69", "0.92", "-18.5%"],
    "Optimized Portfolio": ["9.2%", "11.8%", "0.78", "1.05", "-16.2%"],
    "Improvement": ["↑ +0.7%", "↓ -0.5%", "↑ +0.09", "↑ +0.13", "↑ +2.3%"]
}

metrics_df = pd.DataFrame(metrics_data)
st.dataframe(metrics_df, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
# KEY METRICS DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
Section.render("KEY IMPROVEMENTS", emoji="✨")

MetricsDisplay.render_metrics([
    {
        "title": "Annual Return",
        "value": "9.2%",
        "emoji": "📈",
        "description": "↑ +0.7% improvement"
    },
    {
        "title": "Risk (Volatility)",
        "value": "11.8%",
        "emoji": "⚡",
        "description": "↓ -0.5% improvement"
    },
    {
        "title": "Sharpe Ratio",
        "value": "0.78",
        "emoji": "🎯",
        "description": "↑ +0.09 improvement"
    },
    {
        "title": "Max Drawdown",
        "value": "-16.2%",
        "emoji": "📉",
        "description": "↑ +2.3% improvement"
    },
], columns=4)

# ═══════════════════════════════════════════════════════════════════════════════
# WEIGHT COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
Section.render("PORTFOLIO WEIGHT COMPARISON", emoji="⚖️")

# Create comparison dataframe
weight_comparison = pd.DataFrame({
    "Asset": all_assets,
    "Original Weight (%)": [original_weights.get(asset, 0) for asset in all_assets],
    "Optimized Weight (%)": [optimized_weights.get(asset, 0) for asset in all_assets],
})

weight_comparison["Change (%)"] = (weight_comparison["Optimized Weight (%)"] - 
                                   weight_comparison["Original Weight (%)"])

st.dataframe(weight_comparison, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
# VISUALIZATION TABS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
Section.render("DETAILED ANALYSIS", emoji="📈")

def render_efficient_frontier():
    st.write("📊 **3D Efficient Frontier Visualization** (Coming in production version)")
    st.info("Hover over points to see portfolio details. Click and drag to rotate.")
    # In production: st.plotly_chart(fig_3d)

def render_weight_chart():
    st.write("📊 **Weight Comparison Chart**")
    chart_data = pd.DataFrame({
        "Asset": all_assets,
        "Original": [original_weights.get(asset, 0) for asset in all_assets],
        "Optimized": [optimized_weights.get(asset, 0) for asset in all_assets],
    })
    st.bar_chart(chart_data.set_index("Asset"))

def render_metrics_table():
    st.write("📊 **Detailed Metrics**")
    detailed_metrics = pd.DataFrame({
        "Metric": ["Annual Return", "Annual Volatility", "Sharpe Ratio", "Sortino Ratio", 
                   "Max Drawdown", "Value at Risk (95%)", "Expected Shortfall"],
        "Original": ["8.50%", "12.30%", "0.69", "0.92", "-18.50%", "-2.15%", "-2.85%"],
        "Optimized": ["9.20%", "11.80%", "0.78", "1.05", "-16.20%", "-1.98%", "-2.61%"],
    })
    st.dataframe(detailed_metrics, use_container_width=True, hide_index=True)

TabsDisplay.render({
    "3️⃣ Efficient Frontier": render_efficient_frontier,
    "📊 Weight Comparison": render_weight_chart,
    "📋 Metrics Table": render_metrics_table,
})

# ═══════════════════════════════════════════════════════════════════════════════
# ACTION BUTTONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.write("### Next Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("← Back to Setup", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

with col2:
    if st.button("💾 Save Results", use_container_width=True):
        InfoBox.success("✅ Results saved successfully!")

with col3:
    if st.button("📥 Download CSV", use_container_width=True):
        InfoBox.success("✅ Download started!")

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

render_footer()
