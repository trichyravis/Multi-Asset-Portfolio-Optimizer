
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
# MANUAL WEIGHT ADJUSTMENT (Percentage Input)
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚙️ ADJUST PORTFOLIO WEIGHTS</h2>
        <p style='color: #90EE90; margin: 0.5rem 0 0 0;'>Enter the percentage allocation for each asset (must total 100%)</p>
        <p style='color: #FFD700; margin: 0.5rem 0 0 0;'>💡 Values appear in gold boxes on the right side</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize weights in session state if not already done
if "asset_weights_adjusted" not in st.session_state or len(st.session_state.asset_weights_adjusted) == 0:
    st.session_state.asset_weights_adjusted = {asset: value for asset, value in st.session_state.selected_assets.items()}

# Create input fields for each asset in 2 columns with visible values
weights = {}
cols = st.columns(2)

for idx, asset in enumerate(selected_assets_list):
    col = cols[idx % 2]
    
    with col:
        # Get current weight
        current_weight = st.session_state.asset_weights_adjusted.get(asset, st.session_state.selected_assets.get(asset, 1.0/num_assets))
        
        # Create 3-column layout for better visibility
        input_col, display_col = st.columns([3, 1])
        
        with input_col:
            # Create a nice input field with validation
            weight_pct = st.number_input(
                f"📊 {asset} (%)",
                min_value=0.0,
                max_value=100.0,
                value=round(current_weight * 100, 2),
                step=0.1,
                key=f"input_{asset}",
                help=f"Enter percentage allocation for {asset}",
                label_visibility="visible"
            )
        
        with display_col:
            # Display the value prominently with high contrast
            st.markdown(f"""
            <div style='padding: 0.5rem; background-color: #FFD700; border-radius: 0.25rem; text-align: center; margin-top: 1.5rem;'>
                <p style='color: #003366; font-weight: bold; font-size: 1rem; margin: 0;'>{weight_pct:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        weights[asset] = weight_pct / 100.0

# ═══════════════════════════════════════════════════════════════════════════════
# VALIDATE WEIGHTS
# ═══════════════════════════════════════════════════════════════════════════════

total_weight = sum(weights.values())
total_pct = total_weight * 100

st.markdown("")

# ═══════════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE - ENTERED VALUES
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #FFD700; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;'>
        <h3 style='color: #003366; margin: 0;'>📊 YOUR ENTERED VALUES</h3>
    </div>
    """, unsafe_allow_html=True)

# Create a summary table with high contrast
summary_cols = st.columns(len(selected_assets_list))
for idx, asset in enumerate(selected_assets_list):
    with summary_cols[idx]:
        st.markdown(f"""
        <div style='background-color: #004d80; padding: 1rem; border-radius: 0.5rem; text-align: center; border: 2px solid #FFD700;'>
            <p style='color: #90EE90; margin: 0; font-size: 0.85rem;'>{asset}</p>
            <h2 style='color: #FFD700; margin: 0.5rem 0; font-size: 1.5rem;'>{weights[asset]*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)

# Display validation status
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 Total Weight", f"{total_pct:.2f}%", delta=f"{total_pct - 100:.2f}%" if total_pct != 100 else None)

with col2:
    if abs(total_pct - 100) < 0.01:
        st.success("✅ Valid (100%)")
    elif total_pct < 100:
        st.warning(f"⚠️ Under ({total_pct:.2f}%)")
    else:
        st.error(f"❌ Over ({total_pct:.2f}%)")

with col3:
    if st.button("🔄 Reset to Equal", help="Reset all weights to equal distribution", use_container_width=True):
        equal_weight = 1.0 / num_assets
        # Update session state with equal weights
        for asset in selected_assets_list:
            st.session_state.asset_weights_adjusted[asset] = equal_weight
            # Clear the widget input state to force reload from session state
            if f"input_{asset}" in st.session_state:
                del st.session_state[f"input_{asset}"]
        st.rerun()

with col4:
    if st.button("📋 Auto-Normalize", help="Automatically adjust to 100%", use_container_width=True):
        if total_weight > 0:
            # Normalize weights to sum to 100%
            for asset in selected_assets_list:
                normalized_weight = weights[asset] / total_weight
                st.session_state.asset_weights_adjusted[asset] = normalized_weight
                # Clear the widget input state to force reload from session state
                if f"input_{asset}" in st.session_state:
                    del st.session_state[f"input_{asset}"]
            st.rerun()
        else:
            st.error("❌ Cannot normalize - all weights are 0. Please enter values first.")

# ═══════════════════════════════════════════════════════════════════════════════
# WEIGHTS SUMMARY TABLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📋 WEIGHT SUMMARY & ALLOCATION</h2>
    </div>
    """, unsafe_allow_html=True)

