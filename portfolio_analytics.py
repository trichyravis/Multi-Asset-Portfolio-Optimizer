"""
Portfolio Analytics Module
Handles visualizations, metrics display, and data analysis
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from config import COLORS, RISK_METRICS

# ============================================================================
# METRICS DISPLAY FUNCTIONS
# ============================================================================

def display_portfolio_metrics(opt_results: dict, portfolio_data: dict):
    """Display comprehensive portfolio metrics"""
    
    if not opt_results.get('success'):
        st.error("No valid optimization results")
        return
    
    weights = opt_results['weights']
    metrics = opt_results['metrics']
    annual_returns = portfolio_data['annual_returns']
    
    # Calculate individual asset metrics
    asset_metrics = pd.DataFrame({
        'Asset': portfolio_data['tickers'],
        'Weight (%)': weights * 100,
        'Annual Return (%)': annual_returns.values * 100,
        'Contribution (%)': weights * annual_returns.values * 100
    })
    
    asset_metrics = asset_metrics.sort_values('Weight (%)', ascending=False)
    
    # Display portfolio metrics
    st.markdown("### Portfolio Performance Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "📈 Annual Return",
            f"{metrics['return']*100:.2f}%",
            help="Expected annual portfolio return"
        )
    
    with col2:
        st.metric(
            "📊 Volatility",
            f"{metrics['volatility']*100:.2f}%",
            help="Portfolio standard deviation"
        )
    
    with col3:
        st.metric(
            "⚡ Sharpe Ratio",
            f"{metrics['sharpe']:.3f}",
            help="Return per unit of risk"
        )
    
    with col4:
        st.metric(
            "🎯 Sortino Ratio",
            f"{metrics['sortino']:.3f}",
            help="Return per unit of downside risk"
        )
    
    # Asset-level metrics table
    st.markdown("### Asset Composition & Contribution")
    st.dataframe(
        asset_metrics.style.format({
            'Weight (%)': '{:.2f}',
            'Annual Return (%)': '{:.2f}',
            'Contribution (%)': '{:.2f}'
        }),
        use_container_width=True,
        hide_index=True
    )


def display_weights_table(opt_results: dict, portfolio_data: dict):
    """Display detailed weights allocation table"""
    
    weights = opt_results['weights']
    tickers = portfolio_data['tickers']
    
    # Create weights dataframe
    weights_df = pd.DataFrame({
        'Ticker': tickers,
        'Weight (%)': weights * 100,
        'Allocation': weights
    })
    
    weights_df = weights_df.sort_values('Weight (%)', ascending=False)
    
    st.markdown("### Allocation Table")
    
    # Color-coded display
    def color_weight(val):
        if val > 0.2:
            color = '#00cc66'  # Green for significant allocations
        elif val > 0.05:
            color = '#FFD700'  # Gold for medium allocations
        else:
            color = '#ff6b35'  # Orange for small allocations
        
        return f'background-color: {color}; color: white; font-weight: bold;'
    
    st.dataframe(
        weights_df.style.applymap(color_weight, subset=['Weight (%)']).format({
            'Weight (%)': '{:.2f}',
            'Allocation': '{:.4f}'
        }),
        use_container_width=True,
        hide_index=True
    )


def display_risk_metrics(opt_results: dict, portfolio_data: dict):
    """Display advanced risk metrics"""
    
    metrics = opt_results['metrics']
    daily_returns = portfolio_data['daily_returns']
    weights = opt_results['weights']
    annual_returns = portfolio_data['annual_returns']
    cov_matrix = portfolio_data['cov_matrix']
    
    st.markdown("### Risk Analysis Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "📉 Calmar Ratio",
            f"{metrics.get('calmar', 0):.3f}",
            help="Return relative to maximum drawdown"
        )
        st.metric(
            "ℹ️ Information Ratio",
            f"{metrics.get('information', 0):.3f}",
            help="Excess return per unit of tracking error"
        )
    
    with col2:
        # Value at Risk (95%)
        var_95 = np.percentile(daily_returns.mean(axis=1) * weights, 5) * 252
        st.metric(
            "⚠️ VaR (95%)",
            f"{var_95*100:.2f}%",
            help="Maximum expected loss in worst 5% of scenarios"
        )
        
        # Expected Shortfall
        es_95 = np.mean(daily_returns[daily_returns < np.percentile(daily_returns, 5)].mean(axis=1) * weights) * 252
        st.metric(
            "🚨 Expected Shortfall",
            f"{es_95*100:.2f}%",
            help="Average loss in tail events"
        )
    
    # Diversification metrics
    st.markdown("### Diversification Analysis")
    
    # Herfindahl index
    herfindahl = np.sum(weights ** 2)
    effective_assets = 1 / herfindahl
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "📊 Herfindahl Index",
            f"{herfindahl:.3f}",
            help="Concentration measure (lower = more diversified)"
        )
    
    with col2:
        st.metric(
            "🔀 Effective # of Assets",
            f"{effective_assets:.2f}",
            help=f"Equivalent to {effective_assets:.0f} equally-weighted assets"
        )


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def plot_efficient_frontier(portfolio_data: dict, opt_results: dict, risk_free_rate: float):
    """Plot efficient frontier with optimal portfolio"""
    
    annual_returns = portfolio_data['annual_returns']
    cov_matrix = portfolio_data['cov_matrix']
    
    # Generate efficient frontier
    num_assets = len(annual_returns)
    frontier_returns = []
    frontier_vols = []
    
    min_ret = annual_returns.min()
    max_ret = annual_returns.max()
    target_returns = np.linspace(min_ret, max_ret, 100)
    
    from scipy.optimize import minimize
    
    for target_ret in target_returns:
        x0 = np.array([1 / num_assets] * num_assets)
        bounds = tuple((0, 1) for _ in range(num_assets))
        
        constraints = [
            {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq', 'fun': lambda w: np.sum(annual_returns * w) - target_ret}
        ]
        
        def portfolio_vol(w):
            return np.sqrt(np.dot(w, np.dot(cov_matrix, w)))
        
        result = minimize(
            portfolio_vol,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'maxiter': 1000}
        )
        
        if result.success:
            frontier_returns.append(target_ret)
            frontier_vols.append(result.fun)
    
    # Create figure
    fig = go.Figure()
    
    # Add efficient frontier
    fig.add_trace(go.Scatter(
        x=frontier_vols,
        y=frontier_returns,
        mode='lines',
        name='Efficient Frontier',
        line=dict(color=COLORS['light_blue'], width=3),
        hovertemplate='<b>Risk:</b> %{x:.4f}<br><b>Return:</b> %{y:.4f}<extra></extra>'
    ))
    
    # Add optimal portfolio
    opt_metrics = opt_results['metrics']
    fig.add_trace(go.Scatter(
        x=[opt_metrics['volatility']],
        y=[opt_metrics['return']],
        mode='markers+text',
        name='Optimal Portfolio ★',
        marker=dict(
            size=20,
            color=COLORS['gold'],
            symbol='star',
            line=dict(color='white', width=2)
        ),
        text=['★ Optimal'],
        textposition='top center',
        hovertemplate='<b>Optimal Portfolio</b><br>Risk: %{x:.4f}<br>Return: %{y:.4f}<extra></extra>'
    ))
    
    # Add individual assets
    for i, ticker in enumerate(portfolio_data['tickers']):
        fig.add_trace(go.Scatter(
            x=[np.sqrt(cov_matrix.iloc[i, i])],
            y=[annual_returns.iloc[i]],
            mode='markers+text',
            name=ticker,
            marker=dict(size=8),
            text=[ticker],
            textposition='top center',
            hovertemplate=f'<b>{ticker}</b><br>Risk: %{{x:.4f}}<br>Return: %{{y:.4f}}<extra></extra>'
        ))
    
    # Update layout
    fig.update_layout(
        title="Efficient Frontier & Portfolio Optimization",
        xaxis_title="Volatility (Risk)",
        yaxis_title="Annual Return",
        hovermode='closest',
        template='plotly_dark',
        paper_bgcolor=COLORS['dark_blue'],
        plot_bgcolor=COLORS['dark_blue'],
        font=dict(color=COLORS['text_dark']),
        height=600,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)


def plot_portfolio_weights(opt_results: dict, portfolio_data: dict):
    """Plot portfolio weights as pie chart"""
    
    weights = opt_results['weights']
    tickers = portfolio_data['tickers']
    
    # Filter out zero weights
    non_zero_mask = weights > 0.001
    filtered_weights = weights[non_zero_mask]
    filtered_tickers = [t for t, m in zip(tickers, non_zero_mask) if m]
    
    fig = go.Figure(data=[go.Pie(
        labels=filtered_tickers,
        values=filtered_weights,
        marker=dict(
            colors=[COLORS['gold'] if w > 0.2 else COLORS['light_blue'] for w in filtered_weights]
        ),
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Weight: %{value:.4f}<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title="Portfolio Allocation",
        template='plotly_dark',
        paper_bgcolor=COLORS['dark_blue'],
        font=dict(color=COLORS['text_dark']),
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)


def plot_cumulative_returns(portfolio_data: dict, opt_results: dict):
    """Plot cumulative returns"""
    
    daily_returns = portfolio_data['daily_returns']
    weights = opt_results['weights']
    
    # Calculate portfolio cumulative returns
    portfolio_returns = (daily_returns * weights).sum(axis=1)
    portfolio_cumulative = (1 + portfolio_returns).cumprod() - 1
    
    # Individual asset cumulative returns
    individual_cumulative = (1 + daily_returns).cumprod() - 1
    
    fig = go.Figure()
    
    # Add portfolio line
    fig.add_trace(go.Scatter(
        x=portfolio_cumulative.index,
        y=portfolio_cumulative.values * 100,
        name='Portfolio',
        line=dict(color=COLORS['gold'], width=3),
        mode='lines',
        hovertemplate='<b>Date:</b> %{x}<br><b>Return:</b> %{y:.2f}%<extra></extra>'
    ))
    
    # Add individual assets (lighter)
    for ticker in portfolio_data['tickers'][:5]:  # Limit to first 5 for clarity
        if ticker in individual_cumulative.columns:
            fig.add_trace(go.Scatter(
                x=individual_cumulative.index,
                y=individual_cumulative[ticker].values * 100,
                name=ticker,
                line=dict(dash='dash', width=1),
                opacity=0.5,
                mode='lines'
            ))
    
    fig.update_layout(
        title="Cumulative Returns",
        xaxis_title="Date",
        yaxis_title="Return (%)",
        hovermode='x unified',
        template='plotly_dark',
        paper_bgcolor=COLORS['dark_blue'],
        plot_bgcolor=COLORS['dark_blue'],
        font=dict(color=COLORS['text_dark']),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)


def plot_correlation_matrix(portfolio_data: dict):
    """Plot correlation matrix heatmap"""
    
    daily_returns = portfolio_data['daily_returns']
    correlation = daily_returns.corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=correlation.values,
        x=correlation.columns,
        y=correlation.index,
        colorscale='RdYlGn',
        zmid=0,
        zmin=-1,
        zmax=1,
        text=np.round(correlation.values, 2),
        texttemplate='%{text:.2f}',
        textfont={"size": 10},
        hovertemplate='%{x} vs %{y}<br>Correlation: %{z:.3f}<extra></extra>'
    ))
    
    fig.update_layout(
        title="Asset Correlation Matrix",
        template='plotly_dark',
        paper_bgcolor=COLORS['dark_blue'],
        font=dict(color=COLORS['text_dark']),
        height=600,
        width=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
