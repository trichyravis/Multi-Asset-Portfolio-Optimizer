"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - HOME
Multi-Asset Portfolio Optimizer - Asset Selection & Quick Settings
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
from config_enhanced import PAGE_CONFIG, ASSET_STATS
from styles_enhanced import apply_main_styles, render_header, render_footer

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🏠 Portfolio Optimizer</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Select assets and configure model assumptions</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state for assumptions if not already done
if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "investment_period" not in st.session_state:
    st.session_state.investment_period = 5
if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}

# Quick Model Assumptions Section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>⚡ QUICK MODEL ASSUMPTIONS</h3>
        <p style='color: white;'>Set key parameters or go to Settings page for detailed configuration:</p>
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
        help="Currently ~4.5% (US Treasury 10Y). Adjust based on current market rates."
    )
    st.session_state.risk_free_rate = risk_free

with col2:
    period = st.slider(
        "📅 Investment Period (Years)",
        min_value=1,
        max_value=30,
        value=st.session_state.investment_period,
        step=1,
        help="Your investment horizon. Longer periods allow higher risk tolerance."
    )
    st.session_state.investment_period = period

# Settings link
st.markdown("""
    <div style='background-color: #1a5f7a; padding: 1rem; border-radius: 0.5rem; margin-bottom: 2rem; border-left: 5px solid #FFD700;'>
        <p style='color: white; margin: 0;'>
            📖 <strong>View detailed assumptions:</strong> Go to <strong>⚙️ Settings</strong> page to see asset details and calculation methodology.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Asset Selection Section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>📊 SELECT ASSETS</h3>
        <p style='color: white;'>Choose assets for your portfolio (minimum 2, maximum 6):</p>
    </div>
    """, unsafe_allow_html=True)

# Create asset selection in a grid
cols = st.columns(3)
selected_assets = {}

for idx, (asset, stats) in enumerate(ASSET_STATS.items()):
    col_idx = idx % 3
    
    with cols[col_idx]:
        asset_selected = st.checkbox(
            f"{stats['emoji']} {asset}",
            value=asset in st.session_state.selected_assets,
            help=f"Return: {stats['return']*100:.1f}% | Volatility: {stats['volatility']*100:.1f}%"
        )
        if asset_selected:
            selected_assets[asset] = st.session_state.selected_assets.get(asset, 100 / len(ASSET_STATS))

st.session_state.selected_assets = selected_assets

# Validation
num_assets = len(selected_assets)

if num_assets < 2:
    st.warning("⚠️ Please select at least 2 assets to proceed")
elif num_assets > 6:
    st.error("❌ Maximum 6 assets allowed. Please deselect some assets.")
else:
    # Asset Summary Table
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📈 SELECTED ASSETS SUMMARY</h3>
        </div>
        """, unsafe_allow_html=True)
    
    assets_summary_html = """
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem;'>
        <table style='width: 100%; border-collapse: collapse;'>
            <thead>
                <tr style='background-color: #004d80;'>
                    <th style='color: #FFD700; padding: 1rem; text-align: left; border-bottom: 2px solid #FFD700;'>Asset</th>
                    <th style='color: #FFD700; padding: 1rem; text-align: center; border-bottom: 2px solid #FFD700;'>Annual Return</th>
                    <th style='color: #FFD700; padding: 1rem; text-align: center; border-bottom: 2px solid #FFD700;'>Volatility</th>
                    <th style='color: #FFD700; padding: 1rem; text-align: center; border-bottom: 2px solid #FFD700;'>Category</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for asset in selected_assets.keys():
        stats = ASSET_STATS[asset]
        assets_summary_html += f"""
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.2);'>
                    <td style='color: white; padding: 1rem; text-align: left;'>
                        <strong>{stats['emoji']} {asset}</strong>
                    </td>
                    <td style='color: #90EE90; padding: 1rem; text-align: center;'>
                        {stats['return']*100:.2f}%
                    </td>
                    <td style='color: #FFB6C1; padding: 1rem; text-align: center;'>
                        {stats['volatility']*100:.2f}%
                    </td>
                    <td style='color: #FFD700; padding: 1rem; text-align: center;'>
                        {stats.get('category', 'Asset')}
                    </td>
                </tr>
        """
    
    assets_summary_html += """
            </tbody>
        </table>
    </div>
    """
    
    st.markdown(assets_summary_html, unsafe_allow_html=True)
    
    # Current Assumptions Display
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🔧 ACTIVE ASSUMPTIONS</h3>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
                <p style='color: #FFD700; margin: 0;'>Risk-Free Rate</p>
                <p style='color: white; font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0 0 0;'>{st.session_state.risk_free_rate:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
                <p style='color: #FFD700; margin: 0;'>Investment Period</p>
                <p style='color: white; font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0 0 0;'>{st.session_state.investment_period} Year(s)</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
                <p style='color: #FFD700; margin: 0;'>Assets Selected</p>
                <p style='color: white; font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0 0 0;'>{num_assets}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Next Steps
    st.markdown("")
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🚀 NEXT STEPS</h3>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⚖️ Set Initial Weights", use_container_width=True):
            st.switch_page("pages/2_⚖️_Weights.py")
    
    with col2:
        if st.button("🎯 Choose Objective", use_container_width=True):
            st.switch_page("pages/4_🎯_Objective.py")
    
    with col3:
        if st.button("⚙️ View Settings", use_container_width=True):
            st.switch_page("pages/0_⚙️_Settings.py")

render_footer()