# Create detailed dataframe for weights
weights_data = []
for asset, weight in weights.items():
    weights_data.append({
        "Asset": asset,
        "Weight %": f"{weight*100:.2f}%",
        "Amount ($1000)": f"${weight*1000:.2f}",
        "Amount ($10K)": f"${weight*10000:.2f}",
        "Amount ($100K)": f"${weight*100000:.2f}"
    })

df_weights = pd.DataFrame(weights_data)

st.dataframe(
    df_weights,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Asset": st.column_config.TextColumn("Asset", width="small"),
        "Weight %": st.column_config.TextColumn("Weight %", width="small"),
        "Amount ($1000)": st.column_config.TextColumn("If $1,000", width="small"),
        "Amount ($10K)": st.column_config.TextColumn("If $10,000", width="small"),
        "Amount ($100K)": st.column_config.TextColumn("If $100,000", width="small")
    }
)

# Show total in a nice box
st.markdown(f"""
    <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center; border: 2px solid #FFD700;'>
        <p style='color: white; margin: 0;'>Total Allocation</p>
        <h2 style='color: #FFD700; margin: 0.5rem 0;'>{total_pct:.2f}%</h2>
        <p style='color: #90EE90; margin: 0;'>{"✅ Perfect! Ready for analysis" if abs(total_pct - 100) < 0.01 else "⚠️ Please adjust to 100%"}</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SAVE & VALIDATE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("")

if total_pct < 99.9 or total_pct > 100.1:
    st.warning(f"""
    ⚠️ **Weights must total 100%**
    
    Current total: **{total_pct:.2f}%**
    
    **Options:**
    1. Manually adjust the percentages above
    2. Click "Auto-Normalize" button to automatically adjust to 100%
    3. Click "Reset to Equal" to start over with equal weights
    """)
else:
    # Update session state
    st.session_state.selected_assets = weights
    st.session_state.asset_weights_adjusted = weights
    
    st.markdown("")
    st.success(f"""
    ✅ **Weights Saved Successfully!**
    
    Total Allocation: **{total_pct:.2f}%**
    
    Your portfolio weights are ready for analysis!
    """)
    
    # Show quick summary
    st.info("💡 **Portfolio Summary:**")
    for asset, weight in weights.items():
        st.write(f"• **{asset}**: {weight*100:.2f}%")
    
    # Navigation buttons with breadcrumb
    st.markdown("")
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>🔄 NAVIGATION</h2>
        </div>
        """, unsafe_allow_html=True)
    
    nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])
    
    with nav_col1:
        st.markdown("""<div style='text-align: left;'>""", unsafe_allow_html=True)
        if st.button("← Back to Setup", key="weights_to_app", use_container_width=True, help="Go back to Setup page"):
            st.switch_page("app.py")
        st.markdown("""</div>""", unsafe_allow_html=True)
    
    with nav_col2:
        st.markdown("""
            <div style='text-align: center; padding: 0.75rem; background-color: #004d80; border-radius: 0.5rem;'>
                <p style='color: #FFD700; font-weight: bold; margin: 0;'>Step 2/6</p>
                <p style='color: #90EE90; font-size: 0.9rem; margin: 0.25rem 0 0 0;'>Weights</p>
            </div>
            """, unsafe_allow_html=True)
    
    with nav_col3:
        st.markdown("""<div style='text-align: right;'>""", unsafe_allow_html=True)
        if st.button("Next: Analysis →", key="weights_to_analysis", use_container_width=True, help="Go to Analysis page"):
            st.switch_page("pages/3_Analysis.py")
        st.markdown("""</div>""", unsafe_allow_html=True)
    
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
