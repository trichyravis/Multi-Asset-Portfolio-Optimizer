
"""
Multi-Asset Portfolio Optimization Streamlit Application
Main app file with data fetching, optimization, and portfolio calculations
"""

import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from scipy.optimize import minimize
import warnings

from config import ASSET_CLASSES, OPTIMIZATION_METHODS, PORTFOLIO_PARAMS, APP_CONFIG
from styles import apply_custom_styles, get_metric_color
import portfolio_analytics as analytics
import portfolio_comparative_analysis as comparative

warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title=APP_CONFIG['page_title'],
    page_icon=APP_CONFIG['page_icon'],
    layout=APP_CONFIG['layout'],
    initial_sidebar_state=APP_CONFIG['initial_sidebar_state']
)

# Apply custom styling
apply_custom_styles()

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'portfolio_data' not in st.session_state:
    st.session_state.portfolio_data = None
if 'optimization_results' not in st.session_state:
    st.session_state.optimization_results = None
if 'original_weights' not in st.session_state:
    st.session_state.original_weights = None

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

@st.cache_data(ttl=3600)
def fetch_asset_data(tickers: list, days: int) -> pd.DataFrame:
    """
    Fetch historical price data from Yahoo Finance
    
    Args:
        tickers: List of ticker symbols
        days: Number of days of historical data
    
    Returns:
        DataFrame with closing prices
    """
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)
        
        # Handle single ticker case
        if isinstance(data.columns, pd.MultiIndex):
            # Try 'Adj Close' first, fallback to 'Close'
            if 'Adj Close' in data.columns.get_level_values(0):
                data = data['Adj Close']
            elif 'Close' in data.columns.get_level_values(0):
                data = data['Close']
            else:
                st.error("Error: No price data found in Yahoo Finance response")
                return None
        else:
            # For single ticker, try Adj Close first, then Close
            if 'Adj Close' in data.columns:
                data = data[['Adj Close']]
            elif 'Close' in data.columns:
                data = data[['Close']]
            else:
                st.error("Error: No price data found in Yahoo Finance response")
                return None
        
        # Remove any NaN values
        data = data.dropna()
        
        return data
    
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}, closing prices will work in yahoo finance")
        return None


def calculate_portfolio_returns(prices: pd.DataFrame) -> pd.Series:
    """
    Calculate daily returns from price data
    
    Args:
        prices: DataFrame of asset prices
    
    Returns:
        Series of daily returns
    """
    return prices.pct_change().dropna()


def calculate_portfolio_metrics(weights: np.ndarray, 
                               annual_returns: pd.Series,
                               cov_matrix: pd.DataFrame,
                               risk_free_rate: float) -> dict:
    """
    Calculate comprehensive portfolio metrics
    
    Args:
        weights: Portfolio weights
        annual_returns: Annual returns of assets
        cov_matrix: Covariance matrix
        risk_free_rate: Risk-free rate
    
    Returns:
        Dictionary with all portfolio metrics
    """
    
    # Portfolio return and volatility
    port_return = np.sum(annual_returns * weights)
    port_volatility = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    
    # Sharpe ratio
    sharpe_ratio = (port_return - risk_free_rate) / port_volatility if port_volatility > 0 else 0
    
    # Sortino ratio
    daily_returns = annual_returns / 252
    downside_returns = daily_returns.copy()
    downside_returns[downside_returns > 0] = 0
    downside_vol = np.sqrt(np.mean(downside_returns ** 2)) * np.sqrt(252)
    sortino_ratio = (port_return - risk_free_rate) / downside_vol if downside_vol > 0 else 0
    
    # Calmar ratio
    max_drawdown = 0.05  # Placeholder
    calmar_ratio = port_return / max_drawdown if max_drawdown > 0 else 0
    
    # Information ratio
    benchmark_return = annual_returns.mean() * 0.95
    information_ratio = (port_return - benchmark_return) / (port_volatility * 0.2) if port_volatility > 0 else 0
    
    return {
        'return': port_return,
        'volatility': port_volatility,
        'sharpe': sharpe_ratio,
        'sortino': sortino_ratio,
        'calmar': calmar_ratio,
        'information': information_ratio,
    }


