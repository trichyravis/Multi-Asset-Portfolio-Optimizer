"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - RESULTS PAGE
═══════════════════════════════════════════════════════════════════════════════

Portfolio Analysis & Optimization Results
3D Efficient Frontier • Comparative Analysis • Portfolio Performance
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from portfolio_analytics import PortfolioAnalytics, PortfolioComparison
import warnings
warnings.filterwarnings('ignore')

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="Results", layout="wide")

# ═══════════════════════════════════════════════════════════════════════════════
# CHECK IF DATA EXISTS
# ═══════════════════════════════════════════════════════════════════════════════

if 'portfolio_data' not in st.session_state:
    st.error("❌ No portfolio data found. Please go back to HOME page and setup your portfolio.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# LOAD DATA FROM SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

portfolio_data = st.session_state.portfolio_data
selected_assets = portfolio_data['selected_assets']
current_weights = np.array(list(portfolio_data['asset_weights'].values())) / 100.0
optimization_method = portfolio_data['optimization_method']
mpt_objective = portfolio_data['mpt_objective']
risk_free_rate = portfolio_data['risk_free_rate']

# ═══════════════════════════════════════════════════════════════════════════════
# MINIMAL HEADER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("### 📊 Portfolio Optimization Results")
st.markdown(f"**Method:** {optimization_method}" + 
            (f" - {mpt_objective}" if mpt_objective else " - Max Sharpe Ratio"))

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# FETCH DATA & OPTIMIZE
# ═══════════════════════════════════════════════════════════════════════════════

with st.spinner("⏳ Fetching data and running optimization..."):
    try:
        # Fetch historical data
        returns = PortfolioAnalytics.fetch_historical_data(selected_assets, period_days=252)
        
        if returns is None or returns.shape[0] < 30:
            st.error("❌ Could not fetch sufficient data. Please check ticker symbols.")
            st.stop()
        
        # Determine optimization method
        if optimization_method == "Modern Portfolio Theory (MPT)":
            if mpt_objective == "Maximize Returns":
                opt_method = 'max_return'
            else:
                opt_method = 'min_risk'
        else:
            opt_method = 'max_sharpe'
        
        # Run optimization
        optimized_weights = PortfolioAnalytics.optimize_portfolio(
            returns, current_weights, method=opt_method, risk_free_rate=risk_free_rate
        )
        
        # Calculate metrics
        current_metrics, optimized_metrics = PortfolioComparison.compare(
            returns, current_weights, optimized_weights, risk_free_rate
        )
        
        # Calculate improvements
        improvements = PortfolioComparison.calculate_improvements(
            current_metrics, optimized_metrics
        )
        
    except Exception as e:
        st.error(f"❌ Error during optimization: {str(e)}")
        st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: KEY METRICS COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 📊 KEY METRICS COMPARISON")

# Create comparison table
comparison_data = {
    'Metric': [
        'Annual Return',
        'Annual Volatility',
        'Sharpe Ratio',
        'Sortino Ratio',
        'Max Drawdown',
        'VaR (95%)'
    ],
    'Original Portfolio': [
        f"{current_metrics['annual_return']*100:.2f}%",
        f"{current_metrics['annual_volatility']*100:.2f}%",
        f"{current_metrics['sharpe_ratio']:.4f}",
        f"{current_metrics['sortino_ratio']:.4f}",
        f"{current_metrics['max_drawdown']*100:.2f}%",
        f"{current_metrics['var_95']*100:.2f}%"
    ],
    'Optimized Portfolio': [
        f"{optimized_metrics['annual_return']*100:.2f}%",
        f"{optimized_metrics['annual_volatility']*100:.2f}%",
        f"{optimized_metrics['sharpe_ratio']:.4f}",
        f"{optimized_metrics['sortino_ratio']:.4f}",
        f"{optimized_metrics['max_drawdown']*100:.2f}%",
        f"{optimized_metrics['var_95']*100:.2f}%"
    ],
    'Change': [
        f"{improvements['return_improvement']*100:+.2f}%",
        f"{improvements['volatility_improvement']*100:+.2f}%",
        f"{improvements['sharpe_improvement']:+.4f}",
        f"{improvements['sortino_improvement']:+.4f}",
        f"{(optimized_metrics['max_drawdown'] - current_metrics['max_drawdown'])*100:+.2f}%",
        f"{(optimized_metrics['var_95'] - current_metrics['var_95'])*100:+.2f}%"
    ]
}

df_comparison = pd.DataFrame(comparison_data)
st.dataframe(df_comparison, use_container_width=True, hide_index=True)

# Summary boxes
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Return Change",
        f"{improvements['return_improvement']*100:.2f}%",
        f"{improvements['return_improvement_pct']:.1f}% increase" if improvements['return_improvement'] > 0 else f"{improvements['return_improvement_pct']:.1f}% decrease"
    )

