"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
⚖️ Portfolio Weights Management
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
import pandas as pd
from config_enhanced import PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE & CHECK ASSETS
# ═══════════════════════════════════════════════════════════════════════════════

if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}
if "asset_weights_adjusted" not in st.session_state:
    st.session_state.asset_weights_adjusted = {}

# Check if assets are selected
if not st.session_state.selected_assets:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 style='color: #003366; font-size: 2.5rem; border: none;'>⚖️ Portfolio Weights</h1>
        </div>
        """, unsafe_allow_html=True)
    st.error("⚠️ No assets selected! Please go back to the main app and select assets first.")
    st.stop()

# Get selected assets
selected_assets_list = list(st.session_state.selected_assets.keys())
num_assets = len(selected_assets_list)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>⚖️ Portfolio Weights</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Adjust allocation for each asset (100% total)</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SELECTED ASSETS INFO
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown(f"""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 YOUR SELECTED ASSETS ({num_assets})</h2>
        <p style='color: white;'>Adjust the weight for each asset. Total must equal 100%:</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# WEIGHT ADJUSTMENT SLIDERS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown(f"""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚙️ ADJUST WEIGHTS</h2>
        <p style='color: white;'>Use sliders to set allocation. Total must equal 100%.</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize weights in session state if not already done
if "asset_weights_adjusted" not in st.session_state or len(st.session_state.asset_weights_adjusted) == 0:
    st.session_state.asset_weights_adjusted = {asset: value for asset, value in st.session_state.selected_assets.items()}

# Create sliders for each asset in 2 columns
weights = {}
cols = st.columns(2)

for idx, asset in enumerate(selected_assets_list):
    col = cols[idx % 2]
    
    with col:
        # Get current weight
        current_weight = st.session_state.asset_weights_adjusted.get(asset, st.session_state.selected_assets.get(asset, 1.0/num_assets))
        
        weight_pct = st.slider(
            f"📊 {asset}",
            min_value=0.0,
            max_value=100.0,
            value=current_weight * 100,
            step=0.1,
            key=f"slider_{asset}"
        )
        weights[asset] = weight_pct / 100.0

# ═══════════════════════════════════════════════════════════════════════════════
# VALIDATE WEIGHTS
# ═══════════════════════════════════════════════════════════════════════════════

total_weight = sum(weights.values())
total_pct = total_weight * 100

st.markdown("")

# Display metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📈 Total Weight", f"{total_pct:.1f}%")

with col2:
    if abs(total_pct - 100) < 0.01:
        st.success("✅ Valid (100%)")
    else:
        st.error(f"❌ Invalid ({total_pct:.1f}%)")

with col3:
    if st.button("🔄 Reset to Equal"):
        equal_weight = 1.0 / num_assets
        for asset in selected_assets_list:
            st.session_state.asset_weights_adjusted[asset] = equal_weight
        st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# WEIGHTS TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📋 WEIGHT SUMMARY</h2>
    </div>
    """, unsafe_allow_html=True)

# Create dataframe for weights
weights_data = []
for asset, weight in weights.items():
    weights_data.append({
        "Asset": asset,
        "Weight": f"{weight*100:.1f}%",
        "Amount (if $1000)": f"${weight*1000:.2f}"
    })

df_weights = pd.DataFrame(weights_data)
st.dataframe(
    df_weights,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Asset": st.column_config.TextColumn("Asset", width="medium"),
        "Weight": st.column_config.TextColumn("Weight", width="medium"),
        "Amount (if $1000)": st.column_config.TextColumn("Amount", width="medium")
    }
)

# ═══════════════════════════════════════════════════════════════════════════════
# SAVE & VALIDATE
# ═══════════════════════════════════════════════════════════════════════════════

if total_pct < 99.9 or total_pct > 100.1:
    st.warning(f"⚠️ Weights don't sum to 100% (currently {total_pct:.1f}%). Please adjust!")
else:
    # Update session state
    st.session_state.selected_assets = weights
    st.session_state.asset_weights_adjusted = weights
    
    st.markdown("")
    st.success(f"""
    ✅ **Weights Saved!** Total = {total_pct:.1f}%
    
    Your portfolio allocation is ready for analysis.
    """)
    
    # Navigation info
    st.markdown("")
    st.info("""
    📊 **Next Step:** Go to sidebar → 📊 **Analysis** to view your current portfolio metrics.
    """)
    
    # Next steps
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>🚀 NEXT STEPS</h2>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Step 5: Analyze Portfolio**
        - Go to sidebar → 📊 **Analysis**
        - View current portfolio metrics
        """)
    
    with col2:
        st.markdown("""
        **Step 6-7: Optimize**
        - Go to 🎯 **Objective** → Choose goal
        - Go to 🚀 **Optimize** → Run optimization
        - Go to 📊 **Results** → View optimized
        """)

render_footer()