def optimize_portfolio(annual_returns: pd.Series,
                      cov_matrix: pd.DataFrame,
                      risk_free_rate: float,
                      method: str = 'max_sharpe') -> dict:
    """
    Optimize portfolio weights using specified method
    
    Args:
        annual_returns: Annual returns of assets
        cov_matrix: Covariance matrix
        risk_free_rate: Risk-free rate
        method: Optimization method
    
    Returns:
        Dictionary with optimized weights and metrics
    """
    
    num_assets = len(annual_returns)
    
    # Initial weights
    x0 = np.array([1 / num_assets] * num_assets)
    
    # Bounds for weights
    bounds = tuple((0, 1) for _ in range(num_assets))
    
    # Constraint: weights sum to 1
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    
    # Define objective functions
    def portfolio_return(w):
        return -np.sum(annual_returns * w)  # Negative for minimization
    
    def portfolio_vol(w):
        return np.sqrt(np.dot(w, np.dot(cov_matrix, w)))
    
    def negative_sharpe(w):
        ret = np.sum(annual_returns * w)
        vol = np.sqrt(np.dot(w, np.dot(cov_matrix, w)))
        return -(ret - risk_free_rate) / vol if vol > 0 else 0
    
    # Select objective function
    if method == 'max_returns':
        objective = portfolio_return
    elif method == 'min_risk':
        objective = portfolio_vol
    else:  # max_sharpe
        objective = negative_sharpe
    
    # Optimize
    result = minimize(
        objective,
        x0,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'maxiter': 1000, 'ftol': 1e-9}
    )
    
    if result.success:
        opt_weights = result.x
        metrics = calculate_portfolio_metrics(
            opt_weights, annual_returns, cov_matrix, risk_free_rate
        )
        
        return {
            'weights': opt_weights,
            'metrics': metrics,
            'success': True,
            'method': method
        }
    else:
        return {'success': False, 'error': 'Optimization failed'}


def calculate_efficient_frontier(annual_returns: pd.Series,
                                cov_matrix: pd.DataFrame,
                                risk_free_rate: float,
                                num_points: int = 100) -> tuple:
    """
    Calculate efficient frontier
    
    Args:
        annual_returns: Annual returns of assets
        cov_matrix: Covariance matrix
        risk_free_rate: Risk-free rate
        num_points: Number of points on frontier
    
    Returns:
        Tuple of (frontier_returns, frontier_vols, frontier_weights)
    """
    
    num_assets = len(annual_returns)
    frontier_returns = []
    frontier_vols = []
    frontier_weights = []
    
    # Target returns from minimum to maximum
    min_ret = annual_returns.min()
    max_ret = annual_returns.max()
    target_returns = np.linspace(min_ret, max_ret, num_points)
    
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
            frontier_weights.append(result.x)
    
    return (
        np.array(frontier_returns),
        np.array(frontier_vols),
        np.array(frontier_weights)
    )


# ============================================================================
# MAIN APP LAYOUT
# ============================================================================

