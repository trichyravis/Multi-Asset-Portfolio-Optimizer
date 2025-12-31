"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - MULTI-ASSET PORTFOLIO OPTIMIZER
═══════════════════════════════════════════════════════════════════════════════

Main entry point for the application.
Handles page configuration, header, and footer.

Run with: streamlit run app.py
"""

import streamlit as st
from styles import apply_main_styles
from components import HeroHeader, Footer
from config import PAGE_CONFIG, COLORS

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Multi-Asset Portfolio Optimizer",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_main_styles()

# ═══════════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════════

HeroHeader.render(
    title="MULTI-ASSET PORTFOLIO OPTIMIZER",
    subtitle="Professional Risk Management & Optimization",
    description="Modern Portfolio Theory • Sharpe Ratio Optimization • Real-Time Analysis",
    emoji="🏔️"
)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT (Rendered by page files)
# ═══════════════════════════════════════════════════════════════════════════════

# Pages are automatically handled by Streamlit multi-page app structure
# See pages/ folder:
# - 1_🏠_Home.py
# - 2_📊_Results.py

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")

Footer.render(
    title="The Mountain Path - World of Finance",
    description="Professional Portfolio Optimization Platform",
    author="Prof. V. Ravichandran | 28+ Years Corporate Finance | 10+ Years Academic Excellence",
    social_links={},
    disclaimer="This tool is for educational and analytical purposes. Past performance does not guarantee future results. Always consult financial advisors before making investment decisions."
)
