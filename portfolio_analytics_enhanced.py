
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - PORTFOLIO ANALYTICS
Advanced Portfolio Analysis with Metrics and Visualizations
═══════════════════════════════════════════════════════════════════════════════
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from config_enhanced import ASSET_STATS, RISK_FREE_RATE

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO METRICS CALCULATION
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_portfolio_metrics(assets, weights):
    """
    Calculate portfolio metrics based on selected assets and weights
    
    Args:
        assets: List of asset tickers
        weights: Dictionary with ticker: weight mappings
        
    Returns:
        Dictionary with portfolio metrics
    """
    total_weight = sum(weights.values())
    
    # Normalize weights to 100%
    normalized_weights = {asset: (weight / total_weight) * 100 for asset, weight in weights.items()}
    
    # Calculate portfolio return (weighted average of individual returns)
    portfolio_return = sum(
        normalized_weights[asset] / 100 * ASSET_STATS[asset]['return'] 
        for asset in assets if asset in ASSET_STATS
    )
    
    # Calculate portfolio volatility (simplified - assuming some correlation)
    individual_variances = [
        (normalized_weights[asset] / 100) ** 2 * (ASSET_STATS[asset]['volatility'] ** 2)
        for asset in assets if asset in ASSET_STATS
    ]
    
    # Add correlation effect (simplified)
    correlation_effect = 0.15 * sum(individual_variances)
    portfolio_variance = sum(individual_variances) + correlation_effect
    portfolio_volatility = np.sqrt(portfolio_variance)
    
    # Sharpe Ratio = (Return - Risk-Free Rate) / Volatility
    sharpe_ratio = (portfolio_return - RISK_FREE_RATE) / portfolio_volatility if portfolio_volatility > 0 else 0
    
    # Sortino Ratio (simplified - using downside volatility as 70% of total volatility)
    downside_volatility = portfolio_volatility * 0.70
    sortino_ratio = (portfolio_return - RISK_FREE_RATE) / downside_volatility if downside_volatility > 0 else 0
    
    # Max Drawdown (simplified estimate)
    max_drawdown = -portfolio_volatility * 1.5
    
    return {
        "annual_return": portfolio_return,
        "volatility": portfolio_volatility,
        "sharpe_ratio": sharpe_ratio,
        "sortino_ratio": sortino_ratio,
        "max_drawdown": max_drawdown,
        "weights": normalized_weights,
        "risk_free_rate": RISK_FREE_RATE,
    }

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZE PORTFOLIO
# ═══════════════════════════════════════════════════════════════════════════════

def optimize_portfolio(assets, initial_weights, objective="Maximize Sharpe Ratio"):
    """
    Optimize portfolio based on selected objective
    
    Args:
        assets: List of asset tickers
        initial_weights: Dictionary with ticker: weight mappings
        objective: Optimization objective
        
    Returns:
        Dictionary with optimized portfolio details
    """
    # Generate random portfolio variations
    optimized_weights = initial_weights.copy()
    
    if objective == "Maximize Returns":
        # Give more weight to high-return assets
        high_return_assets = sorted(
            [(asset, ASSET_STATS[asset]['return']) for asset in assets if asset in ASSET_STATS],
            key=lambda x: x[1],
            reverse=True
        )
        
        # Reweight toward high return assets
        new_weights = {asset: 0 for asset in assets}
        for i, (asset, _) in enumerate(high_return_assets):
            new_weights[asset] = (len(high_return_assets) - i) / len(high_return_assets) * 100
        
        total = sum(new_weights.values())
        optimized_weights = {asset: weight / total * 100 for asset, weight in new_weights.items()}
    
    elif objective == "Minimize Risk":
        # Give more weight to low-volatility assets
        low_vol_assets = sorted(
            [(asset, ASSET_STATS[asset]['volatility']) for asset in assets if asset in ASSET_STATS],
            key=lambda x: x[1]
        )
        
        new_weights = {asset: 0 for asset in assets}
        for i, (asset, _) in enumerate(low_vol_assets):
            new_weights[asset] = (len(low_vol_assets) - i) / len(low_vol_assets) * 100
        
        total = sum(new_weights.values())
        optimized_weights = {asset: weight / total * 100 for asset, weight in new_weights.items()}
    
    else:  # Maximize Sharpe Ratio (default)
        # Optimize for risk-adjusted returns
        sharpe_ratios = {}
        for asset in assets:
            if asset in ASSET_STATS:
                ret = ASSET_STATS[asset]['return']
                vol = ASSET_STATS[asset]['volatility']
                sharpe = (ret - RISK_FREE_RATE) / vol if vol > 0 else 0
                sharpe_ratios[asset] = sharpe
        
        sorted_assets = sorted(sharpe_ratios.items(), key=lambda x: x[1], reverse=True)
        new_weights = {asset: 0 for asset in assets}
        
        for i, (asset, _) in enumerate(sorted_assets):
            # Give more weight to higher Sharpe ratio assets
            new_weights[asset] = (len(sorted_assets) - i * 0.5) / len(sorted_assets)
        
        total = sum(new_weights.values())
        optimized_weights = {asset: weight / total * 100 for asset, weight in new_weights.items()}
    
    return optimized_weights

