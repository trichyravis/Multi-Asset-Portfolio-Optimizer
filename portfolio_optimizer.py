
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - PROFESSIONAL PORTFOLIO OPTIMIZER
Completely redesigned with professional components and styling
═══════════════════════════════════════════════════════════════════════════════

Run with: streamlit run portfolio_optimizer_REDESIGNED.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Import professional components and styling
from config_REDESIGNED import (
    PAGE_CONFIG, COLORS, PORTFOLIO_PARAMS, OPTIMIZATION_METHODS, 
    ASSET_CLASSES, APP_BRANDING
)
from styles_REDESIGNED import apply_professional_styles
from components_REDESIGNED import (
    HeroHeader, SidebarSection, WeightAllocationDisplay, 
    MetricsDisplay, ResultsDisplay, Footer
)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title=PAGE_CONFIG["page_title"],
    page_icon=PAGE_CONFIG["page_icon"],
    layout=PAGE_CONFIG["layout"],
    initial_sidebar_state=PAGE_CONFIG["initial_sidebar_state"]
)

# Apply professional styles
apply_professional_styles()

# Initialize session state
if 'portfolio_data' not in st.session_state:
    st.session_state.portfolio_data = None
    st.session_state.optimization_results = None
    st.session_state.original_weights = None
    st.session_state.risk_free_rate = None

# ═══════════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════════

