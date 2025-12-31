
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - PROFESSIONAL STYLING
COMPREHENSIVE CSS WITH PERFECT TEXT CONTRAST
═══════════════════════════════════════════════════════════════════════════════

Perfect contrast, professional design, production-ready styling.
All text visible and readable with WCAG AAA compliance.
"""

import streamlit as st
from config_REDESIGNED import COLORS, TYPOGRAPHY

def apply_professional_styles():
    """Apply comprehensive professional styling to entire app."""
    
    custom_css = f"""
    <style>
    /* ====================================================================
       GLOBAL STYLES
       ==================================================================== */
    
    * {{
        font-family: '{TYPOGRAPHY["font_secondary"]}', sans-serif;
    }}
    
    body {{
        background-color: {COLORS['primary_dark']} !important;
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       UNIVERSAL TEXT STYLING - ALL TEXT MUST BE WHITE ON DARK
       ==================================================================== */
    
    /* All generic text elements */
    p, span, div, label, caption, a {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* All paragraph text */
    p {{
        color: {COLORS['text_white']} !important;
        font-size: {TYPOGRAPHY['body_size']};
    }}
    
    /* All spans */
    span {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* All labels */
    label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    /* ====================================================================
       HEADERS - GOLD FOR VISIBILITY
       ==================================================================== */
    
    h1, h2, h3, h4, h5, h6 {{
        color: {COLORS['accent_gold']} !important;
        font-weight: 700 !important;
        font-family: '{TYPOGRAPHY['font_primary']}', serif;
    }}
    
    h1 {{ font-size: {TYPOGRAPHY['h1_size']}; }}
    h2 {{ font-size: {TYPOGRAPHY['h2_size']}; }}
    h3 {{ font-size: {TYPOGRAPHY['h3_size']}; }}
    
    /* ====================================================================
       SIDEBAR - WHITE TEXT ON DARK BACKGROUND
       ==================================================================== */
    
    [data-testid="stSidebar"] {{
        background: linear-gradient(135deg, {COLORS['primary_dark']} 0%, {COLORS['primary_light']} 50%, {COLORS['primary_dark']} 100%) !important;
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stSidebar"] * {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stSidebar"] p {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stSidebar"] span {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stSidebar"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    /* ====================================================================
       MAIN CONTENT - WHITE TEXT ON DARK BACKGROUND
       ==================================================================== */
    
    .main {{
        color: {COLORS['text_white']} !important;
    }}
    
    .main * {{
        color: {COLORS['text_white']} !important;
    }}
    
    .main p {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       MARKDOWN CONTAINERS - WHITE TEXT
       ==================================================================== */
    
    [data-testid="stMarkdownContainer"] {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stMarkdownContainer"] * {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stMarkdownContainer"] p {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stMarkdownContainer"] span {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       SLIDERS - WHITE TEXT ON DARK BACKGROUND
       ==================================================================== */
    
    [data-testid="stSlider"] {{
        padding: 15px 10px !important;
    }}
    
    [data-testid="stSlider"] label {{
        color: {COLORS['text_white']} !important;
        font-size: {TYPOGRAPHY['body_size']} !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }}
    
    [data-testid="stSlider"] * {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stSlider"] [role="slider"] {{
        accent-color: {COLORS['accent_gold']} !important;
    }}
    
    /* Slider track */
    .stSlider > div > div > div > div {{
        background: linear-gradient(to right, {COLORS['primary_light']}, {COLORS['accent_gold']}) !important;
        height: 8px !important;
        border-radius: 4px !important;
    }}
    
    /* Slider thumb */
    .stSlider > div > div > div > div > div {{
        background-color: {COLORS['accent_gold']} !important;
        border: 2px solid {COLORS['text_white']} !important;
        height: 20px !important;
        width: 20px !important;
        border-radius: 50% !important;
        box-shadow: 0px 2px 8px rgba(255, 215, 0, 0.4) !important;
    }}
    
    /* ====================================================================
       SELECT BOXES & MULTISELECT - WHITE LABELS
       ==================================================================== */
    
    [data-testid="stSelectbox"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    [data-testid="stMultiSelect"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    /* Select box input text - DARK on LIGHT */
    [data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: {COLORS['primary_lightest']} !important;
        border: 2px solid {COLORS['accent_gold']} !important;
        border-radius: 6px !important;
    }}
    
    [data-testid="stSelectbox"] div[data-baseweb="select"] * {{
        color: {COLORS['text_dark']} !important;
    }}
    
    /* ====================================================================
       INPUT ELEMENTS - DARK TEXT ON LIGHT BACKGROUND
       ==================================================================== */
    
    [data-testid="stNumberInput"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    [data-testid="stNumberInput"] input {{
        background-color: {COLORS['primary_lightest']} !important;
        color: {COLORS['text_dark']} !important;
        border: 2px solid {COLORS['accent_gold']} !important;
        border-radius: 6px !important;
        padding: 10px !important;
        font-weight: 600 !important;
    }}
    
    [data-testid="stTextInput"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    [data-testid="stTextInput"] input {{
        background-color: {COLORS['primary_lightest']} !important;
        color: {COLORS['text_dark']} !important;
        border: 2px solid {COLORS['accent_gold']} !important;
        border-radius: 6px !important;
    }}
    
    /* ====================================================================
       RADIO BUTTONS & CHECKBOXES - WHITE TEXT
       ==================================================================== */
    
    [data-testid="stRadio"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    [data-testid="stCheckbox"] label {{
        color: {COLORS['text_white']} !important;
        font-weight: 700 !important;
    }}
    
    /* ====================================================================
       BUTTONS - PROFESSIONAL STYLING
       ==================================================================== */
    
    button {{
        background: linear-gradient(135deg, {COLORS['primary_dark']} 0%, {COLORS['primary_light']} 100%) !important;
        color: {COLORS['text_white']} !important;
        border: 2px solid {COLORS['accent_gold']} !important;
        border-radius: 6px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }}
    
    button:hover {{
        background: linear-gradient(135deg, {COLORS['primary_light']} 0%, {COLORS['primary_dark']} 100%) !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3) !important;
    }}
    
    /* ====================================================================
       METRIC CARDS & CONTAINERS
       ==================================================================== */
    
    [data-testid="metric-container"] {{
        background: linear-gradient(135deg, #003d70 0%, #005a9d 100%) !important;
        color: {COLORS['text_white']} !important;
        border: 2px solid {COLORS['accent_gold']} !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
    }}
    
    [data-testid="metric-container"] * {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       NOTIFICATIONS & ALERTS - DARK TEXT ON LIGHT
       ==================================================================== */
    
    [data-testid="stNotification"] {{
        background-color: {COLORS['primary_lightest']} !important;
        color: {COLORS['text_dark']} !important;
    }}
    
    [data-testid="stNotification"] * {{
        color: {COLORS['text_dark']} !important;
    }}
    
    .stAlert {{
        color: {COLORS['text_dark']} !important;
    }}
    
    /* ====================================================================
       TABS - WHITE TEXT HEADERS
       ==================================================================== */
    
    [data-testid="stTabs"] {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stTabs"] button {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       DATAFRAMES & TABLES
       ==================================================================== */
    
    [data-testid="stDataFrame"] {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       ELEMENT CONTAINERS
       ==================================================================== */
    
    .element-container {{
        background-color: transparent !important;
    }}
    
    .element-container p {{
        color: {COLORS['text_white']} !important;
    }}
    
    .element-container span {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       CAPTIONS & SMALL TEXT
       ==================================================================== */
    
    .caption {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       DIVIDERS
       ==================================================================== */
    
    hr {{
        border-color: rgba(255, 255, 255, 0.3) !important;
    }}
    
    /* ====================================================================
       LINKS
       ==================================================================== */
    
    a {{
        color: {COLORS['accent_gold']} !important;
        text-decoration: none;
    }}
    
    a:hover {{
        color: {COLORS['accent_light']} !important;
        text-decoration: underline;
    }}
    
    /* ====================================================================
       SECTION HEADERS
       ==================================================================== */
    
    .stSectionHeader {{
        color: {COLORS['accent_gold']} !important;
    }}
    
    /* ====================================================================
       EXPAND SECTIONS
       ==================================================================== */
    
    [data-testid="stExpander"] {{
        color: {COLORS['text_white']} !important;
    }}
    
    [data-testid="stExpander"] * {{
        color: {COLORS['text_white']} !important;
    }}
    
    /* ====================================================================
       SCROLLBARS
       ==================================================================== */
    
    ::-webkit-scrollbar {{
        width: 10px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {COLORS['primary_dark']};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {COLORS['primary_light']};
        border-radius: 5px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {COLORS['accent_gold']};
    }}
    
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)
