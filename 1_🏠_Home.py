"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - HOME PAGE
═══════════════════════════════════════════════════════════════════════════════

Portfolio Setup & Configuration
Step 1: Select Asset Classes
Step 2: Select Specific Assets
Step 3: Allocate Weights
Step 4: Choose Optimization Method
"""

import streamlit as st
import numpy as np
from config import COLORS

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_CLASSES = {
    "Indian Equities": ["TCS", "INFY", "HDFC", "RELIANCE", "WIPRO", "MARUTI", "BAJAJFINSV", "LT", "SUNPHARMA", "HCL"],
    "Indices": ["^NSEI", "^BSESN", "^NSEBANK", "^NSMID50", "^NSEINFRA"],
    "US Futures": ["ES=F", "NQ=F", "RTY=F", "YM=F"],
    "Commodities": ["GC=F", "SI=F", "CL=F", "HG=F", "ZC=F", "ZW=F", "ZS=F"],
    "Currencies": ["EURUSD=X", "GBPUSD=X", "JPYUSD=X", "INRUSD=X"],
    "Cryptocurrencies": ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "XRP-USD"]
}

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.title("🏠 Portfolio Setup & Configuration")
st.markdown("Configure your portfolio for optimization analysis")
st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if 'selected_classes' not in st.session_state:
    st.session_state.selected_classes = []

if 'selected_assets' not in st.session_state:
    st.session_state.selected_assets = []

if 'asset_weights' not in st.session_state:
    st.session_state.asset_weights = {}

if 'optimization_method' not in st.session_state:
    st.session_state.optimization_method = "Maximize Sharpe Ratio"

if 'mpt_objective' not in st.session_state:
    st.session_state.mpt_objective = "Maximize Returns"

if 'risk_free_rate' not in st.session_state:
    st.session_state.risk_free_rate = 5.0

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: SELECT ASSET CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 📊 STEP 1: SELECT ASSET CLASSES")
st.markdown("Choose one or more asset classes for your portfolio:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Asset Class Selection")
    
    selected_classes = st.multiselect(
        "Select Asset Classes:",
        options=list(ASSET_CLASSES.keys()),
        default=st.session_state.selected_classes,
        key="asset_classes_multiselect"
    )
    
    st.session_state.selected_classes = selected_classes

with col2:
    st.markdown("### Your Selection")
    if selected_classes:
        st.write(f"**Selected:** {len(selected_classes)} class(es)")
        for cls in selected_classes:
            st.write(f"✅ {cls}")
    else:
        st.warning("No asset classes selected yet")

with col3:
    st.markdown("### Information")
    st.info(f"""
    **Total Classes Available:** {len(ASSET_CLASSES)}
    
    **Selected:** {len(selected_classes)}
    
    **Next Step:** Select specific assets from each class
    """)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: SELECT SPECIFIC ASSETS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 🎯 STEP 2: SELECT SPECIFIC ASSETS")
st.markdown("Choose specific assets from each selected asset class:")

if not selected_classes:
    st.warning("⚠️ Please select at least one asset class in Step 1")
else:
    selected_assets = []
    
    # Create tabs for each selected class
    if len(selected_classes) == 1:
        # Single class - show directly
        class_name = selected_classes[0]
        assets_in_class = ASSET_CLASSES[class_name]
        
        st.markdown(f"### {class_name}")
        assets = st.multiselect(
            f"Select assets from {class_name}:",
            options=assets_in_class,
            default=[a for a in st.session_state.selected_assets if a in assets_in_class],
            key=f"assets_{class_name}"
        )
        selected_assets.extend(assets)
    
    else:
        # Multiple classes - use tabs
        tabs = st.tabs([f"📌 {cls}" for cls in selected_classes])
        
        for idx, class_name in enumerate(selected_classes):
            with tabs[idx]:
                assets_in_class = ASSET_CLASSES[class_name]
                
                assets = st.multiselect(
                    f"Select assets from {class_name}:",
                    options=assets_in_class,
                    default=[a for a in st.session_state.selected_assets if a in assets_in_class],
                    key=f"assets_{class_name}"
                )
                selected_assets.extend(assets)
    
    st.session_state.selected_assets = selected_assets
    
    # Show summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Assets Selected", len(selected_assets))
    with col2:
        st.metric("Classes", len(selected_classes))
    with col3:
        st.metric("Assets Per Class (avg)", round(len(selected_assets) / len(selected_classes), 1) if selected_classes else 0)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3: ALLOCATE WEIGHTS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## ⚖️ STEP 3: ALLOCATE WEIGHTS")
st.markdown("Distribute portfolio weights among selected assets (must sum to 100%)")

if not selected_assets:
    st.warning("⚠️ Please select at least one asset in Step 2")
else:
    # Auto-populate equal weights if not yet initialized
    if not st.session_state.asset_weights or len(st.session_state.asset_weights) != len(selected_assets):
        equal_weight = 100.0 / len(selected_assets)
        st.session_state.asset_weights = {asset: equal_weight for asset in selected_assets}
    
    # Display weight allocation interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Asset Weights")
        weights_dict = {}
        
        for idx, asset in enumerate(selected_assets):
            # Get current weight from session state
            current_weight = st.session_state.asset_weights.get(asset, 100.0 / len(selected_assets))
            
            # Number input for weight
            weight = st.number_input(
                f"{idx + 1}. {asset}",
                min_value=0.0,
                max_value=100.0,
                value=current_weight,
                step=0.01,
                format="%.2f",
                key=f"weight_{asset}"
            )
            weights_dict[asset] = weight
        
        st.session_state.asset_weights = weights_dict
    
    with col2:
        st.markdown("### Status")
        
        # Calculate total weight
        total_weight = sum(weights_dict.values())
        
        # Validation
        is_valid = abs(total_weight - 100.0) < 0.01
        
        if is_valid:
            st.success(f"✅ Total: {total_weight:.2f}%")
        else:
            st.error(f"❌ Total: {total_weight:.2f}%")
            st.warning(f"Must equal 100%")
        
        st.markdown(f"**Number of Assets:** {len(selected_assets)}")
        st.markdown(f"**Equal Weight:** {100/len(selected_assets):.2f}% each")
    
    # Reset button
    if st.button("🔄 Reset to Equal Weights", use_container_width=True):
        equal_weight = 100.0 / len(selected_assets)
        st.session_state.asset_weights = {asset: equal_weight for asset in selected_assets}
        st.rerun()

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 4: OPTIMIZATION METHOD
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## 📈 STEP 4: OPTIMIZATION METHOD")
st.markdown("Choose your portfolio optimization approach:")

col1, col2 = st.columns([1.5, 1.5])

with col1:
    st.markdown("### Main Method")
    
    optimization_method = st.radio(
        "Select Optimization Method:",
        options=["Modern Portfolio Theory (MPT)", "Maximize Sharpe Ratio"],
        index=0 if st.session_state.optimization_method == "Modern Portfolio Theory (MPT)" else 1,
        key="main_optimization_method"
    )
    
    st.session_state.optimization_method = optimization_method
    
    # Show sub-options if MPT is selected
    if optimization_method == "Modern Portfolio Theory (MPT)":
        st.markdown("### MPT Objective")
        mpt_objective = st.radio(
            "Choose MPT Optimization Goal:",
            options=["Maximize Returns", "Minimize Risk"],
            index=0 if st.session_state.mpt_objective == "Maximize Returns" else 1,
            key="mpt_objective"
        )
        st.session_state.mpt_objective = mpt_objective
        
        # Show description
        if mpt_objective == "Maximize Returns":
            st.info("**Goal:** Highest expected annual return\n\n**Best for:** Growth-oriented investors\n\n**Focus:** Maximize annual return")
        else:
            st.info("**Goal:** Lowest portfolio volatility\n\n**Best for:** Risk-averse investors\n\n**Focus:** Minimize annual standard deviation")

with col2:
    st.markdown("### Risk-Free Rate")
    
    risk_free_rate = st.number_input(
        "Risk-Free Rate (%):",
        min_value=0.0,
        max_value=20.0,
        value=st.session_state.risk_free_rate,
        step=0.1,
        key="risk_free_rate_input"
    )
    st.session_state.risk_free_rate = risk_free_rate
    
    st.markdown("### Method Description")
    if optimization_method == "Maximize Sharpe Ratio":
        st.info("""
        **Goal:** Best risk-adjusted returns
        
        **Formula:** (Return - Risk-Free Rate) / Volatility
        
        **Best for:** Balanced investors seeking optimal return per unit of risk
        """)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# RUN OPTIMIZATION BUTTON
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("## ⚡ READY TO OPTIMIZE?")

# Check if all requirements met
can_run = (
    len(selected_assets) > 0 and
    abs(sum(weights_dict.values()) - 100.0) < 0.01
)

if can_run:
    if st.button("🚀 RUN OPTIMIZATION & GO TO RESULTS", use_container_width=True, key="run_optimization"):
        # Store data in session state
        st.session_state.portfolio_data = {
            'selected_assets': selected_assets,
            'asset_weights': weights_dict,
            'optimization_method': optimization_method,
            'mpt_objective': mpt_objective if optimization_method == "Modern Portfolio Theory (MPT)" else None,
            'risk_free_rate': risk_free_rate / 100.0,  # Convert to decimal
        }
        
        # Navigate to Results page
        st.switch_page("pages/2_📊_Results.py")
else:
    st.error("❌ Cannot run optimization. Please:")
    if len(selected_assets) == 0:
        st.write("1. Select at least one asset in Step 2")
    if abs(sum(weights_dict.values()) - 100.0) >= 0.01 if selected_assets else False:
        st.write("2. Ensure weights sum to exactly 100%")
