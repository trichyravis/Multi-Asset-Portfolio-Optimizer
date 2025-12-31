"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
Multi-Asset Portfolio Optimizer Configuration
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

# ═══════════════════════════════════════════════════════════════════════════════
# MOUNTAIN PATH COLOR SCHEME
# ═══════════════════════════════════════════════════════════════════════════════

COLORS = {
    # Mountain Path Official Colors
    "dark_blue": "#003366",          # Primary dark blue (RGB: 0, 51, 102)
    "light_blue": "#ADD8E6",         # Light blue (RGB: 173, 216, 230)
    "gold": "#FFD700",               # Gold accent (RGB: 255, 215, 0)
    
    # Text Colors
    "text_dark": "#003366",          # Dark text
    "text_light": "#FFFFFF",         # Light text
    "text_muted": "#666666",         # Muted text
    
    # Background Colors
    "background_light": "#F5F5F5",   # Light background
    "background_white": "#FFFFFF",   # White background
    
    # Status Colors
    "success": "#2ecc71",            # Green
    "warning": "#f39c12",            # Orange
    "danger": "#e74c3c",             # Red
}

# ═══════════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY - PROFESSIONAL & ELEGANT
# ═══════════════════════════════════════════════════════════════════════════════

TYPOGRAPHY = {
    "font_main": "'Times New Roman', serif",  # Professional serif font
    "font_secondary": "Arial, sans-serif",    # Clean sans-serif
    
    # Sizes
    "h1_size": "28px",
    "h2_size": "22px",
    "h3_size": "18px",
    "body_size": "14px",
    "small_size": "12px",
    
    # Weights
    "light": "300",
    "normal": "400",
    "semibold": "600",
    "bold": "700",
}

# ═══════════════════════════════════════════════════════════════════════════════
# HEADER CONFIGURATION - MINIMAL, PROFESSIONAL
# ═══════════════════════════════════════════════════════════════════════════════

HEADER_CONFIG = {
    "height": "60px",  # Minimal height
    "background": COLORS["dark_blue"],
    "text_color": COLORS["text_light"],
    "padding": "8px 20px",
    "font_size": "16px",
    "font_weight": "bold",
    "border_bottom": f"2px solid {COLORS['gold']}",
    "shadow": "0 2px 8px rgba(0, 51, 102, 0.15)",
}

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER CONFIGURATION - MINIMAL, PROFESSIONAL
# ═══════════════════════════════════════════════════════════════════════════════

FOOTER_CONFIG = {
    "height": "50px",  # Minimal height
    "background": COLORS["dark_blue"],
    "text_color": COLORS["text_light"],
    "padding": "10px 20px",
    "font_size": "12px",
    "border_top": f"1px solid {COLORS['gold']}",
    "shadow": "0 -2px 8px rgba(0, 51, 102, 0.15)",
    
    # Author info (left side)
    "author": "Prof. V. Ravichandran",
    "subtitle": "28+ Years Corporate Finance | 10+ Years Academic Excellence",
    
    # Branding (right side)
    "brand": "🏔️ The Mountain Path - World of Finance",
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

MAIN_CONFIG = {
    "background": COLORS["background_light"],
    "padding_top": "20px",
    "padding_bottom": "20px",
    "max_width": "1400px",
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
# APP INFO
# ═══════════════════════════════════════════════════════════════════════════════

APP_INFO = {
    "name": "Multi-Asset Portfolio Optimizer",
    "tagline": "Professional Portfolio Optimization with Modern Portfolio Theory",
    "author": "Prof. V. Ravichandran",
    "experience": "28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence",
    "organization": "The Mountain Path - World of Finance",
    "version": "1.0.0",
}

# ═══════════════════════════════════════════════════════════════════════════════
# CONVENIENT ACCESS - THEME DICTIONARY
# ═══════════════════════════════════════════════════════════════════════════════

THEME = {
    "colors": COLORS,
    "typography": TYPOGRAPHY,
    "header": HEADER_CONFIG,
    "footer": FOOTER_CONFIG,
    "main": MAIN_CONFIG,
    "page": PAGE_CONFIG,
    "app": APP_INFO,
}