# ═══════════════════════════════════════════════════════════════════════════════
# GENERATE EFFICIENT FRONTIER
# ═══════════════════════════════════════════════════════════════════════════════

def generate_efficient_frontier(assets, num_portfolios=1000):
    """
    Generate random portfolios for efficient frontier visualization
    
    Args:
        assets: List of asset tickers
        num_portfolios: Number of random portfolios to generate
        
    Returns:
        DataFrame with portfolio returns, volatilities, and sharpe ratios
    """
    frontier_data = []
    
    for _ in range(num_portfolios):
        # Generate random weights
        weights = np.random.dirichlet(np.ones(len(assets)), 1)[0]
        weight_dict = {asset: weight * 100 for asset, weight in zip(assets, weights)}
        
        # Calculate metrics
        metrics = calculate_portfolio_metrics(assets, weight_dict)
        
        frontier_data.append({
            "Return": metrics["annual_return"],
            "Volatility": metrics["volatility"],
            "Sharpe Ratio": metrics["sharpe_ratio"],
        })
    
    return pd.DataFrame(frontier_data)

# ═══════════════════════════════════════════════════════════════════════════════
# PLOT EFFICIENT FRONTIER 3D
# ═══════════════════════════════════════════════════════════════════════════════

def plot_efficient_frontier_3d(assets, initial_weights, optimized_weights=None):
    """
    Create interactive 3D efficient frontier plot
    
    Args:
        assets: List of asset tickers
        initial_weights: Initial portfolio weights
        optimized_weights: Optimized portfolio weights
        
    Returns:
        Plotly figure
    """
    # Generate efficient frontier
    frontier = generate_efficient_frontier(assets, num_portfolios=2000)
    
    # Calculate initial portfolio metrics
    initial_metrics = calculate_portfolio_metrics(assets, initial_weights)
    
    # Create 3D scatter plot
    fig = go.Figure()
    
    # Add efficient frontier points
    fig.add_trace(go.Scatter3d(
        x=frontier["Volatility"],
        y=frontier["Return"],
        z=frontier["Sharpe Ratio"],
        mode='markers',
        marker=dict(
            size=3,
            color=frontier["Sharpe Ratio"],
            colorscale='Blues',
            showscale=True,
            colorbar=dict(title="Sharpe Ratio")
        ),
        name='Random Portfolios',
        text=[f"Return: {r:.2%}<br>Volatility: {v:.2%}<br>Sharpe: {s:.2f}" 
              for r, v, s in zip(frontier["Return"], frontier["Volatility"], frontier["Sharpe Ratio"])],
        hoverinfo='text'
    ))
    
    # Add initial portfolio
    fig.add_trace(go.Scatter3d(
        x=[initial_metrics["volatility"]],
        y=[initial_metrics["annual_return"]],
        z=[initial_metrics["sharpe_ratio"]],
        mode='markers',
        marker=dict(size=12, color='gold', symbol='square'),
        name='Initial Portfolio',
        text=f"Initial<br>Return: {initial_metrics['annual_return']:.2%}<br>Vol: {initial_metrics['volatility']:.2%}<br>Sharpe: {initial_metrics['sharpe_ratio']:.2f}",
        hoverinfo='text'
    ))
    
    # Add optimized portfolio if provided
    if optimized_weights:
        optimized_metrics = calculate_portfolio_metrics(assets, optimized_weights)
        fig.add_trace(go.Scatter3d(
            x=[optimized_metrics["volatility"]],
            y=[optimized_metrics["annual_return"]],
            z=[optimized_metrics["sharpe_ratio"]],
            mode='markers',
            marker=dict(size=12, color='lime', symbol='diamond'),
            name='Optimized Portfolio',
            text=f"Optimized<br>Return: {optimized_metrics['annual_return']:.2%}<br>Vol: {optimized_metrics['volatility']:.2%}<br>Sharpe: {optimized_metrics['sharpe_ratio']:.2f}",
            hoverinfo='text'
        ))
    
    # Update layout
    fig.update_layout(
        title="3D Efficient Frontier",
        scene=dict(
            xaxis_title="Volatility (Risk)",
            yaxis_title="Annual Return",
            zaxis_title="Sharpe Ratio",
            bgcolor="rgba(0, 51, 102, 0.1)",
        ),
        paper_bgcolor="rgba(0, 51, 102, 0)",
        plot_bgcolor="rgba(0, 51, 102, 0)",
        font=dict(color="white"),
        hovermode='closest',
        height=600
    )
    
    return fig

