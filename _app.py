
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
Multi-Asset Portfolio Optimizer - Main Entry Point
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT - REDIRECT TO HOME PAGE
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="🏔️ Portfolio Optimizer - The Mountain Path",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Redirect to Home page immediately
st.switch_page("pages/1_🏠_Home.py")
