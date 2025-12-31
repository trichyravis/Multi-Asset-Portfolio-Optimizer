
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - HOME PAGE (ENHANCED)
Portfolio Optimization - Complete Workflow with Pre-Analysis
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import pandas as pd
from config_enhanced import PAGE_CONFIG, ASSET_CLASSES
from styles_enhanced import apply_main_styles, render_header, render_footer
from portfolio_analytics_enhanced import (
    calculate_portfolio_metrics, 
    plot_efficient_frontier_3d,
    plot_weight_comparison,
    create_metrics_comparison
)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header(title="🏠 Portfolio Optimization Setup")

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "selected_classes" not in st.session_state:
    st.session_state.selected_classes = []
if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}
if "weights" not in st.session_state:
    st.session_state.weights = {}
if "optimization_method" not in st.session_state:
    st.session_state.optimization_method = "Maximize Sharpe Ratio"

# ═══════════════════════════════════════════════════════════════════════════════
# INTRODUCTION SECTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
### 📚 Welcome to Professional Portfolio Optimization

This tool helps you build a diversified investment portfolio using **Modern Portfolio Theory (MPT)**.

**What We Do:**
- 📊 **Analyze** your portfolio composition
- 🎯 **Optimize** asset allocation for better risk-adjusted returns
- 📈 **Visualize** efficient frontiers and performance metrics
- 💡 **Recommend** optimal portfolio weights

**3-Step Process:**
1. **Select Assets** - Choose asset classes and specific investments
2. **Set Weights** - Allocate percentage distribution (must sum to 100%)
3. **Optimize** - Apply optimization strategy and view results

