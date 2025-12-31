
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - PORTFOLIO ANALYTICS
Professional analytics and metrics calculation
═══════════════════════════════════════════════════════════════════════════════
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import streamlit as st


class PortfolioAnalytics:
    """Professional portfolio analytics and optimization."""
    
    @staticmethod
    def calculate_metrics(returns, weights, risk_free_rate):
        """
        Calculate portfolio metrics.
        
        Args:
            returns: DataFrame of daily returns
            weights: Array of portfolio weights
            risk_free_rate: Annual risk-free rate
            
        Returns:
            Dict of metrics
        """
        # Portfolio returns
        portfolio_returns = (returns * weights).sum(axis=1)
        
        # Annualized metrics
        annual_return = portfolio_returns.mean() * 252
        annual_volatility = portfolio_returns.std() * np.sqrt(252)
        sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility if annual_volatility > 0 else 0
        
        # Value at Risk (95%)
        var_95 = np.percentile(portfolio_returns, 5) * 252
        
        # Expected Shortfall (Conditional VaR)
        tail_returns = portfolio_returns[portfolio_returns <= np.percentile(portfolio_returns, 5)]
        expected_shortfall = tail_returns.mean() * 252 if len(tail_returns) > 0 else 0
        
        # Maximum Drawdown
        cumulative_returns = (1 + portfolio_returns).cumprod()
        running_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - running_max) / running_max
        max_drawdown = drawdown.min()
        
        # Sortino Ratio
        downside_returns = portfolio_returns[portfolio_returns < 0]
        downside_volatility = downside_returns.std() * np.sqrt(252)
        sortino_ratio = (annual_return - risk_free_rate) / downside_volatility if downside_volatility > 0 else 0
        
        # Information metrics
        correlation_matrix = returns.corr()
        avg_correlation = correlation_matrix.values[np.triu_indices_from(correlation_matrix.values, k=1)].mean()
        
        return {
            'annual_return': annual_return,
            'annual_volatility': annual_volatility,
            'sharpe_ratio': sharpe_ratio,
            'sortino_ratio': sortino_ratio,
            'var_95': var_95,
            'expected_shortfall': expected_shortfall,
            'max_drawdown': max_drawdown,
            'avg_correlation': avg_correlation,
        }
    
    @staticmethod
    def optimize_portfolio(returns, risk_free_rate, method='max_sharpe', target_return=None):
        """
        Optimize portfolio weights.
        
        Args:
            returns: DataFrame of daily returns
            risk_free_rate: Annual risk-free rate
            method: 'max_sharpe' or 'min_risk'
            target_return: Target return for min_risk method
            
        Returns:
            Optimized weights array
        """
        n_assets = returns.shape[1]
        
        # Covariance matrix (annualized)
        cov_matrix = returns.cov() * 252
        
        # Mean returns (annualized)
        mean_returns = returns.mean() * 252
        
        if method == 'max_sharpe':
            def sharpe_objective(weights):
                portfolio_return = np.sum(mean_returns * weights)
                portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
                sharpe = (portfolio_return - risk_free_rate) / portfolio_volatility if portfolio_volatility > 0 else 0
                return -sharpe
        
        elif method == 'min_risk':
            def sharpe_objective(weights):
                portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
                return portfolio_volatility
        
        # Constraints
        constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}
        
        # Bounds
        bounds = tuple((0, 1) for _ in range(n_assets))
        
        # Initial guess (equal weights)
        x0 = np.array([1 / n_assets] * n_assets)
        
        # Optimize
        result = minimize(
            sharpe_objective,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result.x if result.success else x0
    
    @staticmethod
    def display_metrics(metrics, highlight=False):
        """Display metrics in professional cards."""
        from components import MetricsDisplay
        
        metric_cards = [
            {
                "title": "Annual Return",
                "value": f"{metrics['annual_return']*100:.2f}%",
                "emoji": "📈",
                "highlight": highlight
            },
            {
                "title": "Annual Volatility",
                "value": f"{metrics['annual_volatility']*100:.2f}%",
                "emoji": "📊"
            },
            {
                "title": "Sharpe Ratio",
                "value": f"{metrics['sharpe_ratio']:.3f}",
                "emoji": "⚡",
                "highlight": highlight
            },
            {
                "title": "Sortino Ratio",
                "value": f"{metrics['sortino_ratio']:.3f}",
                "emoji": "🎯"
            },
            {
                "title": "Max Drawdown",
                "value": f"{metrics['max_drawdown']*100:.2f}%",
                "emoji": "📉"
            },
            {
                "title": "VaR (95%)",
                "value": f"{metrics['var_95']*100:.2f}%",
                "emoji": "⚠️"
            },
        ]
        
        MetricsDisplay.render_metrics_grid(metric_cards, columns=3)
