
"""
Configuration Module for Multi-Asset Portfolio Optimization App
Defines asset classes, colors, parameters, and styling constants
"""

# ============================================================================
# ASSET CLASSES & DEFINITIONS
# ============================================================================

ASSET_CLASSES = {
    "🇮🇳 Indian Equities": {
        "RELIANCE.NS": "Reliance Industries",
        "TCS.NS": "Tata Consultancy Services",
        "HDFC.NS": "HDFC Bank",
        "INFY.NS": "Infosys",
        "WIPRO.NS": "Wipro",
        "LT.NS": "Larsen & Toubro",
        "MARUTI.NS": "Maruti Suzuki",
        "SBIN.NS": "State Bank of India",
    },
    "📈 Indian Indices": {
        "^NSEI": "Nifty 50 Index",
        "^NSEBANK": "Nifty Bank Index",
        "^CNXIT": "Nifty IT Index",
    },
    "🇺🇸 US Indices Futures": {
        "ES=F": "E-mini S&P 500",
        "NQ=F": "E-mini Nasdaq-100",
        "YM=F": "E-mini Dow Jones",
    },
    "🏆 Commodities Futures": {
        "GC=F": "Gold Futures",
        "CL=F": "Crude Oil Futures",
        "SI=F": "Silver Futures",
        "NG=F": "Natural Gas Futures",
    },
    "💱 Currency Futures": {
        "USDINR=X": "USD/INR Exchange Rate",
        "EURINR=X": "EUR/INR Exchange Rate",
        "GBPINR=X": "GBP/INR Exchange Rate",
    },
    "₿ Cryptocurrencies": {
        "BTC-USD": "Bitcoin",
        "ETH-USD": "Ethereum",
        "BNB-USD": "Binance Coin",
    }
}

# ============================================================================
# COLOR SCHEME - MOUNTAIN PATH BRANDING
# ============================================================================

COLORS = {
    "dark_blue": "#003366",      # RGB(0, 51, 102)
    "light_blue": "#004d80",     # Lighter blue for accents
    "gold": "#FFD700",           # Gold accent color
    "light_gray": "#f0f2f6",     # Light background
    "text_dark": "#ffffff",      # White text on dark
    "text_light": "#000000",     # Dark text on light
    "success": "#00cc66",        # Green for positive
    "warning": "#ff6b35",        # Orange for warnings
    "error": "#cc0000",          # Red for errors
    "border": "#ffffff",         # White borders
}

# ============================================================================
# TYPOGRAPHY & FONTS
# ============================================================================

FONTS = {
    "family": "sans-serif",
    "title": 28,
    "header": 22,
    "subheader": 18,
    "body": 14,
    "small": 12,
    "monospace": "courier new",
}

# ============================================================================
# OPTIMIZATION METHODS
# ============================================================================

OPTIMIZATION_METHODS = {
    "max_sharpe": {
        "emoji": "⚡",
        "label": "Maximize Sharpe Ratio (RECOMMENDED)",
        "description": "Balanced strategy - best risk-adjusted returns. Maximizes return per unit of risk.",
        "formula": "max((w^T × μ - Rf) / √(w^T × Σ × w))",
    },
    "min_risk": {
        "emoji": "🛡️",
        "label": "Minimize Risk",
        "description": "Conservative strategy - minimize portfolio volatility while maintaining target return.",
        "formula": "min(√(w^T × Σ × w))",
    },
}

# ============================================================================
# RISK METRICS DEFINITIONS
# ============================================================================

