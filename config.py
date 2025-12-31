
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
PROFESSIONAL DESIGN + PORTFOLIO OPTIMIZER CONFIGURATION
═══════════════════════════════════════════════════════════════════════════════

Centralized configuration for entire application.
Colors, typography, optimization settings, and portfolio configuration.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PROFESSIONAL COLOR SCHEME
# ═══════════════════════════════════════════════════════════════════════════════

COLORS = {
    # Primary Color Scheme - MOUNTAIN PATH BRANDING
    "primary_dark": "#003366",          # Dark blue (sidebar, background)
    "primary_light": "#004d80",         # Light blue (gradient)
    "primary_lightest": "#E0F0FF",      # Very light blue
    
    # Secondary Colors
    "accent_gold": "#FFD700",           # Gold (highlights, borders)
    "accent_light": "#FFF9E6",          # Light gold (hover)
    
    # Text Colors - FIXED CONTRAST
    "text_white": "#FFFFFF",            # WHITE on dark background
    "text_dark": "#003366",             # Dark text on light backgrounds
    "text_light": "#FFFFFF",            # Light text on dark
    
    # Backgrounds
    "background_light": "#F5F5F5",      # Light background
    "background_dark": "#003366",       # Dark background
    "border_light": "#E0E0E0",          # Light borders
    
    # Status Colors
    "success": "#2ecc71",               # Green
    "warning": "#f39c12",               # Orange
    "danger": "#e74c3c",                # Red
    "info": "#3498db",                  # Blue
}

# ═══════════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY
# ═══════════════════════════════════════════════════════════════════════════════

TYPOGRAPHY = {
    "font_primary": "Times New Roman",
    "font_secondary": "Arial",
    
    # Font sizes
    "h1_size": "40px",
    "h2_size": "32px",
    "h3_size": "24px",
    "body_size": "16px",
    "small_size": "12px",
    
    # Font weights
    "light": "300",
    "normal": "400",
    "semibold": "600",
    "bold": "700",
    "extra_bold": "900",
}

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

