
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - ENHANCED STYLES
Dark Blue Theme with White Text
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
from config_enhanced import COLORS, TYPOGRAPHY

def apply_main_styles():
    """Apply all custom styles - White background with dark blue content containers"""
    st.markdown(f"""
    <style>
    /* ═══════════════════════════════════════════════════════════════════════════════
       MAIN BACKGROUND - WHITE PAGE
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .main {{
        background: white;
        color: #333333;
    }}
    
    .appview-container {{
        background: white;
        color: #333333;
    }}
    
    /* Full page background */
    body {{
        background: white !important;
        color: #333333;
        font-family: {TYPOGRAPHY['font_secondary']};
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       HEADINGS - DARK BLUE TEXT ON WHITE
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    h1, h2, h3, h4, h5, h6 {{
        color: {COLORS['dark_blue']};
        font-family: {TYPOGRAPHY['font_main']};
    }}
    
    h1 {{
        font-size: {TYPOGRAPHY['h1_size']};
        font-weight: bold;
        border-bottom: 2px solid {COLORS['gold']};
        padding-bottom: 10px;
        color: {COLORS['dark_blue']};
    }}
    
    h2 {{
        font-size: {TYPOGRAPHY['h2_size']};
        color: {COLORS['dark_blue']};
    }}
    
    h3 {{
        font-size: {TYPOGRAPHY['h3_size']};
        color: {COLORS['dark_blue']};
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       TEXT & PARAGRAPHS - DARK TEXT
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    p {{
        color: #333333;
        line-height: 1.6;
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       LINKS
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    a {{
        color: {COLORS['gold']};
        text-decoration: none;
    }}
    
    a:hover {{
        color: {COLORS['light_blue']};
        text-decoration: underline;
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       SIDEBAR - LIGHT GRAY
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    [data-testid="stSidebar"] {{
        background: #f5f5f5;
    }}
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
        color: #333333;
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       BUTTONS - DARK BLUE WITH WHITE TEXT
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .stButton > button {{
        background: {COLORS['dark_blue']};
        color: {COLORS['text_light']};
        border: 1px solid {COLORS['gold']};
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background: {COLORS['gold']};
        color: {COLORS['dark_blue']};
        border-color: {COLORS['dark_blue']};
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       INPUT FIELDS
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .stTextInput > label, .stNumberInput > label, .stSelectbox > label {{
        color: {COLORS['text_light']};
    }}
    
    .stTextInput input, .stNumberInput input, .stSelectbox select {{
        background: rgba(255, 255, 255, 0.1);
        color: {COLORS['text_light']};
        border: 1px solid {COLORS['light_blue']};
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       CONTAINERS & SECTIONS
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .section-container {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid {COLORS['light_blue']};
        padding: 20px;
        border-radius: 8px;
        color: {COLORS['text_light']};
        margin-bottom: 20px;
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       METRIC CARDS - DARK BLUE WITH GOLD BORDER
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .metric-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid {COLORS['gold']};
        color: {COLORS['text_light']};
        padding: 20px;
        border-radius: 8px;
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
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       MESSAGE BOXES
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .success-box {{
        background: rgba(46, 204, 113, 0.2);
        border-left: 4px solid {COLORS['success']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['success']};
    }}
    
    .warning-box {{
        background: rgba(243, 156, 18, 0.2);
        border-left: 4px solid {COLORS['warning']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['warning']};
    }}
    
    .error-box {{
        background: rgba(231, 76, 60, 0.2);
        border-left: 4px solid {COLORS['danger']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['danger']};
    }}
    
    .info-box {{
        background: rgba(173, 216, 230, 0.1);
        border-left: 4px solid {COLORS['light_blue']};
        padding: 12px;
        border-radius: 4px;
        color: {COLORS['text_light']};
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       TABLES & DATAFRAMES
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    [data-testid="stDataFrame"] {{
        background: rgba(255, 255, 255, 0.05);
        color: {COLORS['text_light']};
    }}
    
    [data-testid="stDataFrame"] th {{
        background: {COLORS['dark_blue']};
        color: {COLORS['text_light']};
        border: 1px solid {COLORS['light_blue']};
    }}
    
    [data-testid="stDataFrame"] td {{
        border: 1px solid {COLORS['light_blue']};
        color: {COLORS['text_light']};
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       EXPANDER
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    .streamlit-expanderHeader {{
        color: {COLORS['text_light']};
        background: rgba(255, 255, 255, 0.05);
    }}
    
    /* ═══════════════════════════════════════════════════════════════════════════════
       HIDE STREAMLIT DEFAULTS
       ═══════════════════════════════════════════════════════════════════════════════ */
    
    #MainMenu {{
        visibility: hidden;
    }}
    
    footer {{
        visibility: hidden;
    }}
    </style>
    """, unsafe_allow_html=True)

def render_header(title: str = "🏔️ Portfolio Optimizer", method: str = None):
    """Render professional header"""
    if method:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%); 
                    color: {COLORS['text_light']}; padding: 8px 20px; margin: 0 0 20px 0; 
                    border-bottom: 2px solid {COLORS['gold']}; display: flex; 
                    align-items: center; justify-content: space-between;">
            <div>
                <div style="font-size: 16px; font-weight: bold; color: {COLORS['text_light']};">{title}</div>
                <div style="font-size: 12px; color: {COLORS['light_blue']};">The Mountain Path - World of Finance</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.1); border: 1px solid {COLORS['gold']}; 
                        color: {COLORS['gold']}; padding: 4px 12px; border-radius: 4px; 
                        font-size: 11px; font-weight: bold;">{method}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%); 
                    color: {COLORS['text_light']}; padding: 8px 20px; margin: 0 0 20px 0; 
                    border-bottom: 2px solid {COLORS['gold']};">
            <div style="font-size: 16px; font-weight: bold; color: {COLORS['text_light']};">{title}</div>
            <div style="font-size: 12px; color: {COLORS['light_blue']};">The Mountain Path - World of Finance</div>
        </div>
        """, unsafe_allow_html=True)

def render_footer():
    """Render professional footer"""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {COLORS['dark_blue']} 0%, {COLORS['dark_blue']} 100%); 
                color: {COLORS['text_light']}; padding: 10px 20px; margin-top: 30px; 
                border-top: 2px solid {COLORS['gold']}; display: flex; 
                align-items: center; justify-content: space-between; flex-wrap: wrap;">
        <div>
            <div style="font-weight: bold; font-size: 12px; color: {COLORS['text_light']};">Prof. V. Ravichandran</div>
            <div style="color: {COLORS['light_blue']}; font-size: 11px;">28+ Years Corporate Finance | 10+ Years Academic Excellence</div>
        </div>
        <div style="width: 1px; height: 20px; background: {COLORS['gold']}; opacity: 0.3; margin: 0 20px;"></div>
        <div style="color: {COLORS['text_light']}; font-weight: bold; font-size: 12px;">
            🏔️ The Mountain Path - World of Finance
        </div>
    </div>
    """, unsafe_allow_html=True)