# ═══════════════════════════════════════════════════════════════════════════════
# PLOT WEIGHT COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

def plot_weight_comparison(initial_weights, optimized_weights=None):
    """
    Create bar chart comparing initial and optimized weights
    
    Args:
        initial_weights: Dictionary with ticker: weight mappings
        optimized_weights: Dictionary with ticker: weight mappings
        
    Returns:
        Plotly figure
    """
    data = []
    assets = list(initial_weights.keys())
    
    for asset in assets:
        data.append({
            'Asset': asset,
            'Initial Weight': initial_weights.get(asset, 0),
            'Optimized Weight': optimized_weights.get(asset, 0) if optimized_weights else 0
        })
    
    df = pd.DataFrame(data)
    
    fig = go.Figure(data=[
        go.Bar(name='Initial Weight', x=df['Asset'], y=df['Initial Weight'], marker_color='gold'),
        go.Bar(name='Optimized Weight', x=df['Asset'], y=df['Optimized Weight'], marker_color='lime') if optimized_weights else None
    ])
    
    fig.update_layout(
        title="Portfolio Weight Comparison",
        xaxis_title="Asset",
        yaxis_title="Weight (%)",
        barmode='group',
        paper_bgcolor="rgba(0, 51, 102, 0)",
        plot_bgcolor="rgba(0, 51, 102, 0.1)",
        font=dict(color="white"),
        height=500
    )
    
    return fig

# ═══════════════════════════════════════════════════════════════════════════════
# CREATE METRICS DATAFRAME
# ═══════════════════════════════════════════════════════════════════════════════

def create_metrics_comparison(initial_metrics, optimized_metrics=None):
    """
    Create comparison dataframe of metrics
    
    Args:
        initial_metrics: Dictionary with portfolio metrics
        optimized_metrics: Dictionary with portfolio metrics
        
    Returns:
        DataFrame with comparison
    """
    data = {
        'Metric': [
            'Annual Return',
            'Annual Volatility',
            'Sharpe Ratio',
            'Sortino Ratio',
            'Max Drawdown'
        ],
        'Initial Portfolio': [
            f"{initial_metrics['annual_return']:.2%}",
            f"{initial_metrics['volatility']:.2%}",
            f"{initial_metrics['sharpe_ratio']:.2f}",
            f"{initial_metrics['sortino_ratio']:.2f}",
            f"{initial_metrics['max_drawdown']:.2%}"
        ]
    }
    
    if optimized_metrics:
        improvements = []
        
        ret_imp = (optimized_metrics['annual_return'] - initial_metrics['annual_return']) / initial_metrics['annual_return'] if initial_metrics['annual_return'] != 0 else 0
        vol_imp = (optimized_metrics['volatility'] - initial_metrics['volatility']) / initial_metrics['volatility'] if initial_metrics['volatility'] != 0 else 0
        sharpe_imp = optimized_metrics['sharpe_ratio'] - initial_metrics['sharpe_ratio']
        sortino_imp = optimized_metrics['sortino_ratio'] - initial_metrics['sortino_ratio']
        dd_imp = (optimized_metrics['max_drawdown'] - initial_metrics['max_drawdown']) / initial_metrics['max_drawdown'] if initial_metrics['max_drawdown'] != 0 else 0
        
        data['Optimized Portfolio'] = [
            f"{optimized_metrics['annual_return']:.2%}",
            f"{optimized_metrics['volatility']:.2%}",
            f"{optimized_metrics['sharpe_ratio']:.2f}",
            f"{optimized_metrics['sortino_ratio']:.2f}",
            f"{optimized_metrics['max_drawdown']:.2%}"
        ]
        
        data['Change'] = [
            f"↑ {ret_imp:+.1%}" if ret_imp >= 0 else f"↓ {ret_imp:+.1%}",
            f"↓ {vol_imp:+.1%}" if vol_imp <= 0 else f"↑ {vol_imp:+.1%}",
            f"↑ {sharpe_imp:+.2f}" if sharpe_imp >= 0 else f"↓ {sharpe_imp:+.2f}",
            f"↑ {sortino_imp:+.2f}" if sortino_imp >= 0 else f"↓ {sortino_imp:+.2f}",
            f"↑ {dd_imp:+.1%}" if dd_imp >= 0 else f"↓ {dd_imp:+.1%}"
        ]
    
    return pd.DataFrame(data)