PAGE_CONFIG = {
    "page_title": "🏔️ Multi-Asset Portfolio Optimizer",
    "page_icon": "🏔️",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# ═══════════════════════════════════════════════════════════════════════════════
# HERO HEADER CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

HERO_HEADER = {
    "background_gradient": f"linear-gradient(135deg, {COLORS['primary_dark']} 0%, {COLORS['primary_light']} 50%, {COLORS['primary_dark']} 100%)",
    "padding": "3rem 2rem",
    "border_radius": "20px",
    "border_color": COLORS["accent_gold"],
    "border_width": "3px",
    "box_shadow": "0 12px 30px rgba(0, 51, 102, 0.4)",
    
    # Text styling
    "title_color": COLORS["text_white"],
    "title_font_size": "36px",
    "title_font_weight": "900",
    "title_letter_spacing": "2px",
    
    "subtitle_color": COLORS["accent_gold"],
    "subtitle_font_size": "22px",
    "subtitle_font_weight": "600",
    
    "description_color": "#D0E8FF",
    "description_font_size": "15px",
    
    "emoji_size": "80px",
}

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

SIDEBAR_CONFIG = {
    "background_gradient": f"linear-gradient(135deg, {COLORS['primary_dark']} 0%, {COLORS['primary_light']} 50%, {COLORS['primary_dark']} 100%)",
    "text_color": COLORS["text_white"],
    "header_text_color": COLORS["accent_gold"],
    "divider_color": "rgba(255, 255, 255, 0.3)",
    "padding": "1rem",
}

# ═══════════════════════════════════════════════════════════════════════════════
# METRIC CARD CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

METRIC_CARD = {
    "background_gradient": f"linear-gradient(135deg, #003d70 0%, #005a9d 100%)",
    "text_color": COLORS["text_white"],
    "padding": "1.5rem",
    "border_radius": "15px",
    "box_shadow": "0 4px 15px rgba(0, 51, 102, 0.2)",
    "border_color": COLORS["accent_gold"],
    "border_width": "2px",
}

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

FOOTER_CONFIG = {
    "text_color": "#666",
    "background_color": "transparent",
    "padding": "2rem",
    "text_align": "center",
    "border_top": "1px solid #E0E0E0",
}

# ═══════════════════════════════════════════════════════════════════════════════
# PORTFOLIO OPTIMIZER PARAMETERS
# ═══════════════════════════════════════════════════════════════════════════════

PORTFOLIO_PARAMS = {
    # Time period
    "lookback_min": 30,
    "lookback_max": 90,
    "lookback_default": 60,
    
    # Risk-free rate
    "risk_free_rate_min": 0.0,
    "risk_free_rate_max": 0.10,
    "risk_free_rate_default": 0.06,
    
    # Optimization
    "default_method": "max_sharpe",
}

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZATION METHODS (SIMPLIFIED TO 2)
# ═══════════════════════════════════════════════════════════════════════════════

OPTIMIZATION_METHODS = {
    "max_sharpe": {
        "emoji": "⚡",
        "label": "Maximize Sharpe Ratio (RECOMMENDED)",
        "description": "Best risk-adjusted returns. Maximizes return per unit of risk.",
        "formula": "max((Return - Risk-Free) / Risk)",
        "color": COLORS["accent_gold"],
    },
    "min_risk": {
        "emoji": "🛡️",
        "label": "Minimize Risk",
        "description": "Conservative strategy. Minimum volatility for target return.",
        "formula": "min(Risk) subject to Target Return",
        "color": "#87CEEB",
    },
}

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET CLASSES & TICKERS
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_CLASSES = {
    "Asset Class 1: Indian Equities": {
        "RELIANCE.NS": "Reliance Industries",
        "TCS.NS": "Tata Consultancy Services",
        "HDFC.NS": "HDFC Bank",
        "INFY.NS": "Infosys",
        "WIPRO.NS": "Wipro",
        "LT.NS": "Larsen & Toubro",
        "MARUTI.NS": "Maruti Suzuki",
        "SBIN.NS": "State Bank of India",
    },
    "Asset Class 2: Indian Indices": {
        "^NSEI": "Nifty 50",
        "^NSEBANK": "Nifty Bank",
        "^NSMEIT": "Nifty IT",
    },
    "Asset Class 3: US Futures": {
        "^GSPC": "S&P 500",
        "^CCMP": "Nasdaq-100",
        "^DJI": "Dow Jones",
    },
    "Asset Class 4: Commodities": {
        "GC=F": "Gold",
        "CL=F": "Crude Oil",
        "SI=F": "Silver",
        "NG=F": "Natural Gas",
    },
    "Asset Class 5: Currencies": {
        "USDINR=X": "USD/INR",
        "EURINR=X": "EUR/INR",
        "GBPINR=X": "GBP/INR",
    },
    "Asset Class 6: Crypto": {
        "BTC-USD": "Bitcoin",
        "ETH-USD": "Ethereum",
        "BNB-USD": "Binance Coin",
    },
}

# ═══════════════════════════════════════════════════════════════════════════════
# SPACING & LAYOUT
# ═══════════════════════════════════════════════════════════════════════════════

SPACING = {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "xxl": "3rem",
}

# ═══════════════════════════════════════════════════════════════════════════════
# THEME DICTIONARY - EASY ACCESS
# ═══════════════════════════════════════════════════════════════════════════════

THEME = {
    "colors": COLORS,
    "typography": TYPOGRAPHY,
    "sidebar": SIDEBAR_CONFIG,
    "hero": HERO_HEADER,
    "cards": METRIC_CARD,
    "footer": FOOTER_CONFIG,
    "spacing": SPACING,
}

# ═══════════════════════════════════════════════════════════════════════════════
# APP BRANDING
# ═══════════════════════════════════════════════════════════════════════════════

APP_BRANDING = {
    "name": "🏔️ Multi-Asset Portfolio Optimizer",
    "tagline": "Powered by Modern Portfolio Theory & Risk Analytics",
    "author": "Prof. V. Ravichandran",
    "author_title": "28+ Years Corporate Finance & Banking Experience\n10+ Years Academic Excellence",
    "platform": "The Mountain Path - World of Finance",
}
