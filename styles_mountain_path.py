"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - STYLES
Professional CSS for Header, Footer, and Main Content
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
from config import COLORS, TYPOGRAPHY, HEADER_CONFIG, FOOTER_CONFIG, MAIN_CONFIG

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN STYLES - Apply once at app startup
# ═══════════════════════════════════════════════════════════════════════════════

def apply_main_styles():
    """Apply all custom styles to the app"""
    
    st.markdown(f"""
    <style>
    {get_header_styles()}
    {get_footer_styles()}
    {get_main_styles()}
    {get_utility_styles()}
    </style>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# HEADER STYLES
# ═══════════════════════════════════════════════════════════════════════════════

def get_header_styles():
    """CSS for header"""
    return f"""
    /* Header Container */
    .mountain-header {{
        background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%);
        color: {COLORS['text_light']};
        padding: {HEADER_CONFIG['padding']};
        height: {HEADER_CONFIG['height']};
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: {HEADER_CONFIG['border_bottom']};
        box-shadow: {HEADER_CONFIG['shadow']};
        margin: 0;
        margin-bottom: 20px;
        font-family: {TYPOGRAPHY['font_main']};
    }}

    /* Header Title */
    .header-title {{
        font-size: {HEADER_CONFIG['font_size']};
        font-weight: {HEADER_CONFIG['font_weight']};
        color: {COLORS['text_light']};
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    /* Header Subtitle/Info */
    .header-info {{
        font-size: 12px;
        color: {COLORS['light_blue']};
        margin: 0;
    }}

    /* Header Right Section */
    .header-right {{
        display: flex;
        align-items: center;
        gap: 20px;
    }}

    /* Header Method Display */
    .header-method {{
        background: rgba({int('00', 16)}, {int('33', 16)}, {int('66', 16)}, 0.3);
        border: 1px solid {COLORS['gold']};
        color: {COLORS['gold']};
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
    }}
    """


# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER STYLES
# ═══════════════════════════════════════════════════════════════════════════════

def get_footer_styles():
    """CSS for footer"""
    return f"""
    /* Footer Container */
    .mountain-footer {{
        background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%);
        color: {COLORS['text_light']};
        padding: {FOOTER_CONFIG['padding']};
        height: {FOOTER_CONFIG['height']};
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-top: {FOOTER_CONFIG['border_top']};
        box-shadow: {FOOTER_CONFIG['shadow']};
        margin-top: 30px;
        font-family: {TYPOGRAPHY['font_secondary']};
        font-size: {FOOTER_CONFIG['font_size']};
    }}

    /* Footer Left Section - Author */
    .footer-left {{
        display: flex;
        flex-direction: column;
        gap: 2px;
        flex: 1;
    }}

    .footer-author {{
        font-weight: bold;
        color: {COLORS['text_light']};
        font-size: 12px;
    }}

    .footer-subtitle {{
        color: {COLORS['light_blue']};
        font-size: 11px;
    }}

    /* Footer Right Section - Brand */
    .footer-right {{
        display: flex;
        align-items: center;
        gap: 10px;
        color: {COLORS['gold']};
        font-weight: bold;
    }}

    /* Footer Brand */
    .footer-brand {{
        color: {COLORS['text_light']};
        font-size: 12px;
        font-weight: bold;
    }}

    /* Footer Link */
    .footer-link {{
        color: {COLORS['gold']};
        text-decoration: none;
    }}

    .footer-link:hover {{
        text-decoration: underline;
    }}

    /* Divider in Footer */
    .footer-divider {{
        width: 1px;
        height: 20px;
        background: {COLORS['gold']};
        opacity: 0.3;
    }}
    """


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT STYLES
# ═══════════════════════════════════════════════════════════════════════════════

def get_main_styles():
    """CSS for main content area"""
    return f"""
    /* Main Content Background */
    .main {{
        background: {COLORS['background_light']};
    }}

    /* Streamlit Container */
    .appview-container {{
        background: {COLORS['background_light']};
    }}

    /* Section Container */
    .section-container {{
        background: {COLORS['background_white']};
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid {COLORS['dark_blue']};
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}

    /* Headings */
    h1, h2, h3 {{
        color: {COLORS['dark_blue']};
        font-family: {TYPOGRAPHY['font_main']};
    }}

    h1 {{
        font-size: {TYPOGRAPHY['h1_size']};
        font-weight: {TYPOGRAPHY['bold']};
        border-bottom: 2px solid {COLORS['gold']};
        padding-bottom: 10px;
    }}

    h2 {{
        font-size: {TYPOGRAPHY['h2_size']};
        font-weight: {TYPOGRAPHY['semibold']};
        color: {COLORS['dark_blue']};
    }}

    h3 {{
        font-size: {TYPOGRAPHY['h3_size']};
        color: {COLORS['dark_blue']};
    }}

    /* Body Text */
    body {{
        font-family: {TYPOGRAPHY['font_secondary']};
        color: {COLORS['text_dark']};
    }}

    p {{
        color: {COLORS['text_dark']};
        line-height: 1.6;
    }}

    /* Links */
    a {{
        color: {COLORS['dark_blue']};
        text-decoration: none;
        font-weight: 500;
    }}

    a:hover {{
        color: {COLORS['gold']};
        text-decoration: underline;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%);
    }}

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
        color: {COLORS['text_light']};
    }}

    /* Buttons */
    .stButton > button {{
        background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%);
        color: {COLORS['text_light']};
        border: 2px solid {COLORS['gold']};
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        transition: all 0.3s ease;
    }}

    .stButton > button:hover {{
        background: linear-gradient(135deg, {COLORS['gold']} 0%, {COLORS['gold']} 100%);
        color: {COLORS['dark_blue']};
        border-color: {COLORS['dark_blue']};
    }}

    /* Metric Cards */
    .metric-card {{
        background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%);
        color: {COLORS['text_light']};
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid {COLORS['gold']};
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.15);
        text-align: center;
    }}

    .metric-label {{
        font-size: 12px;
        color: {COLORS['light_blue']};
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }}

    .metric-value {{
        font-size: 24px;
        font-weight: bold;
        color: {COLORS['gold']};
    }}

    /* Table Styling */
    table {{
        border-collapse: collapse;
        width: 100%;
    }}

    table thead {{
        background: {COLORS['dark_blue']};
        color: {COLORS['text_light']};
    }}

    table th {{
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }}

    table td {{
        padding: 10px 12px;
        border-bottom: 1px solid {COLORS['light_blue']};
    }}

    table tbody tr:hover {{
        background: {COLORS['background_light']};
    }}
    """


# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY STYLES
# ═══════════════════════════════════════════════════════════════════════════════

def get_utility_styles():
    """CSS for utility classes"""
    return f"""
    /* Success Message */
    .success-box {{
        background: rgba(46, 204, 113, 0.1);
        border-left: 4px solid {COLORS['success']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['success']};
    }}

    /* Warning Message */
    .warning-box {{
        background: rgba(243, 156, 18, 0.1);
        border-left: 4px solid {COLORS['warning']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['warning']};
    }}

    /* Error Message */
    .error-box {{
        background: rgba(231, 76, 60, 0.1);
        border-left: 4px solid {COLORS['danger']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['danger']};
    }}

    /* Info Box */
    .info-box {{
        background: rgba(0, 51, 102, 0.05);
        border-left: 4px solid {COLORS['dark_blue']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['text_dark']};
    }}

    /* Centered Text */
    .text-center {{
        text-align: center;
    }}

    /* Gold Text */
    .text-gold {{
        color: {COLORS['gold']};
        font-weight: bold;
    }}

    /* Dark Blue Text */
    .text-dark-blue {{
        color: {COLORS['dark_blue']};
        font-weight: bold;
    }}

    /* Hidden Streamlit Elements */
    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}
    """


# ═══════════════════════════════════════════════════════════════════════════════
# RENDER HEADER FUNCTION
# ═══════════════════════════════════════════════════════════════════════════════

def render_header(title: str = "🏔️ Portfolio Optimizer", method: str = None):
    """
    Render professional header
    
    Args:
        title: Header title
        method: Optional method display (e.g., "Maximize Sharpe Ratio")
    """
    if method:
        st.markdown(f"""
        <div class="mountain-header">
            <div>
                <div class="header-title">{title}</div>
                <div class="header-info">The Mountain Path - World of Finance</div>
            </div>
            <div class="header-right">
                <div class="header-method">{method}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="mountain-header">
            <div>
                <div class="header-title">{title}</div>
                <div class="header-info">The Mountain Path - World of Finance</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# RENDER FOOTER FUNCTION
# ═══════════════════════════════════════════════════════════════════════════════

def render_footer():
    """Render professional footer with author and branding"""
    st.markdown(f"""
    <div class="mountain-footer">
        <div class="footer-left">
            <div class="footer-author">Prof. V. Ravichandran</div>
            <div class="footer-subtitle">28+ Years Corporate Finance | 10+ Years Academic Excellence</div>
        </div>
        <div class="footer-divider"></div>
        <div class="footer-right">
            <div class="footer-brand">🏔️ The Mountain Path - World of Finance</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