---
""")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: SELECT ASSET CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 🎯 STEP 1: SELECT ASSET CLASSES")
st.write("Choose one or more asset classes for your portfolio. Each class offers different benefits:")

st.markdown("""
| Class | Description | Risk | Expected Return |
|-------|-------------|------|-----------------|
| 📈 **Equities** | Stocks - Growth potential, higher volatility | High | 8-28% |
| 📊 **Indices** | Market baskets - Diversified exposure | Medium | 8-15% |
| 💰 **Bonds** | Fixed income - Stable, lower returns | Low | 3-5% |
| 🏆 **Commodities** | Raw materials - Inflation hedge | Medium-High | 2-8% |
| ₿ **Crypto** | Digital assets - High growth, very volatile | Very High | 30-60% |
""")

selected_classes = st.multiselect(
    label="Select Asset Classes (minimum 1 required):",
    options=list(ASSET_CLASSES.keys()),
    default=st.session_state.selected_classes,
    help="Select the asset classes you want to include in your portfolio"
)

st.session_state.selected_classes = selected_classes

if not selected_classes:
    st.warning("⚠️ Please select at least one asset class to continue")
    st.stop()

st.success(f"✅ Selected {len(selected_classes)} asset class(es)")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: SELECT SPECIFIC ASSETS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 🎯 STEP 2: SELECT SPECIFIC ASSETS")
st.write("Choose specific investments from each asset class. Click each section to expand:")

selected_assets = {}
total_selected = 0

for asset_class in selected_classes:
    with st.expander(f"📌 {asset_class} ({ASSET_CLASSES[asset_class]['description']})", expanded=False):
        st.write(f"**{ASSET_CLASSES[asset_class]['description']}**")
        
        assets_in_class = ASSET_CLASSES[asset_class]['assets']
        
        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        selected_in_class = st.multiselect(
            label=f"Select {asset_class}:",
            options=list(assets_in_class.keys()),
            default=st.session_state.selected_assets.get(asset_class, []),
            label_visibility="collapsed",
            help=f"Select which {asset_class.lower()} to include"
        )
        
        if selected_in_class:
            # Display details of selected assets
            st.write(f"\n**Selected {asset_class}:**")
            asset_details = []
            for ticker in selected_in_class:
                asset_info = assets_in_class[ticker]
                asset_details.append({
                    "Ticker": ticker,
                    "Asset Name": asset_info.get("name", ""),
                    "Type": asset_info.get("sector", asset_info.get("description", ""))
                })
            
            df_assets = pd.DataFrame(asset_details)
            st.dataframe(df_assets, use_container_width=True, hide_index=True)
            
            selected_assets[asset_class] = selected_in_class
            total_selected += len(selected_in_class)

st.session_state.selected_assets = selected_assets

if total_selected == 0:
    st.warning("⚠️ Please select at least one asset from at least one class to continue")
    st.stop()

st.success(f"✅ Selected {total_selected} total assets")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3: ALLOCATE WEIGHTS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 🎯 STEP 3: ALLOCATE PORTFOLIO WEIGHTS")
st.write("Distribute your investment across selected assets. Weights must sum to 100%.")

# Flatten all assets
all_assets = []
for asset_class, assets in selected_assets.items():
    all_assets.extend(assets)

# Default: equal weights
equal_weight = 100 / len(all_assets)

# Auto-populate button
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    if st.button("📊 Equal Weights", use_container_width=True, help="Set all assets to equal weight"):
        for asset in all_assets:
            st.session_state.weights[asset] = equal_weight
        st.rerun()

with col2:
    if st.button("🔄 Reset", use_container_width=True, help="Clear all weights"):
        st.session_state.weights = {}
        st.rerun()

# Manual weight input
st.write("\n**Adjust weights individually:**")

weights = {}
weight_cols = st.columns(min(3, len(all_assets)))

for idx, asset in enumerate(all_assets):
    col = weight_cols[idx % min(3, len(all_assets))]
    with col:
        weight = st.number_input(
            label=f"**{asset}** (%)",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.weights.get(asset, equal_weight),
            step=1.0,
            label_visibility="collapsed",
        )
        weights[asset] = weight

st.session_state.weights = weights

# Weight validation
total_weight = sum(weights.values())
weight_valid = abs(total_weight - 100.0) < 0.01

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Weight", f"{total_weight:.1f}%")

with col2:
    if weight_valid:
        st.success("✅ Weights sum to 100%")
    elif total_weight > 100.0:
        st.error(f"❌ Over: +{total_weight - 100:.1f}%")
    else:
        st.warning(f"❌ Under: -{100 - total_weight:.1f}%")

with col3:
    st.metric("Assets in Portfolio", len(all_assets))

if not weight_valid:
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# PRE-OPTIMIZATION ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 📊 PRE-OPTIMIZATION ANALYSIS")
st.write("Analysis of your current portfolio before optimization:")

# Calculate current portfolio metrics
current_metrics = calculate_portfolio_metrics(all_assets, weights)

# Key metrics display
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Annual Return",
        f"{current_metrics['annual_return']:.2%}",
        help="Expected annual return"
    )

with col2:
    st.metric(
        "Volatility (Risk)",
        f"{current_metrics['volatility']:.2%}",
        help="Standard deviation of returns"
    )

with col3:
    st.metric(
        "Sharpe Ratio",
        f"{current_metrics['sharpe_ratio']:.2f}",
        help="Risk-adjusted return metric"
    )

with col4:
    st.metric(
        "Max Drawdown",
        f"{current_metrics['max_drawdown']:.2%}",
        help="Maximum expected loss"
    )

# Detailed metrics table
st.markdown("**Detailed Metrics:**")
metrics_df = pd.DataFrame({
    "Metric": [
        "Annual Return",
        "Annual Volatility",
        "Sharpe Ratio",
        "Sortino Ratio",
        "Max Drawdown"
    ],
    "Your Portfolio": [
        f"{current_metrics['annual_return']:.2%}",
        f"{current_metrics['volatility']:.2%}",
        f"{current_metrics['sharpe_ratio']:.2f}",
        f"{current_metrics['sortino_ratio']:.2f}",
        f"{current_metrics['max_drawdown']:.2%}"
    ],
    "Interpretation": [
        "Expected yearly gain",
        "Price fluctuation/risk",
        "Return per unit of risk",
        "Return per unit of downside risk",
        "Worst expected loss"
    ]
})

st.dataframe(metrics_df, use_container_width=True, hide_index=True)

# Portfolio composition
st.markdown("**Portfolio Composition:**")
composition_df = pd.DataFrame({
    "Asset": all_assets,
    "Weight (%)": [f"{weights.get(asset, 0):.1f}%" for asset in all_assets],
    "Expected Return": [f"{current_metrics['annual_return']:.2%}" for _ in all_assets],
})
st.dataframe(composition_df, use_container_width=True, hide_index=True)

# Charts
st.markdown("---")
st.markdown("**Portfolio Visualization:**")

col1, col2 = st.columns(2)

with col1:
    # Pie chart of weights
    fig_pie = {
        "data": [{"values": list(weights.values()), "labels": list(weights.keys()), "type": "pie"}],
        "layout": {"title": "Asset Allocation", "paper_bgcolor": "rgba(0, 51, 102, 0)"}
    }
    st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": False})

with col2:
    # Metrics summary
    fig_metrics = {
        "data": [{
            "x": ["Annual Return", "Volatility", "Max Drawdown"],
            "y": [current_metrics['annual_return'] * 100, current_metrics['volatility'] * 100, abs(current_metrics['max_drawdown']) * 100],
            "type": "bar",
            "marker": {"color": ["gold", "lightblue", "salmon"]}
        }],
        "layout": {
            "title": "Key Metrics (%)",
            "paper_bgcolor": "rgba(0, 51, 102, 0)",
            "yaxis": {"title": "Percentage (%)"}
        }
    }
    st.plotly_chart(fig_metrics, use_container_width=True, config={"displayModeBar": False})

# ═══════════════════════════════════════════════════════════════════════════════
# SELECT OPTIMIZATION METHOD
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 🎯 SELECT OPTIMIZATION OBJECTIVE")
st.write("Choose how to optimize your portfolio:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📈 Maximize Returns", use_container_width=True, help="Aggressive: Focus on growth"):
        st.session_state.optimization_method = "Maximize Returns"

with col2:
    if st.button("🛡️ Minimize Risk", use_container_width=True, help="Conservative: Reduce volatility"):
        st.session_state.optimization_method = "Minimize Risk"

with col3:
    if st.button("⚖️ Maximize Sharpe Ratio", use_container_width=True, help="Balanced: Best risk-adjusted returns (RECOMMENDED)"):
        st.session_state.optimization_method = "Maximize Sharpe Ratio"

st.info(f"**Selected Objective:** {st.session_state.optimization_method}")

optimization_descriptions = {
    "Maximize Returns": "🚀 Prioritize growth - Accept higher volatility for better returns",
    "Minimize Risk": "🛡️ Prioritize safety - Reduce volatility, accept lower returns",
    "Maximize Sharpe Ratio": "⚖️ Balanced approach - Optimal risk-adjusted returns (RECOMMENDED)"
}

st.markdown(f"**Strategy:** {optimization_descriptions[st.session_state.optimization_method]}")

# ═══════════════════════════════════════════════════════════════════════════════
# PROCEED TO OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🚀 NEXT STEP")

col1, col2 = st.columns([1, 3])

with col1:
    if st.button("🚀 OPTIMIZE PORTFOLIO", use_container_width=True, type="primary"):
        st.switch_page("pages/2_📊_Results_Enhanced.py")

with col2:
    st.write("Click to proceed to optimization and see recommended portfolio allocation")

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

render_footer()
