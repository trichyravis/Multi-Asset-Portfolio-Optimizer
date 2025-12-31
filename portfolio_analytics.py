"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - PORTFOLIO ANALYTICS & OPTIMIZATION
═══════════════════════════════════════════════════════════════════════════════

Portfolio analytics and optimization using Modern Portfolio Theory.
Uses ANNUAL RETURNS and ANNUAL STANDARD DEVIATION for all calculations.
"""

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
from datetime import datetime, timedelta
import streamlit as st


class PortfolioAnalytics:
    """Professional portfolio analytics and optimization."""
    
    @staticmethod
    def fetch_historical_data(tickers, period_days=252):
        """
        Fetch historical price data for assets.
        
        Args:
            tickers: List of ticker symbols
            period_days: Number of days of historical data (default 252 = 1 year)
        
        Returns:
            DataFrame with daily returns
        """
        try:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=period_days)
            
            # Fetch data
            data = yf.download(tickers, start=start_date, end=end_date, progress=False)
            
            if len(tickers) == 1:
                data = data[['Adj Close']]
                data.columns = [tickers[0]]
            else:
                data = data['Adj Close']
            
            # Calculate daily returns
            returns = data.pct_change().dropna()
            
            return returns
        
        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")
            return None
    
    @staticmethod
    def calculate_annual_metrics(returns, weights, risk_free_rate=0.05):
        """
        Calculate portfolio metrics using ANNUAL returns and ANNUAL standard deviation.
        
        Args:
            returns: DataFrame of daily returns
            weights: Array of portfolio weights
            risk_free_rate: Annual risk-free rate (default 5%)
        
        Returns:
            Dictionary of metrics
        """
        # Ensure weights sum to 1
        weights = np.array(weights) / np.sum(weights)
        
        # Portfolio daily returns
        portfolio_daily_returns = (returns * weights).sum(axis=1)
        
        # ANNUAL RETURN (annualized from daily)
        annual_return = (1 + portfolio_daily_returns.mean()) ** 252 - 1
        
        # ANNUAL STANDARD DEVIATION (annualized from daily)
        annual_volatility = portfolio_daily_returns.std() * np.sqrt(252)
        
        # Sharpe Ratio (using annual metrics)
        sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility if annual_volatility > 0 else 0
        
        # Sortino Ratio (using annual metrics)
        downside_daily_returns = portfolio_daily_returns[portfolio_daily_returns < 0]
        downside_annual_volatility = downside_daily_returns.std() * np.sqrt(252)
        sortino_ratio = (annual_return - risk_free_rate) / downside_annual_volatility if downside_annual_volatility > 0 else 0
        
        # Value at Risk (95%)
        var_95_daily = np.percentile(portfolio_daily_returns, 5)
        var_95_annual = (1 + var_95_daily) ** 252 - 1
        
        # Expected Shortfall (Conditional VaR)
        tail_returns = portfolio_daily_returns[portfolio_daily_returns <= np.percentile(portfolio_daily_returns, 5)]
        expected_shortfall_daily = tail_returns.mean()
        expected_shortfall_annual = (1 + expected_shortfall_daily) ** 252 - 1 if len(tail_returns) > 0 else 0
        
        # Maximum Drawdown
        cumulative_returns = (1 + portfolio_daily_returns).cumprod()
        running_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - running_max) / running_max
        max_drawdown = drawdown.min()
        
        return {
            'annual_return': annual_return,
            'annual_volatility': annual_volatility,
            'sharpe_ratio': sharpe_ratio,
            'sortino_ratio': sortino_ratio,
            'var_95': var_95_annual,
            'expected_shortfall': expected_shortfall_annual,
            'max_drawdown': max_drawdown,
        }
    
    @staticmethod
    def optimize_portfolio(returns, weights, method='max_sharpe', risk_free_rate=0.05):
        """
        Optimize portfolio weights using Modern Portfolio Theory.
        
        Uses ANNUAL RETURNS and ANNUAL STANDARD DEVIATION.
        
        Args:
            returns: DataFrame of daily returns
            weights: Current portfolio weights (for reference)
            method: 'max_sharpe', 'max_return', or 'min_risk'
            risk_free_rate: Annual risk-free rate
        
        Returns:
            Optimized weights array
        """
        n_assets = returns.shape[1]
        
        # Annual metrics from daily data
        # ANNUAL RETURN
        annual_returns = ((1 + returns.mean()) ** 252 - 1).values
        
        # ANNUAL COVARIANCE (annualized from daily)
        daily_cov = returns.cov().values
        annual_cov = daily_cov * 252
        
        # Define objective functions
        if method == 'max_sharpe':
            def objective(w):
                # Portfolio annual return
                ret = np.sum(annual_returns * w)
                # Portfolio annual volatility
                vol = np.sqrt(np.dot(w, np.dot(annual_cov, w)))
                # Sharpe ratio (negative because we minimize)
                sharpe = (ret - risk_free_rate) / vol if vol > 0 else 0
                return -sharpe
        
        elif method == 'max_return':
            def objective(w):
                # Portfolio annual return (negative because we minimize)
                ret = np.sum(annual_returns * w)
                return -ret
        
        elif method == 'min_risk':
            def objective(w):
                # Portfolio annual volatility
                vol = np.sqrt(np.dot(w, np.dot(annual_cov, w)))
                return vol
        
        # Constraints: weights sum to 1
        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
        
        # Bounds: 0 to 1 (no short selling)
        bounds = tuple((0, 1) for _ in range(n_assets))
        
        # Initial guess (equal weights)
        x0 = np.array([1 / n_assets] * n_assets)
        
        # Optimize
        result = minimize(
            objective,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'maxiter': 1000}
        )
        
        if result.success:
            return result.x
        else:
            return x0


class PortfolioComparison:
    """Compare current vs optimized portfolio."""
    
    @staticmethod
    def compare(returns, current_weights, optimized_weights, risk_free_rate=0.05):
        """
        Compare current and optimized portfolios.
        
        Args:
            returns: DataFrame of daily returns
            current_weights: Current portfolio weights
            optimized_weights: Optimized portfolio weights
            risk_free_rate: Annual risk-free rate
        
        Returns:
            Tuple of (current_metrics, optimized_metrics)
        """
        current_metrics = PortfolioAnalytics.calculate_annual_metrics(
            returns, current_weights, risk_free_rate
        )
        
        optimized_metrics = PortfolioAnalytics.calculate_annual_metrics(
            returns, optimized_weights, risk_free_rate
        )
        
        return current_metrics, optimized_metrics
    
    @staticmethod
    def calculate_improvements(current_metrics, optimized_metrics):
        """
        Calculate improvements from optimization.
        
        Args:
            current_metrics: Current portfolio metrics
            optimized_metrics: Optimized portfolio metrics
        
        Returns:
            Dictionary of improvement metrics
        """
        return {
            'return_improvement': (optimized_metrics['annual_return'] - current_metrics['annual_return']),
            'return_improvement_pct': (
                ((optimized_metrics['annual_return'] - current_metrics['annual_return']) / 
                 abs(current_metrics['annual_return'])) * 100 if current_metrics['annual_return'] != 0 else 0
            ),
            'volatility_improvement': (current_metrics['annual_volatility'] - optimized_metrics['annual_volatility']),
            'volatility_improvement_pct': (
                ((current_metrics['annual_volatility'] - optimized_metrics['annual_volatility']) / 
                 current_metrics['annual_volatility']) * 100 if current_metrics['annual_volatility'] != 0 else 0
            ),
            'sharpe_improvement': (optimized_metrics['sharpe_ratio'] - current_metrics['sharpe_ratio']),
            'sharpe_improvement_pct': (
                ((optimized_metrics['sharpe_ratio'] - current_metrics['sharpe_ratio']) / 
                 abs(current_metrics['sharpe_ratio'])) * 100 if current_metrics['sharpe_ratio'] != 0 else 0
            ),
        }
