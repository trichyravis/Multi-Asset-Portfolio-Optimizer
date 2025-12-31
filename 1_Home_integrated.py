"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - HOME PAGE
Portfolio Setup & Asset Selection
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
from styles import apply_main_styles, render_header, render_footer
from components import Section, InfoBox

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="Home - Portfolio Optimizer", layout="wide")
apply_main_styles()
render_header(title="🏠 Portfolio Setup")

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "selected_classes" not in st.session_state:
    st.session_state.selected_classes = []

if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}

if "weights" not in st.session_state:
    st.session_state.weights = {}

if "mpt_objective" not in st.session_state:
    st.session_state.mpt_objective = "Maximize Sharpe Ratio"

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET CLASS OPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_CLASSES = {
    "Equities": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM"],
    "Indices": ["SPY", "QQQ", "IWM", "EFA", "VTI"],
    "Bonds": ["BND", "AGG", "SHV", "TLT", "LQD"],
    "Commodities": ["GLD", "SLV", "USO", "DBC", "PDBC"],
    "Cryptocurrencies": ["BTC", "ETH"],
    "Currencies": ["EUR", "GBP", "JPY", "CHF"],
}

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: SELECT ASSET CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

Section.render("STEP 1: SELECT ASSET CLASSES", emoji="🎯")
st.write("Choose one or more asset classes for your portfolio:")

selected_classes = st.multiselect(
    label="Asset Classes",
    options=list(ASSET_CLASSES.keys()),
    default=st.session_state.selected_classes,
    label_visibility="collapsed"
)

st.session_state.selected_classes = selected_classes

if not selected_classes:
    InfoBox.warning("Please select at least one asset class")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: SELECT SPECIFIC ASSETS
# ═══════════════════════════════════════════════════════════════════════════════

if selected_classes:
    Section.render("STEP 2: SELECT SPECIFIC ASSETS", emoji="🎯")
    st.write("Choose specific assets from each selected asset class:")
    
    selected_assets = {}
    
    for asset_class in selected_classes:
        with st.expander(f"**{asset_class}** Assets", expanded=True):
            assets = st.multiselect(
                label=f"Select {asset_class}",
                options=ASSET_CLASSES[asset_class],
                default=st.session_state.selected_assets.get(asset_class, []),
                label_visibility="collapsed",
                key=f"assets_{asset_class}"
            )
            if assets:
                selected_assets[asset_class] = assets
            elif asset_class in st.session_state.selected_assets:
                selected_assets[asset_class] = []
    
    st.session_state.selected_assets = selected_assets
    
    # Count total assets
    total_assets = sum(len(assets) for assets in selected_assets.values())
    if total_assets == 0:
        InfoBox.warning("Please select at least one asset from each class")
    else:
        st.success(f"✅ Selected {total_assets} assets")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3: ALLOCATE WEIGHTS
# ═══════════════════════════════════════════════════════════════════════════════

if selected_assets and any(len(assets) > 0 for assets in selected_assets.values()):
    Section.render("STEP 3: ALLOCATE WEIGHTS", emoji="⚖️")
    st.write("Distribute portfolio weights among selected assets (must sum to 100%):")
    
    # Flatten all selected assets
    all_assets = []
    for asset_class, assets in selected_assets.items():
        all_assets.extend(assets)
    
    # Initialize weights
    weights = {}
    equal_weight = 100 / len(all_assets) if all_assets else 0
    
    st.markdown("**Auto-populate equal weights:**")
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("📊 Equal Weights", use_container_width=True):
            for asset in all_assets:
                st.session_state.weights[asset] = equal_weight
            st.rerun()
    
    st.markdown("**Adjust individual weights:**")
    weight_cols = st.columns(min(3, len(all_assets)))
    
    for idx, asset in enumerate(all_assets):
        with weight_cols[idx % min(3, len(all_assets))]:
            weight = st.number_input(
                label=f"**{asset}** Weight (%)",
                min_value=0.0,
                max_value=100.0,
                value=st.session_state.weights.get(asset, equal_weight),
                step=0.1,
                label_visibility="collapsed",
                key=f"weight_{asset}"
            )
            weights[asset] = weight
    
    st.session_state.weights = weights
    
    # Calculate total weight
    total_weight = sum(weights.values())
    
    # Display weight validation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Weight", f"{total_weight:.1f}%")
    
    with col2:
        if total_weight == 100.0:
            st.success("✅ Weights sum to 100%")
        elif total_weight > 100.0:
            st.error(f"⚠️ Weights exceed 100% by {total_weight - 100:.1f}%")
        else:
            st.warning(f"⚠️ Weights are {100 - total_weight:.1f}% short of 100%")
    
    with col3:
        st.metric("Number of Assets", len(all_assets))

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4: OPTIMIZATION METHOD
# ═══════════════════════════════════════════════════════════════════════════════

if selected_assets and any(len(assets) > 0 for assets in selected_assets.values()):
    if sum(st.session_state.weights.values()) == 100.0:
        
        Section.render("STEP 4: SELECT OPTIMIZATION METHOD", emoji="🎯")
        st.write("Choose the Modern Portfolio Theory optimization objective:")
        
        mpt_objective = st.radio(
            label="Optimization Objective",
            options=[
                "Maximize Returns",
                "Minimize Risk",
                "Maximize Sharpe Ratio"
            ],
            index=2 if st.session_state.mpt_objective == "Maximize Sharpe Ratio" 
                  else (0 if st.session_state.mpt_objective == "Maximize Returns" else 1),
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.session_state.mpt_objective = mpt_objective
        
        # Display description
        descriptions = {
            "Maximize Returns": "Focus on highest expected returns, accepting higher risk",
            "Minimize Risk": "Focus on lowest portfolio volatility, accepting lower returns",
            "Maximize Sharpe Ratio": "Balance returns and risk - optimal risk-adjusted returns"
        }
        
        st.info(f"📊 {descriptions[mpt_objective]}")
        
        st.markdown("---")
        
        # PROCEED TO RESULTS
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("🚀 Optimize Portfolio", use_container_width=True, type="primary"):
                st.switch_page("pages/2_📊_Results.py")
        
        with col2:
            st.write("**Next Step:** Click 'Optimize Portfolio' to analyze and optimize your portfolio")

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

render_footer()
