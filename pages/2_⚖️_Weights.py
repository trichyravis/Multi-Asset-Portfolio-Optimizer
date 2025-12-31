import streamlit as st
from config_enhanced import ASSET_STATS, PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

if "portfolio_weights" not in st.session_state:
    st.session_state.portfolio_weights = {}

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>⚖️ Allocate Weights</h1>
        <p style='color: #003366; font-size: 1.1rem;'>STEP 3: Portfolio Weight Distribution</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>⚖️ STEP 3: ALLOCATE PORTFOLIO WEIGHTS</h3>
        <p style='color: white;'>Distribute your investment across selected assets. Weights must sum to 100%.</p>
    </div>
    """, unsafe_allow_html=True)

selected_assets = list(st.session_state.get("selected_assets", {}).keys())

if not selected_assets:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white;'>👈 Please select assets first</p>
        </div>
        """, unsafe_allow_html=True)
else:
    for asset in selected_assets:
        if asset not in st.session_state.portfolio_weights:
            st.session_state.portfolio_weights[asset] = 1.0 / len(selected_assets) * 100
    
    st.markdown("""
        <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1.5rem;'>
            <h4 style='color: #FFD700; margin: 0;'>📊 Adjust Asset Weights:</h4>
        </div>
        """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    for idx, asset in enumerate(selected_assets):
        col = cols[idx % 2]
        with col:
            st.markdown(f"""
                <div style='background-color: #004d80; padding: 0.75rem; border-radius: 0.25rem; margin-bottom: 0.5rem;'>
                    <p style='color: white; margin: 0;'>{ASSET_STATS[asset].get('emoji', '📊')} {asset}</p>
                </div>
                """, unsafe_allow_html=True)
            
            weight = st.slider(
                f"Weight", min_value=0.0, max_value=100.0, value=st.session_state.portfolio_weights[asset],
                step=0.1, label_visibility="collapsed", key=f"weight_{asset}"
            )
            st.session_state.portfolio_weights[asset] = weight
    
    total_weight = sum(st.session_state.portfolio_weights.values())
    st.markdown("")
    
    if abs(total_weight - 100.0) < 0.01:
        color = "#FFD700"
        status = "✅ Perfect! Weights sum to 100%"
    else:
        color = "#FFD700"
        status = f"⚠️ {total_weight:.2f}% - Adjust to reach 100%"
    
    st.markdown(f"""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
            <h4 style='color: {color}; margin-top: 0;'>Total Weight: {total_weight:.2f}%</h4>
            <p style='color: {color};'>{status}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if abs(total_weight - 100.0) < 0.1:
            if st.button("➡️ NEXT: View Analysis", width='stretch', type="primary"):
                st.switch_page("pages/3_📈_Analysis.py")
        else:
            st.button("➡️ NEXT: View Analysis", width='stretch', disabled=True)

render_footer()
