
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
Multi-Asset Portfolio Optimizer - Enhanced Configuration
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

# ═══════════════════════════════════════════════════════════════════════════════
# MOUNTAIN PATH COLOR SCHEME - DARK BLUE THEME
# ═══════════════════════════════════════════════════════════════════════════════

COLORS = {
    "dark_blue": "#003366",          # Primary dark blue
    "light_blue": "#ADD8E6",         # Light blue (secondary)
    "gold": "#FFD700",               # Gold accent
    "text_dark": "#003366",          # Dark text
    "text_light": "#FFFFFF",         # White text
    "text_muted": "#CCCCCC",         # Muted text
    "background_light": "#F5F5F5",   # Light background
    "background_white": "#FFFFFF",   # White background
    "success": "#2ecc71",            # Green
    "warning": "#f39c12",            # Orange
    "danger": "#e74c3c",             # Red
}

# ═══════════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY
# ═══════════════════════════════════════════════════════════════════════════════

TYPOGRAPHY = {
    "font_main": "'Times New Roman', serif",
    "font_secondary": "Arial, sans-serif",
    "h1_size": "28px",
    "h2_size": "22px",
    "h3_size": "18px",
    "body_size": "14px",
    "small_size": "12px",
}

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

PAGE_CONFIG = {
    "page_title": "🏔️ Portfolio Optimizer - The Mountain Path",
    "page_icon": "🏔️",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET CLASSES WITH FULL NAMES AND DESCRIPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_CLASSES = {
    "Equities": {
        "emoji": "📈",
        "description": "Individual stocks - Direct ownership in companies",
        "risk": "High",
        "return": "8-28%",
        "assets": {
            "AAPL": {"name": "Apple Inc.", "sector": "Technology"},
            "MSFT": {"name": "Microsoft Corporation", "sector": "Technology"},
            "GOOGL": {"name": "Alphabet Inc. (Google)", "sector": "Technology"},
            "AMZN": {"name": "Amazon.com Inc.", "sector": "Consumer Discretionary"},
            "TSLA": {"name": "Tesla Inc.", "sector": "Automotive"},
            "META": {"name": "Meta Platforms (Facebook)", "sector": "Technology"},
            "NVDA": {"name": "NVIDIA Corporation", "sector": "Semiconductors"},
            "JPM": {"name": "JPMorgan Chase & Co.", "sector": "Financials"},
            "V": {"name": "Visa Inc.", "sector": "Financials"},
            "WMT": {"name": "Walmart Inc.", "sector": "Retail"},
        }
    },
    "Indices": {
        "emoji": "📊",
        "description": "Market indices - Diversified baskets of stocks",
        "risk": "Medium",
        "return": "8-15%",
        "assets": {
            "SPY": {"name": "S&P 500 ETF", "description": "Tracks top 500 US companies"},
            "QQQ": {"name": "Nasdaq-100 ETF", "description": "Tracks 100 largest non-financial stocks"},
            "IWM": {"name": "Russell 2000 ETF", "description": "Tracks 2000 small-cap US companies"},
            "EFA": {"name": "MSCI EAFE ETF", "description": "International developed markets"},
            "VTI": {"name": "Total US Market ETF", "description": "Entire US stock market"},
        }
    },
    "Bonds": {
        "emoji": "💰",
        "description": "Fixed income securities - Lower risk, steady returns",
        "risk": "Low",
        "return": "3-5%",
        "assets": {
            "BND": {"name": "Vanguard Total Bond ETF", "description": "Total US bond market"},
            "AGG": {"name": "iShares Core US Aggregate Bond ETF", "description": "US investment-grade bonds"},
            "SHV": {"name": "iShares 1-3 Year Treasury ETF", "description": "Short-term US Treasury bonds"},
            "TLT": {"name": "iShares 20+ Year Treasury ETF", "description": "Long-term US Treasury bonds"},
            "LQD": {"name": "iShares Investment Grade Corporate Bond ETF", "description": "Corporate bonds"},
        }
    },
    "Commodities": {
        "emoji": "🏆",
        "description": "Raw materials - Inflation hedge and diversification",
        "risk": "Medium-High",
        "return": "2-8%",
        "assets": {
            "GLD": {"name": "SPDR Gold Shares", "description": "Physical gold"},
            "SLV": {"name": "iShares Silver Trust", "description": "Physical silver"},
            "USO": {"name": "United States Oil ETF", "description": "Crude oil"},
            "DBC": {"name": "Commodities ETF", "description": "Diversified commodity basket"},
            "PDBC": {"name": "Invesco Commodity ETF", "description": "Broad commodity index"},
        }
    },
    "Cryptocurrencies": {
        "emoji": "₿",
        "description": "Digital assets - High growth, high volatility",
        "risk": "Very High",
        "return": "30-60%",
        "assets": {
            "BTC": {"name": "Bitcoin", "description": "Largest cryptocurrency by market cap"},
            "ETH": {"name": "Ethereum", "description": "Second largest cryptocurrency, smart contracts"},
        }
    },
}

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET STATISTICS (Annualized returns, volatility, correlation)
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_STATS = {
    # Equities
    "AAPL": {"return": 0.28, "volatility": 0.32, "description": "Apple Inc.", "emoji": "📈", "class": "Equities"},
    "MSFT": {"return": 0.25, "volatility": 0.28, "description": "Microsoft", "emoji": "📈", "class": "Equities"},
    "GOOGL": {"return": 0.20, "volatility": 0.26, "description": "Alphabet/Google", "emoji": "📈", "class": "Equities"},
    "AMZN": {"return": 0.22, "volatility": 0.30, "description": "Amazon", "emoji": "📈", "class": "Equities"},
    "TSLA": {"return": 0.35, "volatility": 0.45, "description": "Tesla", "emoji": "📈", "class": "Equities"},
    "META": {"return": 0.18, "volatility": 0.35, "description": "Meta/Facebook", "emoji": "📈", "class": "Equities"},
    "NVDA": {"return": 0.32, "volatility": 0.38, "description": "NVIDIA", "emoji": "📈", "class": "Equities"},
    "JPM": {"return": 0.12, "volatility": 0.22, "description": "JPMorgan Chase", "emoji": "📈", "class": "Equities"},
    "V": {"return": 0.16, "volatility": 0.20, "description": "Visa", "emoji": "📈", "class": "Equities"},
    "WMT": {"return": 0.10, "volatility": 0.18, "description": "Walmart", "emoji": "📈", "class": "Equities"},
    
    # Indices
    "SPY": {"return": 0.12, "volatility": 0.18, "description": "S&P 500", "emoji": "📊", "class": "Indices"},
    "QQQ": {"return": 0.15, "volatility": 0.22, "description": "Nasdaq-100", "emoji": "📊", "class": "Indices"},
    "IWM": {"return": 0.11, "volatility": 0.20, "description": "Russell 2000", "emoji": "📊", "class": "Indices"},
    "EFA": {"return": 0.08, "volatility": 0.18, "description": "International", "emoji": "📊", "class": "Indices"},
    "VTI": {"return": 0.11, "volatility": 0.17, "description": "Total Market", "emoji": "📊", "class": "Indices"},
    
    # Bonds
    "BND": {"return": 0.04, "volatility": 0.05, "description": "Total Bonds", "emoji": "💰", "class": "Bonds"},
    "AGG": {"return": 0.04, "volatility": 0.05, "description": "Aggregate Bonds", "emoji": "💰", "class": "Bonds"},
    "SHV": {"return": 0.03, "volatility": 0.02, "description": "Short Treasury", "emoji": "💰", "class": "Bonds"},
    "TLT": {"return": 0.05, "volatility": 0.08, "description": "Long Treasury", "emoji": "💰", "class": "Bonds"},
    "LQD": {"return": 0.05, "volatility": 0.06, "description": "Corp Bonds", "emoji": "💰", "class": "Bonds"},
    
    # Commodities
    "GLD": {"return": 0.06, "volatility": 0.15, "description": "Gold", "emoji": "🏆", "class": "Commodities"},
    "SLV": {"return": 0.08, "volatility": 0.22, "description": "Silver", "emoji": "🏆", "class": "Commodities"},
    "USO": {"return": 0.02, "volatility": 0.25, "description": "Oil", "emoji": "🏆", "class": "Commodities"},
    "DBC": {"return": 0.03, "volatility": 0.18, "description": "Commodities", "emoji": "🏆", "class": "Commodities"},
    "PDBC": {"return": 0.04, "volatility": 0.17, "description": "Commodity Index", "emoji": "🏆", "class": "Commodities"},
    
    # Cryptocurrencies
    "BTC": {"return": 0.60, "volatility": 0.75, "description": "Bitcoin", "emoji": "₿", "class": "Cryptocurrencies"},
    "ETH": {"return": 0.55, "volatility": 0.80, "description": "Ethereum", "emoji": "₿", "class": "Cryptocurrencies"},
}

# ═══════════════════════════════════════════════════════════════════════════════
# RISK-FREE RATE
# ═══════════════════════════════════════════════════════════════════════════════

RISK_FREE_RATE = 0.045  # 4.5% (Current US Treasury rate)

# ═══════════════════════════════════════════════════════════════════════════════
# THEME DICTIONARY
# ═══════════════════════════════════════════════════════════════════════════════

THEME = {
    "colors": COLORS,
    "typography": TYPOGRAPHY,
    "page": PAGE_CONFIG,
}
