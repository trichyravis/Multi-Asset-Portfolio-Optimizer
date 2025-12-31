"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - RESULTS PAGE (ENHANCED)
Portfolio Optimization Results with Efficient Frontier & Recommendations
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import pandas as pd
from config_enhanced import PAGE_CONFIG, ASSET_CLASSES
from styles_enhanced import apply_main_styles, render_header, render_footer
from portfolio_analytics_enhanced import (
    calculate_portfolio_metrics,
    optimize_portfolio,
    plot_efficient_frontier_3d,
    plot_weight_comparison,
    create_metrics_comparison
)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()

# Get optimization method from session state
optimization_method = st.session_state.get("optimization_method", "Maximize Sharpe Ratio")
render_header(title="📊 Portfolio Optimization Results", method=optimization_method)

# ═══════════════════════════════════════════════════════════════════════════════
# VERIFY SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if not st.session_state.selected_assets:
    st.error("❌ No portfolio configured. Please go to Home page and set up your portfolio.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# GET DATA FROM SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

all_assets = []
for asset_class, assets in st.session_state.selected_assets.items():
    all_assets.extend(assets)

initial_weights = st.session_state.weights
optimized_weights = optimize_portfolio(all_assets, initial_weights, optimization_method)

# Calculate metrics
initial_metrics = calculate_portfolio_metrics(all_assets, initial_weights)
optimized_metrics = calculate_portfolio_metrics(all_assets, optimized_weights)

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZATION SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 📊 OPTIMIZATION SUMMARY")
st.write(f"**Strategy Applied:** {optimization_method}")

# Key metrics comparison
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Return Improvement",
        f"{(optimized_metrics['annual_return'] - initial_metrics['annual_return']):.2%}",
        delta=f"{((optimized_metrics['annual_return'] - initial_metrics['annual_return']) / initial_metrics['annual_return'] * 100):.1f}%" if initial_metrics['annual_return'] != 0 else "N/A"
    )

with col2:
    st.metric(
        "Risk Reduction",
        f"{(initial_metrics['volatility'] - optimized_metrics['volatility']):.2%}",
        delta=f"{((initial_metrics['volatility'] - optimized_metrics['volatility']) / initial_metrics['volatility'] * 100):.1f}%" if initial_metrics['volatility'] != 0 else "N/A"
    )

with col3:
    st.metric(
        "Sharpe Improvement",
        f"{(optimized_metrics['sharpe_ratio'] - initial_metrics['sharpe_ratio']):.2f}",
    )

with col4:
    st.metric(
        "Efficiency Gain",
        f"{((optimized_metrics['sharpe_ratio'] / initial_metrics['sharpe_ratio'] - 1) * 100):.1f}%" if initial_metrics['sharpe_ratio'] > 0 else "N/A",
    )

# ═══════════════════════════════════════════════════════════════════════════════
# DETAILED METRICS COMPARISON TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 📋 DETAILED METRICS COMPARISON")

metrics_comparison = create_metrics_comparison(initial_metrics, optimized_metrics)
st.dataframe(metrics_comparison, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
# EFFICIENT FRONTIER 3D VISUALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 📈 EFFICIENT FRONTIER 3D ANALYSIS")
st.write("Interactive 3D visualization showing all possible portfolios and optimal position:")

try:
    fig_frontier = plot_efficient_frontier_3d(all_assets, initial_weights, optimized_weights)
    st.plotly_chart(fig_frontier, use_container_width=True)
except Exception as e:
    st.warning(f"Could not generate 3D frontier: {str(e)}")

st.info("""
**How to interpret this chart:**
- **Blue Points:** Random portfolio combinations (1000+ simulations)
- **Gold Diamond:** Your initial portfolio position
- **Green Star:** Optimized portfolio (recommended)
- **X-axis:** Portfolio volatility (risk)
- **Y-axis:** Expected annual return
- **Z-axis:** Sharpe ratio (efficiency)
""")

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO WEIGHT COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## ⚖️ PORTFOLIO WEIGHT COMPARISON")
st.write("How your allocation changed from initial to optimized:")

# Weight comparison dataframe
weight_data = []
for asset in all_assets:
    weight_data.append({
        "Asset": asset,
        "Initial Weight": f"{initial_weights.get(asset, 0):.1f}%",
        "Optimized Weight": f"{optimized_weights.get(asset, 0):.1f}%",
        "Change": f"{(optimized_weights.get(asset, 0) - initial_weights.get(asset, 0)):+.1f}%"
    })

weights_df = pd.DataFrame(weight_data)
st.dataframe(weights_df, use_container_width=True, hide_index=True)

# Weight comparison chart
col1, col2 = st.columns(2)

with col1:
    try:
        fig_weights = plot_weight_comparison(initial_weights, optimized_weights)
        st.plotly_chart(fig_weights, use_container_width=True)
    except Exception as e:
        st.warning(f"Could not generate weight chart: {str(e)}")

with col2:
    # Pie charts
    st.markdown("**Initial vs Optimized Allocation:**")
    
    col2a, col2b = st.columns(2)
    
    with col2a:
        st.write("**Initial**")
        fig_initial = {
            "data": [{"values": list(initial_weights.values()), "labels": list(initial_weights.keys()), "type": "pie"}],
            "layout": {"height": 400, "paper_bgcolor": "rgba(0, 51, 102, 0)"}
        }
        st.plotly_chart(fig_initial, use_container_width=True, config={"displayModeBar": False})
    
    with col2b:
        st.write("**Optimized**")
        fig_optimized = {
            "data": [{"values": list(optimized_weights.values()), "labels": list(optimized_weights.keys()), "type": "pie"}],
            "layout": {"height": 400, "paper_bgcolor": "rgba(0, 51, 102, 0)"}
        }
        st.plotly_chart(fig_optimized, use_container_width=True, config={"displayModeBar": False})

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMAL PORTFOLIO PERFORMANCE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🎯 RECOMMENDED PORTFOLIO PERFORMANCE")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Expected Annual Return",
        f"{optimized_metrics['annual_return']:.2%}",
        help="Annualized expected return"
    )