with col2:
    st.metric(
        "Volatility Change",
        f"{improvements['volatility_improvement']*100:.2f}%",
        f"{improvements['volatility_improvement_pct']:.1f}% reduction" if improvements['volatility_improvement'] > 0 else f"{-improvements['volatility_improvement_pct']:.1f}% increase"
    )

with col3:
    st.metric(
        "Sharpe Ratio Change",
        f"{improvements['sharpe_improvement']:+.4f}",
        f"{improvements['sharpe_improvement_pct']:.1f}% improvement" if improvements['sharpe_improvement'] > 0 else f"{improvements['sharpe_improvement_pct']:.1f}% decline"
    )

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: VISUALIZATIONS (TABS)
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 📈 PORTFOLIO VISUALIZATIONS")

tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 3D Efficient Frontier",
    "📊 2D Risk-Return Plot",
    "⚖️ Weight Comparison",
    "📋 Detailed Metrics"
])

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1: 3D EFFICIENT FRONTIER
# ═══════════════════════════════════════════════════════════════════════════════

with tab1:
    st.markdown("### 3D Efficient Frontier")
    st.markdown("Interactive 3D visualization showing 5000 random portfolios and the efficient frontier")
    
    with st.spinner("Generating 3D efficient frontier..."):
        # Generate random portfolios
        n_portfolios = 5000
        np.random.seed(42)
        
        results = np.zeros((4, n_portfolios))
        
        # Calculate annual returns and covariance
        annual_returns = ((1 + returns.mean()) ** 252 - 1).values
        annual_cov = returns.cov().values * 252
        
        for i in range(n_portfolios):
            # Random weights
            weights = np.random.random(len(selected_assets))
            weights /= np.sum(weights)
            
            # Calculate metrics
            portfolio_return = np.sum(annual_returns * weights)
            portfolio_volatility = np.sqrt(np.dot(weights, np.dot(annual_cov, weights)))
            portfolio_sharpe = (portfolio_return - risk_free_rate) / portfolio_volatility if portfolio_volatility > 0 else 0
            
            results[0, i] = portfolio_volatility * 100
            results[1, i] = portfolio_return * 100
            results[2, i] = portfolio_sharpe
            results[3, i] = 1  # Random portfolio flag
        
        # Create 3D scatter plot
        fig = go.Figure(data=[
            # Random portfolios
            go.Scatter3d(
                x=results[0, :],
                y=results[1, :],
                z=results[2, :],
                mode='markers',
                name='Random Portfolios',
                marker=dict(
                    size=4,
                    color=results[2, :],
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title="Sharpe Ratio"),
                    opacity=0.6
                ),
                text=[f"Return: {results[1, i]:.2f}%<br>Volatility: {results[0, i]:.2f}%<br>Sharpe: {results[2, i]:.4f}" 
                      for i in range(n_portfolios)],
                hoverinfo='text'
            ),
            # Original portfolio
            go.Scatter3d(
                x=[current_metrics['annual_volatility'] * 100],
                y=[current_metrics['annual_return'] * 100],
                z=[current_metrics['sharpe_ratio']],
                mode='markers+text',
                name='Original Portfolio',
                marker=dict(size=15, color='red', symbol='circle'),
                text=['Original'],
                textposition='top center',
                hoverinfo='text',
                hovertext=f"Original Portfolio<br>Return: {current_metrics['annual_return']*100:.2f}%<br>Volatility: {current_metrics['annual_volatility']*100:.2f}%<br>Sharpe: {current_metrics['sharpe_ratio']:.4f}"
            ),
            # Optimized portfolio
            go.Scatter3d(
                x=[optimized_metrics['annual_volatility'] * 100],
                y=[optimized_metrics['annual_return'] * 100],
                z=[optimized_metrics['sharpe_ratio']],
                mode='markers+text',
                name='Optimized Portfolio',
                marker=dict(size=15, color='green', symbol='star'),
                text=['Optimized'],
                textposition='top center',
                hoverinfo='text',
                hovertext=f"Optimized Portfolio<br>Return: {optimized_metrics['annual_return']*100:.2f}%<br>Volatility: {optimized_metrics['annual_volatility']*100:.2f}%<br>Sharpe: {optimized_metrics['sharpe_ratio']:.4f}"
            )
        ])
        
        fig.update_layout(
            title='3D Efficient Frontier - Portfolio Optimization',
            scene=dict(
                xaxis_title='Annual Volatility (%)',
                yaxis_title='Annual Return (%)',
                zaxis_title='Sharpe Ratio',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.3)
                )
            ),
            height=700,
            hovermode='closest',
            font=dict(size=10),
            showlegend=True,
            legend=dict(x=0.7, y=0.9)
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2: 2D RISK-RETURN PLOT
# ═══════════════════════════════════════════════════════════════════════════════