HeroHeader.render(
    title=APP_BRANDING["name"],
    subtitle=APP_BRANDING["tagline"],
    description="Professional Portfolio Analysis • Risk Management • Optimization",
    emoji="🏔️"
)

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR - 7-STEP WORKFLOW
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown(f"<div style='color: {COLORS['accent_gold']}; font-size: 18px; font-weight: 700; margin-bottom: 1.5rem;'>⚙️ PORTFOLIO SETUP</div>", unsafe_allow_html=True)
    
    # STEP 1: Time Period
    SidebarSection.render_header("📅", "Select Time Period", 1)
    lookback_days = st.slider(
        "Lookback Period (days):",
        min_value=PORTFOLIO_PARAMS['lookback_min'],
        max_value=PORTFOLIO_PARAMS['lookback_max'],
        value=PORTFOLIO_PARAMS['lookback_default'],
        step=5,
    )
    
    # STEP 2: Asset Classes
    SidebarSection.render_header("📊", "Select Asset Classes", 2)
    selected_classes = st.multiselect(
        "Choose asset classes:",
        options=list(ASSET_CLASSES.keys()),
        default=list(ASSET_CLASSES.keys())[:2],
    )
    
    if not selected_classes:
        st.error("Please select at least one asset class")
        st.stop()
    
    # STEP 3: Asset Selection
    SidebarSection.render_header("🎯", "Select Specific Assets", 3)
    selected_tickers = {}
    all_tickers = []
    
    for asset_class in selected_classes:
        available_tickers = list(ASSET_CLASSES[asset_class].keys())
        selected = st.multiselect(
            f"Choose from {asset_class.split(':')[1].strip()}:",
            options=available_tickers,
            default=available_tickers[:2],
            key=f"select_{asset_class}"
        )
        
        if selected:
            selected_tickers[asset_class] = selected
            all_tickers.extend(selected)
    
    if not all_tickers:
        st.error("Please select at least one asset")
        st.stop()
    
    # STEP 4: Weight Allocation
    SidebarSection.render_header("⚖️", "Allocate Portfolio Weights", 4)
    SidebarSection.render_description("Total = 100% with equal weight default")
    
    portfolio_weights = WeightAllocationDisplay.render(all_tickers)
    if portfolio_weights is None:
        st.stop()
    
    # STEP 5: Risk-Free Rate
    SidebarSection.render_header("📍", "Risk-Free Rate", 5)
    risk_free_rate = st.slider(
        "Annual Risk-Free Rate (%):",
        min_value=int(PORTFOLIO_PARAMS['risk_free_rate_min'] * 100),
        max_value=int(PORTFOLIO_PARAMS['risk_free_rate_max'] * 100),
        value=int(PORTFOLIO_PARAMS['risk_free_rate_default'] * 100),
        step=1,
    ) / 100
    
    # STEP 6: Optimization Method
    SidebarSection.render_header("⚡", "Optimization Method", 6)
    opt_method = st.radio(
        "Select strategy:",
        options=list(OPTIMIZATION_METHODS.keys()),
        format_func=lambda x: f"{OPTIMIZATION_METHODS[x]['emoji']} {OPTIMIZATION_METHODS[x]['label']}"
    )
    
    st.info(OPTIMIZATION_METHODS[opt_method]['description'])
    
    # STEP 7: Run Optimization
    st.markdown("---")
    if st.button("🚀 FETCH DATA & OPTIMIZE", use_container_width=True):
        with st.spinner("Fetching data and optimizing portfolio..."):
            try:
                # Fetch data
                st.session_state.portfolio_data = {
                    'tickers': all_tickers,
                    'weights': portfolio_weights,
                    'lookback': lookback_days,
                }
                st.session_state.risk_free_rate = risk_free_rate
                st.session_state.optimization_method = opt_method
                st.success("✅ Portfolio ready for analysis!")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.portfolio_data is None:
    # Welcome message
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, rgba(0, 51, 102, 0.3) 0%, rgba(0, 77, 128, 0.3) 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid {COLORS["accent_gold"]};
        margin: 2rem 0;
    '>
        <h2 style='color: {COLORS["accent_gold"]}; margin-top: 0;'>👋 Welcome</h2>
        <p style='color: {COLORS["text_white"]};'>
            Complete the 7-step configuration in the sidebar to analyze and optimize your portfolio.
        </p>
        
        <h3 style='color: {COLORS["text_white"]}; margin-top: 1.5rem;'>📋 Workflow:</h3>
        <ul style='color: {COLORS["text_white"]};'>
            <li>📅 <strong>Step 1:</strong> Select historical data period (30-90 days)</li>
            <li>📊 <strong>Step 2:</strong> Choose asset classes (Equities, Indices, etc.)</li>
            <li>🎯 <strong>Step 3:</strong> Select specific assets</li>
            <li>⚖️ <strong>Step 4:</strong> Allocate portfolio weights (equal by default)</li>
            <li>📍 <strong>Step 5:</strong> Set risk-free rate</li>
            <li>⚡ <strong>Step 6:</strong> Choose optimization method</li>
            <li>🚀 <strong>Step 7:</strong> Fetch data and optimize</li>
        </ul>
        
        <h3 style='color: {COLORS["text_white"]}; margin-top: 1.5rem;'>🎯 Available Assets:</h3>
        <p style='color: {COLORS["text_white"]};'>
            🇮🇳 Indian Equities • 📈 Indices • 🇺🇸 US Futures • 🏆 Commodities • 💱 Currencies • ₿ Crypto
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Display results
    ResultsDisplay.render_comparison_header()
    
    # Display portfolio summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Assets", len(st.session_state.portfolio_data['tickers']))
    
    with col2:
        st.metric("Time Period", f"{st.session_state.portfolio_data['lookback']} days")
    
    with col3:
        st.metric("Risk-Free Rate", f"{st.session_state.risk_free_rate*100:.1f}%")
    
    # Display weights
    st.markdown(f"<h3 style='color: {COLORS['accent_gold']}; margin-top: 2rem;'>📊 Portfolio Allocation</h3>", unsafe_allow_html=True)
    
    weights_df = pd.DataFrame({
        'Asset': st.session_state.portfolio_data['tickers'],
        'Weight': [f"{w*100:.1f}%" for w in st.session_state.portfolio_data['weights'].values()]
    })
    
    st.dataframe(weights_df, use_container_width=True, hide_index=True)
    
    # Display optimization method
    opt_method = st.session_state.get('optimization_method', 'max_sharpe')
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, rgba(0, 51, 102, 0.5) 0%, rgba(0, 77, 128, 0.5) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid {COLORS["accent_gold"]};
        margin: 1.5rem 0;
    '>
        <h3 style='color: {COLORS["accent_gold"]}; margin-top: 0;'>
            {OPTIMIZATION_METHODS[opt_method]['emoji']} {OPTIMIZATION_METHODS[opt_method]['label']}
        </h3>
        <p style='color: {COLORS["text_white"]}; margin: 0;'>
            {OPTIMIZATION_METHODS[opt_method]['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

Footer.render(
    author=APP_BRANDING["author"],
    platform=APP_BRANDING["platform"]
)
