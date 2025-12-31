"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - CUSTOM SIDEBAR COMPONENT
Professional sidebar with profile, navigation, and branding
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st

def render_custom_sidebar():
    """
    Renders a custom dark blue sidebar with:
    - Profile section (Prof. V. Ravichandran)
    - LinkedIn button
    - Navigation links
    - Branding footer
    """
    
    sidebar_html = """
    <style>
        /* Sidebar background */
        [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(135deg, #003366 0%, #004d80 100%);
        }
        
        [data-testid="stSidebar"] {
            background: #003366;
        }
        
        /* Sidebar text styling */
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color: white !important;
        }
        
        /* Navigation items */
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border: 1px solid #FFD700 !important;
            width: 100% !important;
            margin: 5px 0 !important;
            text-align: left !important;
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: #FFD700 !important;
            color: #003366 !important;
        }
        
        /* Profile section styling */
        .profile-section {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid #FFD700;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            color: white;
        }
        
        .profile-name {
            font-size: 18px;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .profile-text {
            font-size: 13px;
            color: white;
            text-align: center;
            margin: 5px 0;
            line-height: 1.4;
        }
        
        .linkedin-btn {
            display: block;
            background: #0A66C2 !important;
            color: white !important;
            padding: 10px !important;
            border-radius: 5px !important;
            text-align: center !important;
            margin-top: 12px !important;
            font-weight: bold !important;
            text-decoration: none !important;
            border: none !important;
            cursor: pointer !important;
            width: 100% !important;
            box-sizing: border-box !important;
        }
        
        .linkedin-btn:hover {
            background: #004182 !important;
            text-decoration: none !important;
        }
        
        .divider {
            border-top: 1px solid #FFD700;
            margin: 15px 0;
            opacity: 0.5;
        }
        
        .nav-section {
            margin: 20px 0;
        }
        
        .nav-title {
            color: #FFD700;
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        
        .branding-footer {
            border-top: 1px solid #FFD700;
            padding-top: 15px;
            margin-top: 30px;
            text-align: center;
            font-size: 12px;
            color: #FFD700;
        }
    </style>
    
    <div class="profile-section">
        <div class="profile-name">👤 Prof. V. Ravichandran</div>
        <div class="profile-text">28+ Years Corporate Finance & Banking Experience</div>
        <div class="profile-text">10+ Years Academic Excellence</div>
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank" class="linkedin-btn">
            🔗 LinkedIn Profile
        </a>
    </div>
    
    <div class="divider"></div>
    
    <div class="nav-section">
        <div class="nav-title">📍 Portfolio Optimizer</div>
        <p style="color: white; font-size: 12px; margin: 0;">
            Advanced portfolio optimization using Modern Portfolio Theory (MPT)
        </p>
    </div>
    
    <div class="divider"></div>
    
    <div class="branding-footer">
        🏔️ The Mountain Path<br>
        World of Finance
    </div>
    """
    
    st.markdown(sidebar_html, unsafe_allow_html=True)


def add_sidebar_css():
    """Add CSS for sidebar styling to the main page"""
    css = """
    <style>
        /* Main sidebar container */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #003366 0%, #004d80 100%);
        }
        
        [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(180deg, #003366 0%, #004d80 100%);
        }
        
        /* All text in sidebar */
        [data-testid="stSidebar"] {
            color: white;
        }
        
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Expanders in sidebar */
        [data-testid="stSidebar"] .streamlit-expanderHeader {
            background: rgba(255, 215, 0, 0.1);
            color: white;
        }
        
        /* Links in sidebar */
        [data-testid="stSidebar"] a {
            color: #FFD700 !important;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