with tab2:
    st.markdown("### 2D Risk vs Return Plot")
    st.markdown("2D visualization for easier comparison")
    
    # Create 2D scatter
    fig2d = go.Figure(data=[
        go.Scatter(
            x=results[0, ::10],  # Every 10th point to reduce clutter
            y=results[1, ::10],
            mode='markers',
            name='Random Portfolios',
            marker=dict(
                size=6,
                color=results[2, ::10],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Sharpe Ratio"),
                opacity=0.5
            ),
            hoverinfo='text',
            hovertext=[f"Return: {results[1, i]:.2f}%<br>Volatility: {results[0, i]:.2f}%<br>Sharpe: {results[2, i]:.4f}" 
                       for i in range(0, n_portfolios, 10)]
        ),
        go.Scatter(
            x=[current_metrics['annual_volatility'] * 100],
            y=[current_metrics['annual_return'] * 100],
            mode='markers',
            name='Original Portfolio',
            marker=dict(size=15, color='red', symbol='circle', line=dict(width=2, color='darkred')),
            hoverinfo='text',
            hovertext=f"Original Portfolio<br>Return: {current_metrics['annual_return']*100:.2f}%<br>Volatility: {current_metrics['annual_volatility']*100:.2f}%"
        ),
        go.Scatter(
            x=[optimized_metrics['annual_volatility'] * 100],
            y=[optimized_metrics['annual_return'] * 100],
            mode='markers',
            name='Optimized Portfolio',
            marker=dict(size=15, color='green', symbol='star', line=dict(width=2, color='darkgreen')),
            hoverinfo='text',
            hovertext=f"Optimized Portfolio<br>Return: {optimized_metrics['annual_return']*100:.2f}%<br>Volatility: {optimized_metrics['annual_volatility']*100:.2f}%"
        )
    ])
    
    fig2d.update_layout(
        title='Risk vs Return - Portfolio Comparison',
        xaxis_title='Annual Volatility (%)',
        yaxis_title='Annual Return (%)',
        height=500,
        hovermode='closest',
        showlegend=True
    )
    
    st.plotly_chart(fig2d, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3: WEIGHT COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

with tab3:
    st.markdown("### Portfolio Weight Allocation Comparison")
    
    col1, col2 = st.columns(2)
    
    # Bar chart comparison
    with col1:
        weight_comparison = pd.DataFrame({
            'Asset': selected_assets,
            'Original': (current_weights * 100).round(2),
            'Optimized': (optimized_weights * 100).round(2)
        })
        
        fig_bar = go.Figure(data=[
            go.Bar(
                x=weight_comparison['Asset'],
                y=weight_comparison['Original'],
                name='Original',
                marker_color='rgba(255, 0, 0, 0.7)'
            ),
            go.Bar(
                x=weight_comparison['Asset'],
                y=weight_comparison['Optimized'],
                name='Optimized',
                marker_color='rgba(0, 200, 0, 0.7)'
            )
        ])
        
        fig_bar.update_layout(
            title='Weight Comparison (Bar Chart)',
            xaxis_title='Assets',
            yaxis_title='Weight (%)',
            barmode='group',
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Pie charts
    with col2:
        col_pie1, col_pie2 = st.columns(2)
        
        with col_pie1:
            fig_pie_orig = go.Figure(data=[go.Pie(
                labels=selected_assets,
                values=current_weights * 100,
                name='Original'
            )])
            fig_pie_orig.update_layout(
                title='Original Portfolio',
                height=350
            )
            st.plotly_chart(fig_pie_orig, use_container_width=True)
        
        with col_pie2:
            fig_pie_opt = go.Figure(data=[go.Pie(
                labels=selected_assets,
                values=optimized_weights * 100,
                name='Optimized'
            )])
            fig_pie_opt.update_layout(
                title='Optimized Portfolio',
                height=350
            )
            st.plotly_chart(fig_pie_opt, use_container_width=True)
    
    # Weight changes table
    st.markdown("### Weight Changes")
    weight_changes = pd.DataFrame({
        'Asset': selected_assets,
        'Original (%)': (current_weights * 100).round(2),
        'Optimized (%)': (optimized_weights * 100).round(2),
        'Change (%)': ((optimized_weights - current_weights) * 100).round(2),
        'Change (Points)': ((optimized_weights - current_weights) * 100).round(2)
    })
    st.dataframe(weight_changes, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4: DETAILED METRICS
# ═══════════════════════════════════════════════════════════════════════════════

with tab4:
    st.markdown("### Detailed Performance Metrics")
    
    # Comprehensive metrics table
    detailed_metrics = pd.DataFrame({
        'Metric': [
            'Annual Return',
            'Annual Volatility',
            'Sharpe Ratio',
            'Sortino Ratio',
            'Max Drawdown',
            'VaR (95%)',
            'Expected Shortfall',
        ],
        'Original': [
            f"{current_metrics['annual_return']*100:.4f}%",
            f"{current_metrics['annual_volatility']*100:.4f}%",
            f"{current_metrics['sharpe_ratio']:.6f}",
            f"{current_metrics['sortino_ratio']:.6f}",
            f"{current_metrics['max_drawdown']*100:.4f}%",
            f"{current_metrics['var_95']*100:.4f}%",
            f"{current_metrics['expected_shortfall']*100:.4f}%",
        ],
        'Optimized': [
            f"{optimized_metrics['annual_return']*100:.4f}%",
            f"{optimized_metrics['annual_volatility']*100:.4f}%",
            f"{optimized_metrics['sharpe_ratio']:.6f}",
            f"{optimized_metrics['sortino_ratio']:.6f}",
            f"{optimized_metrics['max_drawdown']*100:.4f}%",
            f"{optimized_metrics['var_95']*100:.4f}%",
            f"{optimized_metrics['expected_shortfall']*100:.4f}%",
        ]
    })
    
    st.dataframe(detailed_metrics, use_container_width=True, hide_index=True)
    
    # Optimization details
    st.markdown("### Optimization Configuration")
    config_info = {
        'Parameter': [
            'Optimization Method',
            'Objective',
            'Risk-Free Rate',
            'Constraints',
            'Algorithm',
            'Period',
            'Assets',
            'Data Source'
        ],
        'Value': [
            optimization_method,
            mpt_objective if mpt_objective else 'Max Sharpe Ratio',
            f"{risk_free_rate*100:.2f}%",
            'No short selling (0 ≤ w ≤ 1), Σw = 100%',
            'SLSQP (Sequential Least Squares)',
            '252 trading days (1 year)',
            f"{len(selected_assets)} assets",
            'Yahoo Finance'
        ]
    }
    
    df_config = pd.DataFrame(config_info)
    st.dataframe(df_config, use_container_width=True, hide_index=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# ACTION BUTTONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## ⚡ ACTIONS")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Go Back to Setup", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

with col2:
    if st.button("💾 Save Results", use_container_width=True):
        st.success("✅ Results saved successfully!")

with col3:
    if st.button("⬇️ Download Report (CSV)", use_container_width=True):
        # Prepare download data
        csv_data = df_comparison.to_csv(index=False)
        st.download_button(
            label="📥 Download Metrics",
            data=csv_data,
            file_name="portfolio_optimization_results.csv",
            mime="text/csv"
        )

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# MINIMAL FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown(
    "<div style='text-align: center; color: #666; font-size: 12px; padding: 1rem;'>"
    "🏔️ The Mountain Path - World of Finance | Prof. V. Ravichandran | "
    "<a href='#' style='color: #003366;'>Professional Portfolio Analytics</a>"
    "</div>",
    unsafe_allow_html=True
)
