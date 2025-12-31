"""
Comparative Analysis Module
Compares original portfolio with optimized portfolio
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from config import COLORS

def calculate_original_portfolio_metrics(original_weights: dict, portfolio_data: dict, risk_free_rate: float) -> dict:
    """
    Calculate metrics for original equal-weight portfolio
    
    Args:
        original_weights: Dictionary with original weights and tickers
        portfolio_data: Portfolio data dictionary
        risk_free_rate: Risk-free rate
    
    Returns:
        Dictionary with original portfolio metrics
    """
    
    weights = original_weights['weights']
    annual_returns = portfolio_data['annual_returns']
    cov_matrix = portfolio_data['cov_matrix']
    daily_returns = portfolio_data['daily_returns']
    
    # Portfolio return and volatility
    port_return = np.sum(annual_returns * weights)
    port_volatility = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    
    # Sharpe ratio
    sharpe_ratio = (port_return - risk_free_rate) / port_volatility if port_volatility > 0 else 0
    
    # Sortino ratio
    downside_returns = daily_returns.copy()
    downside_returns[downside_returns > 0] = 0
    downside_vol = np.sqrt(np.mean(downside_returns ** 2)) * np.sqrt(252)
    sortino_ratio = (port_return - risk_free_rate) / downside_vol if downside_vol > 0 else 0
    
    # Maximum drawdown
    cumulative = (1 + daily_returns).cumprod()
    running_max = cumulative.expanding().max()
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = drawdown.min().min()
    
    # Calmar ratio
    calmar_ratio = port_return / abs(max_drawdown) if max_drawdown != 0 else 0
    
    return {
        'return': port_return,
        'volatility': port_volatility,
        'sharpe': sharpe_ratio,
        'sortino': sortino_ratio,
        'calmar': calmar_ratio,
        'max_drawdown': max_drawdown,
    }


def display_comparative_analysis(original_weights: dict, opt_results: dict, 
                                portfolio_data: dict, risk_free_rate: float):
    """
    Display comprehensive comparative analysis between original and optimized portfolios
    
    Args:
        original_weights: Original equal-weight portfolio
        opt_results: Optimized portfolio results
        portfolio_data: Portfolio data
        risk_free_rate: Risk-free rate
    """
    
    # Calculate original portfolio metrics
    original_metrics = calculate_original_portfolio_metrics(
        original_weights, portfolio_data, risk_free_rate
    )
    
    # Get optimized metrics
    optimized_metrics = opt_results['metrics']
    
    # Create comparison dataframe
    comparison_df = pd.DataFrame({
        'Metric': ['Annual Return (%)', 'Volatility (%)', 'Sharpe Ratio', 
                   'Sortino Ratio', 'Calmar Ratio'],
        'Original': [
            original_metrics['return'] * 100,
            original_metrics['volatility'] * 100,
            original_metrics['sharpe'],
            original_metrics['sortino'],
            original_metrics['calmar']
        ],
        'Optimized': [
            optimized_metrics['return'] * 100,
            optimized_metrics['volatility'] * 100,
            optimized_metrics['sharpe'],
            optimized_metrics['sortino'],
            optimized_metrics['calmar']
        ]
    })
    
    # Calculate improvements
    comparison_df['Change'] = comparison_df['Optimized'] - comparison_df['Original']
    comparison_df['% Change'] = (comparison_df['Change'] / comparison_df['Original'].abs()) * 100
    
    # Display side-by-side comparison
    st.markdown("### 📊 Portfolio Metrics Comparison")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Original Portfolio (Equal Weight)")
        st.metric("Annual Return", f"{original_metrics['return']*100:.2f}%")
        st.metric("Volatility", f"{original_metrics['volatility']*100:.2f}%")
        st.metric("Sharpe Ratio", f"{original_metrics['sharpe']:.3f}")
        st.metric("Sortino Ratio", f"{original_metrics['sortino']:.3f}")
    
    with col2:
        st.markdown("#### Optimized Portfolio")
        st.metric("Annual Return", f"{optimized_metrics['return']*100:.2f}%")
        st.metric("Volatility", f"{optimized_metrics['volatility']*100:.2f}%")
        st.metric("Sharpe Ratio", f"{optimized_metrics['sharpe']:.3f}")
        st.metric("Sortino Ratio", f"{optimized_metrics['sortino']:.3f}")
    
    with col3:
        st.markdown("#### Improvement")
        
        ret_improvement = optimized_metrics['return'] - original_metrics['return']
        ret_color = "green" if ret_improvement > 0 else "red"
        st.metric(
            "Return Change",
            f"{ret_improvement*100:+.2f}%",
            delta_color="normal" if ret_improvement > 0 else "inverse"
        )
        
        vol_improvement = optimized_metrics['volatility'] - original_metrics['volatility']
        vol_color = "green" if vol_improvement < 0 else "red"
        st.metric(
            "Volatility Change",
            f"{vol_improvement*100:+.2f}%",
            delta=f"{abs(vol_improvement/original_metrics['volatility']*100):.1f}%",
            delta_color="inverse" if vol_improvement < 0 else "normal"
        )
        
        sharpe_improvement = optimized_metrics['sharpe'] - original_metrics['sharpe']
        st.metric(
            "Sharpe Improvement",
            f"{sharpe_improvement:+.3f}",
            delta_color="normal" if sharpe_improvement > 0 else "inverse"
        )
    
    # Detailed comparison table
    st.markdown("### 📈 Detailed Metrics Table")
    
    display_df = comparison_df.copy()
    display_df['Original'] = display_df['Original'].apply(lambda x: f"{x:.3f}")
    display_df['Optimized'] = display_df['Optimized'].apply(lambda x: f"{x:.3f}")
    display_df['Change'] = display_df['Change'].apply(lambda x: f"{x:+.3f}")
    display_df['% Change'] = display_df['% Change'].apply(lambda x: f"{x:+.1f}%")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Risk-Return Tradeoff
    st.markdown("### 🎯 Risk-Return Tradeoff Analysis")
    
    fig = go.Figure()
    
    # Add original portfolio
    fig.add_trace(go.Scatter(
        x=[original_metrics['volatility']],
        y=[original_metrics['return']],
        mode='markers+text',
        name='Original (Equal Weight)',
        marker=dict(
            size=15,
            color=COLORS['light_blue'],
            symbol='circle',
            line=dict(color='white', width=2)
        ),
        text=['Equal Weight'],
        textposition='top center',
        hovertemplate='<b>Original Portfolio</b><br>Risk: %{x:.4f}<br>Return: %{y:.4f}<extra></extra>'
    ))
    
    # Add optimized portfolio
    fig.add_trace(go.Scatter(
        x=[optimized_metrics['volatility']],
        y=[optimized_metrics['return']],
        mode='markers+text',
        name='Optimized',
        marker=dict(
            size=15,
            color=COLORS['gold'],
            symbol='star',
            line=dict(color='white', width=2)
        ),
        text=['Optimized ★'],
        textposition='bottom center',
        hovertemplate='<b>Optimized Portfolio</b><br>Risk: %{x:.4f}<br>Return: %{y:.4f}<extra></extra>'
    ))
    
    # Add connection line
    fig.add_trace(go.Scatter(
        x=[original_metrics['volatility'], optimized_metrics['volatility']],
        y=[original_metrics['return'], optimized_metrics['return']],
        mode='lines',
        name='Improvement Path',
        line=dict(color=COLORS['gold'], width=2, dash='dash'),
        hoverinfo='skip'
    ))
    
    fig.update_layout(
        title="Original vs Optimized Portfolio Positioning",
        xaxis_title="Volatility (Risk)",
        yaxis_title="Annual Return",
        hovermode='closest',
        template='plotly_dark',
        paper_bgcolor=COLORS['dark_blue'],
        plot_bgcolor=COLORS['dark_blue'],
        font=dict(color=COLORS['text_dark']),
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Weight allocation comparison
    st.markdown("### 🔄 Weight Allocation Comparison")
    
    col1, col2 = st.columns(2)
    
    original_weights_arr = original_weights['weights']
    optimized_weights_arr = opt_results['weights']
    tickers = portfolio_data['tickers']
    
    weight_comparison_df = pd.DataFrame({
        'Asset': tickers,
        'Original (%)': original_weights_arr * 100,
        'Optimized (%)': optimized_weights_arr * 100,
    })
    
    weight_comparison_df['Change (%)'] = weight_comparison_df['Optimized (%)'] - weight_comparison_df['Original (%)']
    weight_comparison_df = weight_comparison_df.sort_values('Change (%)', key=abs, ascending=False)
    
    with col1:
        st.markdown("#### Weight Changes by Asset")
        
        # Create bar chart
        fig_weights = go.Figure()
        
        fig_weights.add_trace(go.Bar(
            x=weight_comparison_df['Asset'],
            y=weight_comparison_df['Original (%)'],
            name='Original',
            marker=dict(color=COLORS['light_blue']),
            text=weight_comparison_df['Original (%)'].apply(lambda x: f'{x:.1f}%'),
            textposition='auto',
        ))
        
        fig_weights.add_trace(go.Bar(
            x=weight_comparison_df['Asset'],
            y=weight_comparison_df['Optimized (%)'],
            name='Optimized',
            marker=dict(color=COLORS['gold']),
            text=weight_comparison_df['Optimized (%)'].apply(lambda x: f'{x:.1f}%'),
            textposition='auto',
        ))
        
        fig_weights.update_layout(
            title="Weight Allocation Comparison",
            barmode='group',
            xaxis_title="Asset",
            yaxis_title="Weight (%)",
            hovermode='x unified',
            template='plotly_dark',
            paper_bgcolor=COLORS['dark_blue'],
            plot_bgcolor=COLORS['dark_blue'],
            font=dict(color=COLORS['text_dark']),
            height=400
        )
        
        st.plotly_chart(fig_weights, use_container_width=True)
    
    with col2:
        st.markdown("#### Weight Change Analysis")
        st.dataframe(
            weight_comparison_df.style.format({
                'Original (%)': '{:.2f}',
                'Optimized (%)': '{:.2f}',
                'Change (%)': '{:.2f}'
            }),
            use_container_width=True,
            hide_index=True
        )
    
    # Key insights
    st.markdown("### 💡 Key Insights & Recommendations")
    
    # Calculate insights
    return_improvement = optimized_metrics['return'] - original_metrics['return']
    risk_reduction = original_metrics['volatility'] - optimized_metrics['volatility']
    sharpe_improvement = optimized_metrics['sharpe'] - original_metrics['sharpe']
    
    insights = []
    
    if return_improvement > 0:
        insights.append(f"✅ **Higher Returns**: Optimization improved annual returns by {return_improvement*100:.2f}% ({original_metrics['return']*100:.2f}% → {optimized_metrics['return']*100:.2f}%)")
    else:
        insights.append(f"⚠️ **Lower Returns**: Optimization prioritizes risk management over returns ({optimized_metrics['return']*100:.2f}% vs {original_metrics['return']*100:.2f}%)")
    
    if risk_reduction > 0:
        insights.append(f"✅ **Lower Risk**: Volatility reduced by {risk_reduction*100:.2f}% ({original_metrics['volatility']*100:.2f}% → {optimized_metrics['volatility']*100:.2f}%)")
    else:
        insights.append(f"⚠️ **Higher Risk**: Optimization allows higher risk for better returns ({optimized_metrics['volatility']*100:.2f}% vs {original_metrics['volatility']*100:.2f}%)")
    
    if sharpe_improvement > 0:
        insights.append(f"✅ **Better Risk-Adjusted Returns**: Sharpe ratio improved by {sharpe_improvement:.3f} ({original_metrics['sharpe']:.3f} → {optimized_metrics['sharpe']:.3f})")
        insights.append(f"💡 **Recommendation**: The optimized portfolio offers better returns per unit of risk taken and should be preferred.")
    else:
        insights.append(f"⚠️ **Trade-off Analysis**: Consider the risk-return tradeoff carefully.")
    
    # Top 3 weight changes
    top_increases = weight_comparison_df[weight_comparison_df['Change (%)'] > 0].head(3)
    top_decreases = weight_comparison_df[weight_comparison_df['Change (%)'] < 0].head(3)
    
    if len(top_increases) > 0:
        increase_str = ", ".join([f"{row['Asset']} (+{row['Change (%)']:.1f}%)" for _, row in top_increases.iterrows()])
        insights.append(f"📈 **Top Increases**: {increase_str}")
    
    if len(top_decreases) > 0:
        decrease_str = ", ".join([f"{row['Asset']} ({row['Change (%)']:.1f}%)" for _, row in top_decreases.iterrows()])
        insights.append(f"📉 **Top Decreases**: {decrease_str}")
    
    for insight in insights:
        st.info(insight)
    
    # Export options
    st.markdown("### 📥 Export Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 Copy Comparison as CSV"):
            csv = weight_comparison_df.to_csv(index=False)
            st.text_area(
                "Copy this CSV data:",
                value=csv,
                height=200,
                disabled=True
            )
    
    with col2:
        if st.button("📊 Copy Metrics Comparison"):
            csv = comparison_df.to_csv(index=False)
            st.text_area(
                "Copy this CSV data:",
                value=csv,
                height=200,
                disabled=True
            )
