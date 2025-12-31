
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
Multi-Asset Portfolio Optimizer - Main Application
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
import pandas as pd
from config_enhanced import PAGE_CONFIG, ASSET_STATS
from styles_enhanced import apply_main_styles, render_header, render_footer

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)

# ═══════════════════════════════════════════════════════════════════════════════
# APPLY STYLES & RENDER HEADER
# ═══════════════════════════════════════════════════════════════════════════════

apply_main_styles()
render_header()

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "investment_period" not in st.session_state:
    st.session_state.investment_period = 5
if "selected_asset_classes" not in st.session_state:
    st.session_state.selected_asset_classes = []
if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}

# Define asset classes and their assets
ASSET_CLASSES = {
    "Stocks": ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JPM", "BAC", "XOM", "PG", "KO"],
    "Bonds": ["BND", "AGG", "LQD", "TLT", "SHV"],
    "Commodities": ["GLD", "SLV", "USO", "DBC", "UUP"],
    "Cryptocurrencies": ["BTC", "ETH", "BNB", "ADA", "SOL"]
}

CLASS_DESCRIPTIONS = {
    "Stocks": "📈 Equity securities - Higher growth potential, higher volatility",
    "Bonds": "📊 Fixed income - Lower risk, stable returns",
    "Commodities": "🏆 Raw materials & metals - Portfolio diversification",
    "Cryptocurrencies": "⚡ Digital assets - High volatility, emerging class"
}

CLASS_EMOJIS = {
    "Stocks": "📈",
    "Bonds": "📊",
    "Commodities": "🏆",
    "Cryptocurrencies": "⚡"
}

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🏔️ Portfolio Optimizer</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Advanced Multi-Asset Portfolio Optimization</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: MODEL ASSUMPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚡ STEP 1: SET YOUR ASSUMPTIONS</h2>
        <p style='color: white;'>Configure risk-free rate and investment period:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    risk_free = st.slider(
        "💰 Risk-Free Rate (%)",
        min_value=0.1,
        max_value=10.0,
        value=st.session_state.risk_free_rate,
        step=0.1,
        help="Default: 4.5% (US Treasury 10Y)"
    )
    st.session_state.risk_free_rate = risk_free

with col2:
    period = st.slider(
        "📅 Investment Period (Years)",
        min_value=1,
        max_value=30,
        value=st.session_state.investment_period,
        step=1,
        help="Default: 5 years"
    )
    st.session_state.investment_period = period

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: SELECT ASSET CLASSES (MULTIPLE)
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 STEP 2: SELECT ASSET CLASSES</h2>
        <p style='color: white;'>Choose one or more categories for your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

# Multiple class selection with checkboxes
col1, col2, col3, col4 = st.columns(4)

selected_classes = []

with col1:
    if st.checkbox("📈 Stocks", value="Stocks" in st.session_state.selected_asset_classes):
        selected_classes.append("Stocks")

with col2:
    if st.checkbox("📊 Bonds", value="Bonds" in st.session_state.selected_asset_classes):
        selected_classes.append("Bonds")

with col3:
    if st.checkbox("🏆 Commodities", value="Commodities" in st.session_state.selected_asset_classes):
        selected_classes.append("Commodities")

with col4:
    if st.checkbox("⚡ Cryptocurrencies", value="Cryptocurrencies" in st.session_state.selected_asset_classes):
        selected_classes.append("Cryptocurrencies")

st.session_state.selected_asset_classes = selected_classes