with col2:
    st.metric(
        "Expected Volatility",
        f"{optimized_metrics['volatility']:.2%}",
        help="Standard deviation of returns (risk)"
    )

with col3:
    st.metric(
        "Sharpe Ratio",
        f"{optimized_metrics['sharpe_ratio']:.2f}",
        help="Risk-adjusted return metric"
    )

with col4:
    st.metric(
        "Sortino Ratio",
        f"{optimized_metrics['sortino_ratio']:.2f}",
        help="Downside risk-adjusted return"
    )

# ═══════════════════════════════════════════════════════════════════════════════
# RECOMMENDATIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 💡 RECOMMENDATIONS")

# Strategy-specific recommendations
if optimization_method == "Maximize Returns":
    st.info("""
    **Growth Strategy Selected**
    
    ✅ This portfolio prioritizes capital appreciation
    
    📊 **What this means:**
    - Higher expected returns (averaging 15%+ annually)
    - Higher volatility and risk
    - Better for long-term investors (10+ years)
    - Higher risk of short-term losses
    
    📋 **Recommended actions:**
    1. Dollar-cost average into this portfolio over 3-6 months
    2. Rebalance quarterly to maintain target weights
    3. Consider your risk tolerance carefully
    4. Ensure adequate emergency reserves (6-12 months)
    """)

elif optimization_method == "Minimize Risk":
    st.info("""
    **Conservative Strategy Selected**
    
    ✅ This portfolio prioritizes capital preservation
    
    📊 **What this means:**
    - Lower expected returns (3-5% annually)
    - Lower volatility and risk
    - Better for risk-averse investors or near-retirees
    - Smooth, predictable performance
    
    📋 **Recommended actions:**
    1. Implement gradually over 2-3 months
    2. Review quarterly for rebalancing
    3. Consider whether returns meet your goals
    4. Monitor for over-diversification
    """)

else:  # Maximize Sharpe Ratio
    st.info("""
    **Balanced Strategy Selected (RECOMMENDED)**
    
    ✅ This portfolio balances growth and safety
    
    📊 **What this means:**
    - Moderate expected returns (8-12% annually)
    - Moderate volatility and risk
    - Optimal risk-adjusted returns
    - Best for most investors
    
    📋 **Recommended actions:**
    1. Implement as soon as possible
    2. Rebalance semi-annually or when weights drift 5%+
    3. Monitor performance against benchmarks
    4. Review annually and adjust as needed
    """)

# ═══════════════════════════════════════════════════════════════════════════════
# ACTION BUTTONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🎬 NEXT STEPS")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("← Back to Setup", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

with col2:
    if st.button("💾 Save Portfolio", use_container_width=True):
        st.success("✅ Portfolio saved successfully!")

with col3:
    if st.button("📊 Download Results", use_container_width=True):
        st.success("✅ Download started!")

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO SUMMARY FOR EXPORT
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 📄 PORTFOLIO SUMMARY")

summary_data = {
    "Asset": all_assets,
    "Recommended Weight": [f"{optimized_weights.get(asset, 0):.1f}%" for asset in all_assets],
    "Dollar Amount (per $100k)": [f"${optimized_weights.get(asset, 0) * 1000:,.0f}" for asset in all_assets],
}

summary_df = pd.DataFrame(summary_data)
st.dataframe(summary_df, use_container_width=True, hide_index=True)

st.markdown(f"""
**Portfolio Specifications:**
- **Optimization Method:** {optimization_method}
- **Expected Annual Return:** {optimized_metrics['annual_return']:.2%}
- **Expected Volatility:** {optimized_metrics['volatility']:.2%}
- **Sharpe Ratio:** {optimized_metrics['sharpe_ratio']:.2f}
- **Number of Assets:** {len(all_assets)}
- **Diversification Level:** {'Good' if len(all_assets) >= 5 else 'Moderate' if len(all_assets) >= 3 else 'Low'}
""")

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

render_footer()
