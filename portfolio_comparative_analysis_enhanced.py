"""
═══════════════════════════════════════════════════════════════════════════════════
COMPARATIVE ANALYSIS MODULE - ENHANCED VERSION
Original (Equal-Weight) Portfolio vs Optimized Portfolio
═══════════════════════════════════════════════════════════════════════════════════

Features:
  ✓ 9 metrics compared (Return, Volatility, Sharpe, Sortino, Calmar, etc)
  ✓ Side-by-side metrics display
  ✓ Detailed comparison table
  ✓ Risk-return scatter plot
  ✓ Weight allocation bar chart
  ✓ Weight change analysis
  ✓ Automated insights & recommendations
  ✓ Export to CSV & TXT
  ✓ Professional visualizations

Status: Production Ready
═══════════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════════
# SECTION 1: ORIGINAL PORTFOLIO METRICS CALCULATION
# ═══════════════════════════════════════════════════════════════════════════════════

def calculate_original_portfolio_metrics(
    tickers: List[str],
    annual_returns: pd.Series,
    cov_matrix: pd.DataFrame,
    daily_returns: pd.DataFrame,
    risk_free_rate: float = 0.06
) -> Dict:
    """
    Calculate 9 metrics for original equal-weight portfolio
    
    Args:
        tickers: List of asset tickers
        annual_returns: Annual returns for each asset
        cov_matrix: Covariance matrix
        daily_returns: Daily returns DataFrame
        risk_free_rate: Risk-free rate (default 6%)
    
    Returns:
        Dictionary with all metrics for original portfolio
    """
    
    num_assets = len(tickers)
    
    # STEP 1: Equal weights (user's initial selection)
    original_weights = np.array([1 / num_assets] * num_assets)
    
    # STEP 2: Portfolio Return
    portfolio_return = np.sum(annual_returns.values * original_weights)
    
    # STEP 3: Portfolio Volatility
    portfolio_variance = np.dot(original_weights, np.dot(cov_matrix.values, original_weights))
    portfolio_volatility = np.sqrt(portfolio_variance)
    
    # STEP 4: Sharpe Ratio
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility if portfolio_volatility > 0 else 0
    
    # STEP 5: Sortino Ratio (downside volatility focus)
    portfolio_returns = (daily_returns.values @ original_weights) * 252
    downside_returns = portfolio_returns[portfolio_returns < 0]
    downside_volatility = np.sqrt(np.mean(downside_returns ** 2)) if len(downside_returns) > 0 else 0
    sortino_ratio = (portfolio_return - risk_free_rate) / downside_volatility if downside_volatility > 0 else 0
    
    # STEP 6: Maximum Drawdown
    cumulative_returns = (1 + (daily_returns.values @ original_weights)).reshape(-1, 1)
    cumulative_returns = np.cumprod(cumulative_returns, axis=0)
    running_max = np.maximum.accumulate(cumulative_returns, axis=0)
    drawdown = (cumulative_returns - running_max) / running_max
    max_drawdown = np.min(drawdown)
    
    # STEP 7: Calmar Ratio
    calmar_ratio = portfolio_return / abs(max_drawdown) if abs(max_drawdown) > 0 else 0
    
    # STEP 8: Information Ratio
    tracking_error = np.std(portfolio_returns - portfolio_return)
    information_ratio = portfolio_return / tracking_error if tracking_error > 0 else 0
    
    # STEP 9: Value at Risk (VaR 95%)
    var_95 = np.percentile(portfolio_returns, 5)
    
    return {
        'weights': original_weights,
        'return': portfolio_return,
        'volatility': portfolio_volatility,
        'sharpe': sharpe_ratio,
        'sortino': sortino_ratio,
        'calmar': calmar_ratio,
        'information_ratio': information_ratio,
        'max_drawdown': max_drawdown,
        'var_95': var_95,
        'daily_returns': portfolio_returns
    }


# ═══════════════════════════════════════════════════════════════════════════════════
# SECTION 2: MAIN COMPARATIVE ANALYSIS DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════════

def display_comparative_analysis(
    tickers: List[str],
    original_weights: np.ndarray,
    optimized_results: Dict,
    annual_returns: pd.Series,
    cov_matrix: pd.DataFrame,
    daily_returns: pd.DataFrame,
    risk_free_rate: float = 0.06,
    colors: Dict = None
):
    """
    Display comprehensive comparative analysis
    """
    
    # Set default colors if not provided
    if colors is None:
        colors = {
            'dark_blue': '#003366',
            'light_blue': '#004d80',
            'gold': '#FFD700',
            'green': '#28a745',
            'red': '#dc3545'
        }
    
    # STEP 1: Calculate metrics
    original_metrics = calculate_original_portfolio_metrics(
        tickers, annual_returns, cov_matrix, daily_returns, risk_free_rate
    )
    optimized_metrics = optimized_results['metrics']
    optimized_weights = optimized_results['weights']
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 1: HEADER
    # ═════════════════════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown(
        """
        <h2 style='text-align: center; color: #003366;'>
        🔄 COMPARATIVE ANALYSIS: Original vs Optimized
        </h2>
        <p style='text-align: center; color: #666;'>
        Your initial equal-weight portfolio vs algorithm's optimized recommendation
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 2: SIDE-BY-SIDE METRICS (3 COLUMNS)
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("📊 Metrics Comparison")
    
    col1, col2, col3 = st.columns(3)
    
    # Column 1: Original Portfolio
    with col1:
        st.markdown("**📍 Original Portfolio (Equal Weight)**")
        st.metric("Annual Return", f"{original_metrics['return']*100:.2f}%")
        st.metric("Volatility", f"{original_metrics['volatility']*100:.2f}%")
        st.metric("Sharpe Ratio", f"{original_metrics['sharpe']:.3f}")
        st.metric("Sortino Ratio", f"{original_metrics['sortino']:.3f}")
        st.metric("Max Drawdown", f"{original_metrics['max_drawdown']*100:.2f}%")
    
    # Column 2: Optimized Portfolio
    with col2:
        st.markdown("**⭐ Optimized Portfolio**")
        st.metric("Annual Return", f"{optimized_metrics['return']*100:.2f}%")
        st.metric("Volatility", f"{optimized_metrics['volatility']*100:.2f}%")
        st.metric("Sharpe Ratio", f"{optimized_metrics['sharpe']:.3f}")
        st.metric("Sortino Ratio", f"{optimized_metrics['sortino']:.3f}")
        st.metric("Max Drawdown", f"{optimized_metrics['max_drawdown']*100:.2f}%")
    
    # Column 3: Improvements
    with col3:
        st.markdown("**📈 Improvements**")
        
        return_change = optimized_metrics['return'] - original_metrics['return']
        return_change_pct = (return_change / original_metrics['return'] * 100) if original_metrics['return'] != 0 else 0
        
        vol_change = original_metrics['volatility'] - optimized_metrics['volatility']
        vol_change_pct = (vol_change / original_metrics['volatility'] * 100) if original_metrics['volatility'] != 0 else 0
        
        sharpe_change = optimized_metrics['sharpe'] - original_metrics['sharpe']
        
        sortino_change = optimized_metrics['sortino'] - original_metrics['sortino']
        
        dd_change = original_metrics['max_drawdown'] - optimized_metrics['max_drawdown']
        
        st.metric("Return", f"{return_change*100:+.2f}%", f"{return_change_pct:+.1f}%")
        st.metric("Volatility", f"{vol_change*100:+.2f}%", f"{vol_change_pct:+.1f}%")
        st.metric("Sharpe", f"{sharpe_change:+.3f}")
        st.metric("Sortino", f"{sortino_change:+.3f}")
        st.metric("Max DD", f"{dd_change*100:+.2f}%")
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 3: DETAILED METRICS TABLE
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("📋 Detailed Metrics Comparison")
    
    metrics_df = pd.DataFrame({
        'Metric': [
            'Annual Return',
            'Volatility',
            'Sharpe Ratio',
            'Sortino Ratio',
            'Calmar Ratio',
            'Max Drawdown',
            'Information Ratio',
            'VaR (95%)'
        ],
        'Original': [
            f"{original_metrics['return']*100:.2f}%",
            f"{original_metrics['volatility']*100:.2f}%",
            f"{original_metrics['sharpe']:.3f}",
            f"{original_metrics['sortino']:.3f}",
            f"{original_metrics['calmar']:.3f}",
            f"{original_metrics['max_drawdown']*100:.2f}%",
            f"{original_metrics['information_ratio']:.3f}",
            f"{original_metrics['var_95']*100:.2f}%"
        ],
        'Optimized': [
            f"{optimized_metrics['return']*100:.2f}%",
            f"{optimized_metrics['volatility']*100:.2f}%",
            f"{optimized_metrics['sharpe']:.3f}",
            f"{optimized_metrics['sortino']:.3f}",
            f"{optimized_metrics['calmar']:.3f}",
            f"{optimized_metrics['max_drawdown']*100:.2f}%",
            f"{optimized_metrics['information_ratio']:.3f}",
            f"{optimized_metrics['var_95']*100:.2f}%"
        ],
        'Change': [
            f"{(optimized_metrics['return'] - original_metrics['return'])*100:+.2f}%",
            f"{(original_metrics['volatility'] - optimized_metrics['volatility'])*100:+.2f}%",
            f"{(optimized_metrics['sharpe'] - original_metrics['sharpe']):+.3f}",
            f"{(optimized_metrics['sortino'] - original_metrics['sortino']):+.3f}",
            f"{(optimized_metrics['calmar'] - original_metrics['calmar']):+.3f}",
            f"{(original_metrics['max_drawdown'] - optimized_metrics['max_drawdown'])*100:+.2f}%",
            f"{(optimized_metrics['information_ratio'] - original_metrics['information_ratio']):+.3f}",
            f"{(original_metrics['var_95'] - optimized_metrics['var_95'])*100:+.2f}%"
        ]
    })
    
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 4: RISK-RETURN SCATTER PLOT
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("📊 Risk-Return Improvement Path")
    
    fig_scatter = go.Figure()
    
    # Original point
    fig_scatter.add_trace(go.Scatter(
        x=[original_metrics['volatility']],
        y=[original_metrics['return']],
        mode='markers+text',
        name='Original',
        marker=dict(size=20, color=colors['dark_blue'], symbol='circle', line=dict(color='white', width=2)),
        text=['Original'],
        textposition='top center'
    ))
    
    # Optimized point
    fig_scatter.add_trace(go.Scatter(
        x=[optimized_metrics['volatility']],
        y=[optimized_metrics['return']],
        mode='markers+text',
        name='Optimized',
        marker=dict(size=25, color=colors['gold'], symbol='star', line=dict(color='white', width=2)),
        text=['Optimized'],
        textposition='top center'
    ))
    
    # Connection line
    fig_scatter.add_trace(go.Scatter(
        x=[original_metrics['volatility'], optimized_metrics['volatility']],
        y=[original_metrics['return'], optimized_metrics['return']],
        mode='lines',
        name='Improvement Path',
        line=dict(color=colors['gold'], width=2, dash='dash'),
        hoverinfo='skip'
    ))
    
    fig_scatter.update_layout(
        title='Risk-Return Improvement',
        xaxis_title='Volatility (Risk)',
        yaxis_title='Annual Return',
        template='plotly_dark',
        height=500,
        hovermode='closest'
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 5: WEIGHT ALLOCATION BAR CHART
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("⚖️ Weight Allocation Comparison")
    
    weight_df = pd.DataFrame({
        'Asset': tickers,
        'Original': original_weights * 100,
        'Optimized': optimized_weights * 100,
        'Change': (optimized_weights - original_weights) * 100
    })
    weight_df = weight_df.sort_values('Change', ascending=False)
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=weight_df['Asset'], y=weight_df['Original'], name='Original', marker_color=colors['dark_blue']))
    fig_bar.add_trace(go.Bar(x=weight_df['Asset'], y=weight_df['Optimized'], name='Optimized', marker_color=colors['gold']))
    
    fig_bar.update_layout(
        barmode='group',
        title='Weight Allocation Comparison',
        xaxis_title='Asset',
        yaxis_title='Weight (%)',
        template='plotly_dark',
        height=400
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 6: WEIGHT CHANGE TABLE
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("📊 Weight Changes by Asset")
    
    weight_changes_df = pd.DataFrame({
        'Asset': tickers,
        'Original (%)': original_weights * 100,
        'Optimized (%)': optimized_weights * 100,
        'Change (%)': (optimized_weights - original_weights) * 100
    }).sort_values('Change (%)', ascending=False)
    
    st.dataframe(weight_changes_df.style.format(precision=2), use_container_width=True, hide_index=True)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 7: KEY INSIGHTS
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("💡 Key Insights & Recommendations")
    
    insights = generate_insights(original_metrics, optimized_metrics, weight_changes_df)
    for insight in insights:
        st.markdown(insight)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # DISPLAY 8: EXPORT OPTIONS
    # ═════════════════════════════════════════════════════════════════════════════
    st.subheader("📥 Export Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv_metrics = metrics_df.to_csv(index=False)
        st.download_button(
            "📊 Download Metrics",
            csv_metrics,
            f"metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "text/csv"
        )
    
    with col2:
        csv_weights = weight_changes_df.to_csv(index=False)
        st.download_button(
            "⚖️ Download Weights",
            csv_weights,
            f"weights_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "text/csv"
        )
    
    with col3:
        report = f"""COMPARATIVE ANALYSIS REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

METRICS COMPARISON:
{metrics_df.to_string()}

WEIGHT ANALYSIS:
{weight_changes_df.to_string()}
"""
        st.download_button(
            "📄 Download Report",
            report,
            f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            "text/plain"
        )


# ═══════════════════════════════════════════════════════════════════════════════════
# SECTION 3: HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════════

def generate_insights(original_metrics: Dict, optimized_metrics: Dict, weight_changes_df: pd.DataFrame) -> List[str]:
    """Generate key insights from comparison"""
    
    insights = []
    
    # Return analysis
    return_change = optimized_metrics['return'] - original_metrics['return']
    return_change_pct = (return_change / original_metrics['return'] * 100) if original_metrics['return'] != 0 else 0
    
    if return_change > 0.001:
        insights.append(f"✅ **Return Improvement**: +{return_change*100:.2f}% (from {original_metrics['return']*100:.2f}% to {optimized_metrics['return']*100:.2f}%)")
    elif return_change < -0.001:
        insights.append(f"⚠️ **Return Trade-off**: {return_change*100:.2f}% (optimization prioritizes risk management)")
    
    # Risk analysis
    vol_change = original_metrics['volatility'] - optimized_metrics['volatility']
    vol_change_pct = (vol_change / original_metrics['volatility'] * 100) if original_metrics['volatility'] != 0 else 0
    
    if vol_change > 0.001:
        insights.append(f"✅ **Risk Reduction**: {vol_change*100:.2f}% lower volatility ({vol_change_pct:.1f}% improvement)")
    elif vol_change < -0.001:
        insights.append(f"⚠️ **Risk Increase**: {abs(vol_change)*100:.2f}% higher volatility for better returns")
    
    # Sharpe improvement
    sharpe_change = optimized_metrics['sharpe'] - original_metrics['sharpe']
    sharpe_pct = (sharpe_change / original_metrics['sharpe'] * 100) if original_metrics['sharpe'] != 0 else 0
    
    if sharpe_change > 0.01:
        insights.append(f"✅ **Risk-Adjusted Returns**: Sharpe ratio improved {sharpe_pct:.1f}% (better return per unit risk)")
    
    # Top changes
    top_increases = weight_changes_df[weight_changes_df['Change (%)'] > 0.5].head(3)
    if len(top_increases) > 0:
        inc_str = ", ".join([f"{row['Asset']} (+{row['Change (%)']:.1f}%)" for _, row in top_increases.iterrows()])
        insights.append(f"📈 **Top Increases**: {inc_str}")
    
    top_decreases = weight_changes_df[weight_changes_df['Change (%)'] < -0.5].head(3)
    if len(top_decreases) > 0:
        dec_str = ", ".join([f"{row['Asset']} ({row['Change (%)']:.1f}%)" for _, row in top_decreases.iterrows()])
        insights.append(f"📉 **Top Decreases**: {dec_str}")
    
    # Recommendation
    if optimized_metrics['return'] > original_metrics['return'] and optimized_metrics['volatility'] < original_metrics['volatility']:
        insights.append("🎯 **Recommendation**: Exceptional improvement - higher return with lower risk. HIGHLY RECOMMENDED.")
    elif sharpe_change > original_metrics['sharpe'] * 0.1:
        insights.append("🎯 **Recommendation**: Significant improvement in risk-adjusted returns. Recommended.")
    elif vol_change > 0:
        insights.append("🎯 **Recommendation**: Risk-focused optimization. Suitable for conservative investors.")
    else:
        insights.append("⚠️ **Trade-off**: Review trade-offs between return and risk based on your objectives.")
    
    return insights


# ═══════════════════════════════════════════════════════════════════════════════════
# END OF ENHANCED MODULE
# ═══════════════════════════════════════════════════════════════════════════════════