# Show selected classes info in boxes
if selected_classes:
    st.markdown("")
    info_cols = st.columns(len(selected_classes))
    
    for idx, asset_class in enumerate(selected_classes):
        with info_cols[idx]:
            st.markdown(f"""
                <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
                    <p style='color: white; margin: 0;'><strong>{asset_class}</strong></p>
                    <p style='color: #FFD700; margin: 0.5rem 0 0 0; font-size: 0.85rem;'>{CLASS_DESCRIPTIONS[asset_class]}</p>
                </div>
                """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Please select at least one asset class to continue!")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 3: SELECT SPECIFIC ASSETS BY CLASS (2-6 TOTAL)
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🎯 STEP 3: SELECT SPECIFIC ASSETS</h2>
        <p style='color: white;'>Choose 2-6 assets from your selected classes:</p>
    </div>
    """, unsafe_allow_html=True)

# Display assets by class in boxes with checkboxes
selected_assets_list = []

for asset_class in selected_classes:
    st.markdown(f"""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 1rem 0;'>
            <h4 style='color: #FFD700; margin: 0;'>{CLASS_EMOJIS[asset_class]} {asset_class}</h4>
            <p style='color: white; font-size: 0.9rem; margin: 0.5rem 0 0 0;'>{CLASS_DESCRIPTIONS[asset_class]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Create columns for asset checkboxes (4 columns per row)
    assets_in_class = ASSET_CLASSES[asset_class]
    
    # Create rows of 4 columns
    for i in range(0, len(assets_in_class), 4):
        cols = st.columns(4)
        for j, col in enumerate(cols):
            if i + j < len(assets_in_class):
                asset = assets_in_class[i + j]
                with col:
                    # Check if asset was previously selected
                    is_checked = asset in st.session_state.selected_assets
                    if st.checkbox(
                        asset,
                        value=is_checked,
                        key=f"asset_{asset}"
                    ):
                        if asset not in selected_assets_list:
                            selected_assets_list.append(asset)
                    else:
                        # Remove from list if unchecked
                        if asset in selected_assets_list:
                            selected_assets_list.remove(asset)

# Validate selection
if len(selected_assets_list) < 2:
    st.error(f"⚠️ Please select at least 2 assets! (Currently selected: {len(selected_assets_list)})")
    st.stop()
elif len(selected_assets_list) > 6:
    st.error(f"⚠️ Please select at most 6 assets! (Currently selected: {len(selected_assets_list)})")
    st.stop()

# Initialize equal weights for selected assets
equal_weight = 1.0 / len(selected_assets_list)
selected_assets_dict = {asset: equal_weight for asset in selected_assets_list}
st.session_state.selected_assets = selected_assets_dict

# ═══════════════════════════════════════════════════════════════════════════════
# CURRENT SETTINGS DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🔧 YOUR CURRENT SETTINGS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Risk-Free Rate", f"{st.session_state.risk_free_rate:.2f}%")

with col2:
    st.metric("📅 Investment Period", f"{st.session_state.investment_period} years")

with col3:
    st.metric("🎯 Assets Selected", f"{len(selected_assets_list)}")

# Show selected assets and default weights
st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 1rem 0;'>
        <h3 style='color: #FFD700; margin-top: 0;'>📈 SELECTED ASSETS (Default Equal Weights)</h3>
    </div>
    """, unsafe_allow_html=True)

# Create dataframe for assets
assets_data = []
for asset in selected_assets_list:
    # Find which class this asset belongs to
    asset_class = ""
    for cls, assets in ASSET_CLASSES.items():
        if asset in assets:
            asset_class = cls
            break
    
    assets_data.append({
        "Asset": asset,
        "Default Weight": f"{equal_weight*100:.1f}%",
        "Class": asset_class
    })

df_assets = pd.DataFrame(assets_data)
st.dataframe(
    df_assets,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Asset": st.column_config.TextColumn("Asset", width="medium"),
        "Default Weight": st.column_config.TextColumn("Default Weight", width="medium"),
        "Class": st.column_config.TextColumn("Class", width="medium")
    }
)

# ═══════════════════════════════════════════════════════════════════════════════
# WORKFLOW GUIDE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🚀 NEXT STEPS</h2>
        <p style='color: white;'>You have completed Step 1-3. Continue with:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Step 4: Set Weights**
    - Go to sidebar → ⚖️ **Weights**
    - Adjust weights for each asset
    - Total must equal 100%
    """)

with col2:
    st.markdown("""
    **Step 5-7: Analyze & Optimize**
    - Go to 📊 **Analysis** → View current metrics
    - Go to 🎯 **Objective** → Choose goal
    - Go to 🚀 **Optimize** → Run optimization
    - Go to 📊 **Results** → View results
    """)

# Info boxes
st.markdown("")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    💡 **Next Step:** Go to **⚖️ Weights** page to adjust weights. Your assets are set to equal distribution (100% total) by default, and you can customize them.
    """)

with col2:
    if st.button("▶️ Go to Weights Page", key="go_to_weights", use_container_width=True):
        st.switch_page("pages/2_⚖️_Weights.py")

st.success(f"""
✅ **Setup Complete!** Your assumptions and asset selections are ready. All calculations will use your risk-free rate ({st.session_state.risk_free_rate:.2f}%) and investment period ({st.session_state.investment_period} years).
""")

render_footer()
