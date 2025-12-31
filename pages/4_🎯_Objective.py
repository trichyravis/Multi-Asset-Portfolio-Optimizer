import streamlit as st
from config_enhanced import PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

if "optimization_objective" not in st.session_state:
    st.session_state.optimization_objective = "Maximize Sharpe Ratio"

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🎯 Optimization Objective</h1>
        <p style='color: #003366; font-size: 1.1rem;'>STEP 5: Choose Your Optimization Strategy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>🎯 SELECT OPTIMIZATION OBJECTIVE</h3>
        <p style='color: white;'>Choose how to optimize your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

objectives = {
    "Maximize Sharpe Ratio": "⚖️ Balanced approach - Optimal risk-adjusted returns (RECOMMENDED)",
    "Minimize Risk": "🛡️ Conservative - Lowest volatility portfolio",
    "Maximize Return": "📈 Aggressive - Highest expected returns",
    "Equal Weight": "⚪ Simple - Equal distribution across assets"
}

selected = st.radio("Choose your optimization strategy:", list(objectives.keys()), label_visibility="collapsed")
st.session_state.optimization_objective = selected

st.markdown("")

st.markdown(f"""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h4 style='color: #FFD700; margin-top: 0;'>📌 Selected Strategy:</h4>
        <p style='color: white; font-size: 1.1rem;'>{selected}</p>
        <p style='color: #FFD700;'>{objectives[selected]}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("➡️ NEXT: Run Optimization", use_container_width=True, type="primary"):
        st.switch_page("pages/5_🚀_Optimize.py")

render_footer()