RISK_METRICS = {
    "return": {
        "label": "Annual Return",
        "emoji": "📈",
        "formula": "Sum of (weight × asset_return)",
        "interpretation": "Expected annual portfolio return (%)",
    },
    "volatility": {
        "label": "Volatility (Std Dev)",
        "emoji": "📊",
        "formula": "√(w^T × Σ × w) × √252",
        "interpretation": "Portfolio risk measured as annualized standard deviation (%)",
    },
    "sharpe": {
        "label": "Sharpe Ratio",
        "emoji": "⚡",
        "formula": "(Portfolio Return - Risk-Free Rate) / Volatility",
        "interpretation": "Return per unit of risk taken (higher is better, >1 is excellent)",
    },
    "sortino": {
        "label": "Sortino Ratio",
        "emoji": "🎯",
        "formula": "(Portfolio Return - Risk-Free Rate) / Downside Deviation",
        "interpretation": "Return per unit of downside risk (ignores upside volatility)",
    },
    "calmar": {
        "label": "Calmar Ratio",
        "emoji": "📉",
        "formula": "Annual Return / Maximum Drawdown",
        "interpretation": "Return relative to largest loss (>1 is good)",
    },
    "information": {
        "label": "Information Ratio",
        "emoji": "ℹ️",
        "formula": "(Portfolio Return - Benchmark Return) / Tracking Error",
        "interpretation": "Excess return per unit of tracking error vs benchmark",
    },
    "max_drawdown": {
        "label": "Maximum Drawdown",
        "emoji": "📉",
        "formula": "(Peak Value - Trough Value) / Peak Value",
        "interpretation": "Largest peak-to-trough decline (%)",
    },
    "var": {
        "label": "Value at Risk (95%)",
        "emoji": "⚠️",
        "formula": "5th percentile of returns distribution",
        "interpretation": "Maximum expected loss in worst 5% of scenarios (%)",
    }
}

# ============================================================================
# PORTFOLIO PARAMETERS
# ============================================================================

PORTFOLIO_PARAMS = {
    "lookback_min": 30,           # Minimum 30 days
    "lookback_max": 90,           # Maximum 90 days (3 months for futures)
    "lookback_default": 90,       # Default 90 days
    "risk_free_rate_min": 0.0,    # Minimum risk-free rate
    "risk_free_rate_max": 0.10,   # Maximum 10%
    "risk_free_rate_default": 0.06,  # Default 6% (India RBI rate approx)
    "num_frontier_points": 100,   # Points on efficient frontier
    "weight_min": 0.0,            # Minimum weight per asset
    "weight_max": 1.0,            # Maximum weight per asset
}

# ============================================================================
# STREAMLIT CONFIGURATION
# ============================================================================

APP_CONFIG = {
    "page_title": "🏔️ Multi-Asset Portfolio Optimizer",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# ============================================================================
# STYLE CONSTANTS
# ============================================================================

STYLE_CONSTANTS = {
    "border_radius": "10px",
    "box_shadow": "0px 2px 10px rgba(0,0,0,0.1)",
    "padding": "20px",
    "margin": "10px",
    "transition": "all 0.3s ease",
}

# ============================================================================
# BENCHMARK SELECTION
# ============================================================================

BENCHMARKS = {
    "^NSEI": {
        "name": "Nifty 50",
        "description": "Default for Indian equity portfolios",
        "ticker": "^NSEI",
    },
    "^GSPC": {
        "name": "S&P 500",
        "description": "Default for US equity portfolios",
        "ticker": "^GSPC",
    },
}

# ============================================================================
# CURRENCY SYMBOLS & FORMATTING
# ============================================================================

CURRENCY_FORMATS = {
    "INR": "₹",
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
}

# ============================================================================
# TIME PERIODS FOR ANALYSIS
# ============================================================================

TIME_PERIODS = {
    "1M": {"days": 30, "label": "1 Month"},
    "2M": {"days": 60, "label": "2 Months"},
    "3M": {"days": 90, "label": "3 Months (Recommended)"},
}

# ============================================================================
# DEFAULT PORTFOLIO ALLOCATION (for demo)
# ============================================================================

DEFAULT_ALLOCATION = {
    "allocation_method": "equal_weight",  # equal_weight, risk_parity, custom
    "description": "Automatic equal-weight allocation across selected assets",
}

# ============================================================================
# VaR CONFIDENCE LEVELS
# ============================================================================

VAR_CONFIDENCE_LEVELS = [0.95, 0.99]  # 95% and 99% confidence intervals

# ============================================================================
# MONTE CARLO SIMULATION PARAMETERS (Optional)
# ============================================================================

MONTE_CARLO_PARAMS = {
    "num_simulations": 10000,
    "confidence_levels": [0.95, 0.99],
}

# ============================================================================
# EXPORT FORMATS
# ============================================================================

EXPORT_FORMATS = {
    "csv": "CSV (.csv)",
    "json": "JSON (.json)",
    "excel": "Excel (.xlsx)",
}