def main():
    # Header
    st.markdown("""
    <div style="text-align: center; padding: 20px; border-bottom: 3px solid #FFD700;">
        <h1>🏔️ Multi-Asset Portfolio Optimizer</h1>
        <p style="color: #FFD700; font-size: 16px;">Powered by Modern Portfolio Theory & Risk Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar - Input Controls
    with st.sidebar:
        st.markdown("### ⚙️ Portfolio Setup")
        
        # Step 1: Time Period
        st.markdown("**Step 1: Select Time Period**")
        lookback_days = st.slider(
            "Lookback Period (days):",
            min_value=PORTFOLIO_PARAMS['lookback_min'],
            max_value=PORTFOLIO_PARAMS['lookback_max'],
            value=PORTFOLIO_PARAMS['lookback_default'],
            step=5,
            help="30-90 days recommended (max 90 days for futures expiry)"
        )
        
        # Step 2: Asset Classes
        st.markdown("**Step 2: Select Asset Classes**")
        selected_classes = st.multiselect(
            "Choose asset classes:",
            options=list(ASSET_CLASSES.keys()),
            default=list(ASSET_CLASSES.keys())[:2],
            help="Select at least one asset class"
        )
        
        if not selected_classes:
            st.error("Please select at least one asset class")
            return
        
        # Step 3: Asset Selection
        st.markdown("**Step 3: Select Assets**")
        selected_tickers = {}
        all_tickers = []
        
        for asset_class in selected_classes:
            available_tickers = list(ASSET_CLASSES[asset_class].keys())
            selected = st.multiselect(
                f"Choose from {asset_class.split()[1]}:",
                options=available_tickers,
                default=available_tickers[:2],
                key=f"select_{asset_class}"
            )
            
            if selected:
                selected_tickers[asset_class] = selected
                all_tickers.extend(selected)
        
        if not all_tickers:
            st.error("Please select at least one asset")
            return
        
        # Step 4: Weight Allocation (NEW!)
        st.markdown("**Step 4: Allocate Portfolio Weights**")
        st.caption(f"Total Assets: {len(all_tickers)} | Default: Equal Weights ({100/len(all_tickers):.1f}% each)")
        
        # Initialize weights in session state if not present
        if 'portfolio_weights' not in st.session_state:
            st.session_state.portfolio_weights = {ticker: 100/len(all_tickers) for ticker in all_tickers}
        
        # Create two columns: one for sliders, one for display
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Weight sliders for each asset
            weight_dict = {}
            st.write("**Manual Weight Allocation:**")
            for ticker in all_tickers:
                weight = st.slider(
                    f"Weight - {ticker}:",
                    min_value=0.0,
                    max_value=100.0,
                    value=st.session_state.portfolio_weights.get(ticker, 100/len(all_tickers)),
                    step=0.1,
                    key=f"weight_{ticker}",
                    help=f"Allocation % for {ticker}"
                )
                weight_dict[ticker] = weight
        
        with col2:
            st.write("**Summary:**")
            total_weight = sum(weight_dict.values())
            st.metric("Total Weight", f"{total_weight:.1f}%")
            
            if abs(total_weight - 100.0) > 0.01:
                st.warning(f"⚠️ Sum: {total_weight:.1f}%\nNeed: 100%")
            else:
                st.success(f"✅ Sum: {total_weight:.1f}%")
        
        # Reset to equal weights button
        if st.button("🔄 Reset to Equal Weights"):
            st.session_state.portfolio_weights = {ticker: 100/len(all_tickers) for ticker in all_tickers}
            st.rerun()
        
        # Validate weights sum to 100%
        total_weight = sum(weight_dict.values())
        if abs(total_weight - 100.0) > 0.01:
            st.error(f"❌ Portfolio weights must sum to 100%. Current sum: {total_weight:.1f}%")
            st.stop()
        
        # Store weights as numpy array in correct order
        portfolio_weights = np.array([weight_dict[ticker] for ticker in all_tickers]) / 100.0
        
        # Step 5: Risk-Free Rate
        st.markdown("**Step 5: Risk-Free Rate**")
        risk_free_rate = st.slider(
            "Annual Risk-Free Rate (%):",
            min_value=PORTFOLIO_PARAMS['risk_free_rate_min'] * 100,
            max_value=PORTFOLIO_PARAMS['risk_free_rate_max'] * 100,
            value=PORTFOLIO_PARAMS['risk_free_rate_default'] * 100,
            step=0.1,
            help="Current India RBI rate: ~6%"
        ) / 100
        
        # Step 6: Optimization Method
        st.markdown("**Step 6: Optimization Method**")
        opt_method = st.radio(
            "Select optimization target:",
            options=list(OPTIMIZATION_METHODS.keys()),
            format_func=lambda x: f"{OPTIMIZATION_METHODS[x]['emoji']} {OPTIMIZATION_METHODS[x]['label']}"
        )
        st.info(OPTIMIZATION_METHODS[opt_method]['description'])
        
        # Fetch and Optimize Button
        st.markdown("---")
        if st.button("🚀 Fetch Data & Optimize", use_container_width=True):
            with st.spinner("Fetching data and optimizing portfolio..."):
                # Fetch data
                price_data = fetch_asset_data(all_tickers, lookback_days)
                
                if price_data is not None and len(price_data) > 1:
                    # Calculate returns
                    daily_returns = calculate_portfolio_returns(price_data)
                    annual_returns = daily_returns.mean() * 252
                    cov_matrix = daily_returns.cov() * 252
                    
                    # Optimize
                    opt_result = optimize_portfolio(
                        annual_returns, cov_matrix, risk_free_rate, opt_method
                    )
                    
                    if opt_result.get('success'):
                        st.session_state.portfolio_data = {
                            'price_data': price_data,
                            'daily_returns': daily_returns,
                            'annual_returns': annual_returns,
                            'cov_matrix': cov_matrix,
                            'tickers': all_tickers,
                            'asset_classes': selected_classes,
                        }
                        st.session_state.optimization_results = opt_result
                        st.session_state.original_weights = {
                            'weights': portfolio_weights,  # Store user's manual weights
                            'tickers': all_tickers
                        }
                        st.session_state.risk_free_rate = risk_free_rate
                        st.success("✅ Portfolio optimized successfully!")
                    else:
                        st.error(f"Optimization failed: {opt_result.get('error')}")
                else:
                    st.error("Could not fetch data. Please check ticker symbols and try again.")
    
    # Main Content Area
    if st.session_state.portfolio_data is None:
        st.info("""
        👋 Welcome to the Multi-Asset Portfolio Optimizer!
        
        **Step-by-Step Workflow:**
        1. 📅 Select time period (30-90 days)
        2. 📊 Choose asset classes (Equities, Indices, Commodities, etc.)
        3. 🎯 Pick specific assets from each class
        4. ⚖️ Allocate portfolio weights (equal weights by default)
        5. 📍 Set risk-free rate (default: 6%)
        6. ⚡ Choose optimization method:
           - Maximize Sharpe Ratio (RECOMMENDED) - Best risk-adjusted returns
           - Minimize Risk - Conservative approach
        7. 🚀 Click "Fetch Data & Optimize"
        
        **Key Features:**
        ✅ Manual weight allocation with sliders
        ✅ Default equal weights for all assets
        ✅ Real-time weight validation
        ✅ 2 robust optimization methods
        ✅ Comprehensive risk metrics
        ✅ Visual comparisons and analysis
        
        **Supported Assets:**
        - 🇮🇳 Indian Equities: RELIANCE, TCS, HDFC, INFY, WIPRO, LT, MARUTI, SBIN
        - 📈 Indian Indices: Nifty 50, Nifty Bank, Nifty IT
        - 🇺🇸 US Futures: S&P 500, Nasdaq-100, Dow Jones
        - 🏆 Commodities: Gold, Oil, Silver, Gas
        - 💱 Currencies: USD/INR, EUR/INR, GBP/INR
        - ₿ Crypto: Bitcoin, Ethereum, Binance Coin
        """)
    else:
        # Display Results in Tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Metrics",
            "⭐ Efficient Frontier",
            "🎯 Portfolio Weights",
            "📈 Performance",
            "🔍 Risk Analysis"
        ])
        
        with tab1:
            analytics.display_portfolio_metrics(
                st.session_state.optimization_results,
                st.session_state.portfolio_data
            )
        
        with tab2:
            analytics.plot_efficient_frontier(
                st.session_state.portfolio_data,
                st.session_state.optimization_results,
                st.session_state.risk_free_rate
            )
        
        with tab3:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                analytics.plot_portfolio_weights(
                    st.session_state.optimization_results,
                    st.session_state.portfolio_data
                )
            
            with col2:
                analytics.display_weights_table(
                    st.session_state.optimization_results,
                    st.session_state.portfolio_data
                )
        
        with tab4:
            analytics.plot_cumulative_returns(
                st.session_state.portfolio_data,
                st.session_state.optimization_results
            )
        
        with tab5:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                analytics.plot_correlation_matrix(
                    st.session_state.portfolio_data
                )
            
            with col2:
                analytics.display_risk_metrics(
                    st.session_state.optimization_results,
                    st.session_state.portfolio_data
                )
        
        # Comparative Analysis Section
        st.markdown("---")
        st.markdown("### 🔄 Comparative Analysis: Original vs Optimized")
        
        comparative.display_comparative_analysis(
            st.session_state.original_weights,
            st.session_state.optimization_results,
            st.session_state.portfolio_data,
            st.session_state.risk_free_rate
        )


if __name__ == "__main__":
    main()
