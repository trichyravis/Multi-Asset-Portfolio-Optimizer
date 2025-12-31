"""
Styling Module for Multi-Asset Portfolio Optimization App
Provides comprehensive CSS styling with high-contrast inputs
"""

import streamlit as st
from config import COLORS, FONTS

def apply_custom_styles():
    """
    Apply custom CSS styling to the Streamlit app
    Ensures high-contrast inputs, professional appearance, and Mountain Path branding
    """
    
    custom_css = f"""
    <style>
    /* ====================================================================
       ROOT & GENERAL STYLING
       ==================================================================== */
    
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    html, body {{
        background-color: {COLORS['dark_blue']} !important;
        color: {COLORS['text_dark']} !important;
        font-family: {FONTS['family']} !important;
    }}
    
    /* Main app background */
    .main {{
        background-color: {COLORS['dark_blue']} !important;
        padding: 20px !important;
    }}
    
    /* ====================================================================
       SIDEBAR STYLING
       ==================================================================== */
    
    .sidebar .sidebar-content {{
        background-color: {COLORS['dark_blue']} !important;
        color: {COLORS['text_dark']} !important;
    }}
    
    [data-testid="stSidebar"] {{
        background-color: {COLORS['dark_blue']} !important;
        border-right: 2px solid {COLORS['gold']} !important;
    }}
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {{
        border-left: 0 !important;
    }}
    
    /* ====================================================================
       HEADER STYLING
       ==================================================================== */
    
    h1, h2, h3, h4, h5, h6 {{
        color: {COLORS['gold']} !important;
        font-weight: 700 !important;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
    }}
    
    h1 {{
        font-size: {FONTS['title']}px !important;
        border-bottom: 3px solid {COLORS['gold']} !important;
        padding-bottom: 10px !important;
    }}
    
    h2 {{
        font-size: {FONTS['header']}px !important;
        color: {COLORS['gold']} !important;
    }}
    
    h3 {{
        font-size: {FONTS['subheader']}px !important;
        color: {COLORS['light_blue']} !important;
    }}
    
    /* ====================================================================
       TEXT STYLING
       ==================================================================== */
    
    p, span, div {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
    }}
    
    .element-container {{
        background-color: transparent !important;
    }}
    
    /* ====================================================================
       BUTTON STYLING (HIGH CONTRAST)
       ==================================================================== */
    
    button {{
        background-color: {COLORS['gold']} !important;
        color: {COLORS['dark_blue']} !important;
        border: 2px solid {COLORS['gold']} !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
    }}
    
    button:hover {{
        background-color: {COLORS['light_blue']} !important;
        border-color: {COLORS['gold']} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 4px 12px rgba(255, 215, 0, 0.3) !important;
    }}
    
    button:active {{
        transform: translateY(0) !important;
    }}
    
    /* ====================================================================
       INPUT ELEMENTS - HIGH CONTRAST
       ==================================================================== */
    
    /* Radio Buttons - HIGH CONTRAST */
    [data-testid="stRadio"] label {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        margin: 10px 0 !important;
        padding: 10px !important;
        border-radius: 6px !important;
        transition: all 0.2s ease !important;
    }}
    
    [data-testid="stRadio"] input[type="radio"] {{
        width: 20px !important;
        height: 20px !important;
        cursor: pointer !important;
        accent-color: {COLORS['gold']} !important;
        margin-right: 10px !important;
    }}
    
    [data-testid="stRadio"] label:hover {{
        background-color: rgba(255, 215, 0, 0.1) !important;
        border-left: 4px solid {COLORS['gold']} !important;
        padding-left: 16px !important;
    }}
    
    /* Checkboxes - HIGH CONTRAST */
    [data-testid="stCheckbox"] label {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        margin: 8px 0 !important;
        padding: 8px !important;
        border-radius: 6px !important;
    }}
    
    [data-testid="stCheckbox"] input[type="checkbox"] {{
        width: 20px !important;
        height: 20px !important;
        cursor: pointer !important;
        accent-color: {COLORS['gold']} !important;
        margin-right: 10px !important;
    }}
    
    [data-testid="stCheckbox"] label:hover {{
        background-color: rgba(255, 215, 0, 0.1) !important;
    }}
    
    /* Sliders - HIGH CONTRAST */
    [data-testid="stSlider"] {{
        padding: 15px 10px !important;
    }}
    
    [data-testid="stSlider"] label {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
    }}
    
    [data-testid="stSlider"] [role="slider"] {{
        accent-color: {COLORS['gold']} !important;
    }}
    
    /* Track styling */
    .stSlider > div > div > div > div {{
        background: linear-gradient(to right, {COLORS['light_blue']}, {COLORS['gold']}) !important;
        height: 8px !important;
        border-radius: 4px !important;
    }}
    
    /* Slider thumb */
    .stSlider > div > div > div > div > div {{
        background-color: {COLORS['gold']} !important;
        border: 2px solid {COLORS['text_dark']} !important;
        height: 20px !important;
        width: 20px !important;
        border-radius: 50% !important;
        box-shadow: 0px 2px 8px rgba(255, 215, 0, 0.4) !important;
    }}
    
    /* Select Boxes / Dropdowns - HIGH CONTRAST */
    [data-testid="stSelectbox"] label {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }}
    
    [data-testid="stSelectbox"] {{
        padding: 10px 0 !important;
    }}
    
    [data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: {COLORS['light_blue']} !important;
        border: 2px solid {COLORS['gold']} !important;
        border-radius: 6px !important;
    }}
    
    [data-testid="stSelectbox"] div[data-baseweb="select"] * {{
        color: {COLORS['text_light']} !important;
    }}
    
    /* Multiselect */
    [data-testid="stMultiSelect"] label {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }}
    
    [data-testid="stMultiSelect"] {{
        padding: 10px 0 !important;
    }}
    
    /* Number Input - HIGH CONTRAST */
    [data-testid="stNumberInput"] label {{
        color: {COLORS['text_dark']} !important;
        font-size: {FONTS['body']}px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }}
    
    [data-testid="stNumberInput"] input {{
        background-color: {COLORS['light_blue']} !important;
        color: {COLORS['text_light']} !important;
        border: 2px solid {COLORS['gold']} !important;
        border-radius: 6px !important;
        padding: 10px !important;
        font-size: {FONTS['body']}px !important;
    }}
    
    [data-testid="stNumberInput"] input:focus {{
        border-color: {COLORS['gold']} !important;
        box-shadow: 0px 0px 8px rgba(255, 215, 0, 0.5) !important;
    }}
    
    /* Text Input - HIGH CONTRAST */
    [data-testid="stTextInput"] label {{
        color: {COLORS['text_dark']} !important;
        font-weight: 600 !important;
    }}
    
    [data-testid="stTextInput"] input {{
        background-color: {COLORS['light_blue']} !important;
        color: {COLORS['text_light']} !important;
        border: 2px solid {COLORS['gold']} !important;
        border-radius: 6px !important;
        padding: 10px !important;
    }}
    
    /* ====================================================================
       CONTAINER STYLING
       ==================================================================== */
    
    [data-testid="column"] {{
        background-color: transparent !important;
    }}
    
    .stTabs {{
        background-color: transparent !important;
    }}
    
    [data-testid="stTabs"] button {{
        color: {COLORS['text_dark']} !important;
        background-color: {COLORS['light_blue']} !important;
        border: 2px solid {COLORS['light_blue']} !important;
        border-radius: 6px 6px 0 0 !important;
        margin-right: 5px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }}
    
    [data-testid="stTabs"] button:hover {{
        background-color: {COLORS['gold']} !important;
        color: {COLORS['dark_blue']} !important;
    }}
    
    /* Active Tab */
    [data-testid="stTabs"] [role="tablist"] [role="tab"][aria-selected="true"] {{
        background-color: {COLORS['gold']} !important;
        color: {COLORS['dark_blue']} !important;
        border-color: {COLORS['gold']} !important;
    }}
    
    /* Tab Content */
    [data-testid="stTabs"] [role="tabpanel"] {{
        background-color: transparent !important;
        color: {COLORS['text_dark']} !important;
        padding: 20px 10px !important;
    }}
    
    /* ====================================================================
       METRIC CARDS & BOXES
       ==================================================================== */
    
    [data-testid="metric-container"] {{
        background: linear-gradient(135deg, {COLORS['light_blue']} 0%, {COLORS['dark_blue']} 100%) !important;
        border-left: 4px solid {COLORS['gold']} !important;
        border-radius: 8px !important;
        padding: 20px !important;
        margin: 10px 0 !important;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3) !important;
    }}
    
    /* ====================================================================
       TABLE STYLING
       ==================================================================== */
    
    [data-testid="stDataFrame"] {{
        background-color: {COLORS['light_blue']} !important;
        color: {COLORS['text_light']} !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }}
    
    [data-testid="stDataFrame"] tr {{
        background-color: {COLORS['light_blue']} !important;
        color: {COLORS['text_light']} !important;
        border: 1px solid {COLORS['gold']} !important;
    }}
    
    [data-testid="stDataFrame"] th {{
        background-color: {COLORS['dark_blue']} !important;
        color: {COLORS['gold']} !important;
        font-weight: 700 !important;
        padding: 12px !important;
        border: 2px solid {COLORS['gold']} !important;
    }}
    
    [data-testid="stDataFrame"] td {{
        padding: 10px !important;
        text-align: center !important;
        border: 1px solid {COLORS['gold']} !important;
    }}
    
    /* ====================================================================
       EXPANDER STYLING
       ==================================================================== */
    
    [data-testid="stExpander"] {{
        border: 2px solid {COLORS['gold']} !important;
        border-radius: 8px !important;
        background-color: transparent !important;
    }}
    
    [data-testid="stExpander"] button {{
        background-color: {COLORS['light_blue']} !important;
        color: {COLORS['text_light']} !important;
    }}
    
    [data-testid="stExpander"] button:hover {{
        background-color: {COLORS['gold']} !important;
    }}
    
    /* ====================================================================
       PLOTLY CHART STYLING
       ==================================================================== */
    
    [data-testid="stPlotlyChart"] {{
        background-color: transparent !important;
    }}
    
    .plotly {{
        background-color: transparent !important;
    }}
    
    /* ====================================================================
       ALERT & INFO BOXES
       ==================================================================== */
    
    .stAlert {{
        border-radius: 8px !important;
        border-left: 4px solid !important;
        padding: 15px !important;
        margin: 10px 0 !important;
    }}
    
    /* Success Alert */
    .stSuccess {{
        background-color: rgba(0, 204, 102, 0.1) !important;
        border-color: {COLORS['success']} !important;
        color: {COLORS['success']} !important;
    }}
    
    /* Info Alert */
    .stInfo {{
        background-color: rgba(0, 102, 204, 0.1) !important;
        border-color: {COLORS['light_blue']} !important;
        color: {COLORS['light_blue']} !important;
    }}
    
    /* Warning Alert */
    .stWarning {{
        background-color: rgba(255, 107, 53, 0.1) !important;
        border-color: {COLORS['warning']} !important;
        color: {COLORS['warning']} !important;
    }}
    
    /* Error Alert */
    .stError {{
        background-color: rgba(204, 0, 0, 0.1) !important;
        border-color: {COLORS['error']} !important;
        color: {COLORS['error']} !important;
    }}
    
    /* ====================================================================
       SCROLLBAR STYLING
       ==================================================================== */
    
    ::-webkit-scrollbar {{
        width: 10px !important;
        height: 10px !important;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {COLORS['dark_blue']} !important;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {COLORS['gold']} !important;
        border-radius: 5px !important;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {COLORS['light_blue']} !important;
    }}
    
    /* ====================================================================
       FOOTER STYLING
       ==================================================================== */
    
    footer {{
        background-color: {COLORS['dark_blue']} !important;
        color: {COLORS['gold']} !important;
        border-top: 2px solid {COLORS['gold']} !important;
        padding: 10px !important;
        font-size: {FONTS['small']}px !important;
    }}
    
    /* ====================================================================
       RESPONSIVE DESIGN
       ==================================================================== */
    
    @media (max-width: 768px) {{
        h1 {{
            font-size: 24px !important;
        }}
        
        h2 {{
            font-size: 20px !important;
        }}
        
        p, span {{
            font-size: 14px !important;
        }}
        
        button {{
            padding: 8px 16px !important;
        }}
    }}
    
    /* ====================================================================
       ACCESSIBILITY
       ==================================================================== */
    
    /* Focus states for keyboard navigation */
    button:focus, input:focus, select:focus {{
        outline: 3px solid {COLORS['gold']} !important;
        outline-offset: 2px !important;
    }}
    
    /* High contrast for readability */
    .high-contrast {{
        font-weight: 700 !important;
        color: {COLORS['gold']} !important;
    }}
    
    /* Smooth transitions */
    * {{
        transition: background-color 0.2s ease !important;
    }}
    
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)


def get_metric_color(value: float, metric_type: str = "return") -> str:
    """
    Get color for metric value based on type and magnitude
    
    Args:
        value: Metric value
        metric_type: Type of metric (return, volatility, sharpe, etc.)
    
    Returns:
        Color hex code
    """
    
    if metric_type == "return":
        return COLORS['success'] if value >= 0 else COLORS['error']
    elif metric_type == "volatility":
        if value <= 0.10:
            return COLORS['success']
        elif value <= 0.20:
            return "#FFD700"
        else:
            return COLORS['warning']
    elif metric_type == "sharpe":
        if value >= 1.0:
            return COLORS['success']
        elif value >= 0.5:
            return "#FFD700"
        else:
            return COLORS['warning']
    else:
        return COLORS['light_blue']


def create_metric_card(label: str, value: str, emoji: str = "", color: str = None) -> str:
    """
    Create a styled metric card
    
    Args:
        label: Metric label
        value: Metric value
        emoji: Emoji to display
        color: Custom color
    
    Returns:
        HTML string for metric card
    """
    
    if color is None:
        color = COLORS['gold']
    
    card_html = f"""
    <div style="
        background: linear-gradient(135deg, {COLORS['light_blue']} 0%, {COLORS['dark_blue']} 100%);
        border-left: 4px solid {color};
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
    ">
        <p style="
            color: {COLORS['text_dark']};
            font-size: 14px;
            margin: 0;
            margin-bottom: 5px;
        ">{emoji} {label}</p>
        <p style="
            color: {color};
            font-size: 24px;
            font-weight: 700;
            margin: 0;
        ">{value}</p>
    </div>
    """
    
    return card_html
