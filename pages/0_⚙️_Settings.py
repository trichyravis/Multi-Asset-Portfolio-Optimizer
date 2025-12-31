"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - MODEL ASSUMPTIONS & SETTINGS
Detailed Configuration for Portfolio Optimization
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
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>⚙️ Model Assumptions</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Configure optimization parameters and view assumptions</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state if not already done
if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "investment_period" not in st.session_state:
    st.session_state.investment_period = 5

# Main assumptions section
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📊 PORTFOLIO OPTIMIZATION ASSUMPTIONS</h2>
        <p style='color: white;'>Configure the key parameters for your portfolio analysis:</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Risk-Free Rate Setting
with col1:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>💰 Risk-Free Rate</h3>
            <p style='color: white; font-size: 0.95rem;'>
                The return on a risk-free investment (typically US Treasury rate).
                Used in calculating Sharpe Ratio and risk-adjusted returns.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    risk_free = st.slider(
        "Risk-Free Rate (%)",
        min_value=0.1,
        max_value=10.0,
        value=st.session_state.risk_free_rate,
        step=0.1,
        help="Current US Treasury 10-Year Rate typically ranges 1-5%"
    )
    st.session_state.risk_free_rate = risk_free
    
    st.markdown(f"""
        <div style='background-color: #1a5f7a; padding: 1rem; border-radius: 0.3rem; margin-top: 1rem;'>
            <p style='color: #FFD700; margin: 0; font-size: 1.1rem; font-weight: bold;'>{risk_free:.2f}%</p>
            <p style='color: white; margin: 0.5rem 0 0 0; font-size: 0.85rem;'>Current Setting</p>
        </div>
        """, unsafe_allow_html=True)

# Investment Period Setting
with col2:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📅 Investment Period</h3>
            <p style='color: white; font-size: 0.95rem;'>
                Your intended investment horizon in years.
                Affects risk tolerance and portfolio recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    period = st.slider(
        "Investment Period (Years)",
        min_value=1,
        max_value=30,
        value=st.session_state.investment_period,
        step=1,
        help="Longer periods allow for higher volatility tolerance"
    )
    st.session_state.investment_period = period
    
    st.markdown(f"""
        <div style='background-color: #1a5f7a; padding: 1rem; border-radius: 0.3rem; margin-top: 1rem;'>
            <p style='color: #FFD700; margin: 0; font-size: 1.1rem; font-weight: bold;'>{period} Year(s)</p>
            <p style='color: white; margin: 0.5rem 0 0 0; font-size: 0.85rem;'>Current Setting</p>
        </div>
        """, unsafe_allow_html=True)

# Detailed Assumptions Section
st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📈 ASSET ASSUMPTIONS</h2>
        <p style='color: white;'>Historical annual returns and volatility used in calculations:</p>
    </div>
    """, unsafe_allow_html=True)

# Asset returns and volatility table
asset_assumptions_html = """
<div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem;'>
    <table style='width: 100%; border-collapse: collapse;'>
        <thead>
            <tr style='background-color: #004d80;'>
                <th style='color: #FFD700; padding: 1rem; text-align: left; border-bottom: 2px solid #FFD700;'>Asset</th>
                <th style='color: #FFD700; padding: 1rem; text-align: center; border-bottom: 2px solid #FFD700;'>Annual Return</th>
                <th style='color: #FFD700; padding: 1rem; text-align: center; border-bottom: 2px solid #FFD700;'>Volatility</th>
                <th style='color: #FFD700; padding: 1rem; text-align: center; border-bottom: 2px solid #FFD700;'>Sharpe Ratio</th>
            </tr>
        </thead>
        <tbody>
"""

for asset, stats in ASSET_STATS.items():
    return_pct = stats.get('return', 0) * 100
    volatility_pct = stats.get('volatility', 0) * 100
    sharpe = (stats.get('return', 0) - (st.session_state.risk_free_rate / 100)) / stats.get('volatility', 0.01) if stats.get('volatility', 0) > 0 else 0
    
    asset_assumptions_html += f"""
            <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.2);'>
                <td style='color: white; padding: 1rem; text-align: left;'>
                    <strong>{stats.get('emoji', '📊')} {asset}</strong>
                </td>
                <td style='color: #90EE90; padding: 1rem; text-align: center; font-weight: bold;'>
                    {return_pct:.2f}%
                </td>
                <td style='color: #FFB6C1; padding: 1rem; text-align: center; font-weight: bold;'>
                    {volatility_pct:.2f}%
                </td>
                <td style='color: #FFD700; padding: 1rem; text-align: center; font-weight: bold;'>
                    {sharpe:.2f}
                </td>
            </tr>
    """

asset_assumptions_html += """
        </tbody>
    </table>
</div>
"""

st.markdown(asset_assumptions_html, unsafe_allow_html=True)

# Calculation Methodology Section
st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🔧 CALCULATION METHODOLOGY</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h4 style='color: #FFD700; margin-top: 0;'>📊 Sharpe Ratio</h4>
            <p style='color: white; font-size: 0.9rem;'>
                <strong>Formula:</strong><br/>
                (Portfolio Return - Risk-Free Rate) / Portfolio Volatility
            </p>
            <p style='color: #90EE90; font-size: 0.85rem; margin-top: 1rem;'>
                <strong>Higher = Better</strong><br/>
                Risk-adjusted return metric
            </p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h4 style='color: #FFD700; margin-top: 0;'>📈 Sortino Ratio</h4>
            <p style='color: white; font-size: 0.9rem;'>
                <strong>Formula:</strong><br/>
                (Portfolio Return - Risk-Free Rate) / Downside Volatility
            </p>
            <p style='color: #90EE90; font-size: 0.85rem; margin-top: 1rem;'>
                <strong>Penalizes downside only</strong><br/>
                Focuses on negative volatility
            </p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
            <h4 style='color: #FFD700; margin-top: 0;'>💡 Optimization</h4>
            <p style='color: white; font-size: 0.9rem;'>
                <strong>Objectives:</strong><br/>
                • Maximize Sharpe Ratio<br/>
                • Minimize Volatility<br/>
                • Maximize Return
            </p>
            <p style='color: #90EE90; font-size: 0.85rem; margin-top: 1rem;'>
                <strong>Constraints:</strong><br/>
                Sum of weights = 100%
            </p>
        </div>
        """, unsafe_allow_html=True)

# Key Assumptions and Limitations
st.markdown("")
st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; margin-top: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚠️ KEY ASSUMPTIONS & LIMITATIONS</h2>
    </div>
    """, unsafe_allow_html=True)

assumptions_html = """
<div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem;'>
    <h4 style='color: #FFD700; margin-top: 0;'>Key Assumptions:</h4>
    <ul style='color: white; font-size: 0.95rem; line-height: 1.8;'>
        <li><strong>Historical Data:</strong> Asset returns and volatility based on historical performance</li>
        <li><strong>Risk-Free Rate:</strong> Currently set to {:.2f}% (adjustable in this page)</li>
        <li><strong>Investment Period:</strong> {:.0f} year(s) horizon (adjustable in this page)</li>
        <li><strong>Correlation:</strong> Simplified correlation model for volatility calculation</li>
        <li><strong>No Constraints:</strong> Assumes weights can range from 0-100% per asset</li>
        <li><strong>Rebalancing:</strong> Annual rebalancing to maintain target weights</li>
        <li><strong>No Costs:</strong> Does not account for transaction costs or fees</li>
        <li><strong>Taxes:</strong> Tax implications not considered in optimization</li>
    </ul>

    <h4 style='color: #FFD700; margin-top: 2rem;'>Limitations:</h4>
    <ul style='color: #FFB6C1; font-size: 0.95rem; line-height: 1.8;'>
        <li>Past performance does not guarantee future results</li>
        <li>Asset correlations may change during market stress</li>
        <li>Black swan events and tail risks not fully captured</li>
        <li>Model assumes normal distribution of returns</li>
        <li>Results are estimates based on historical data</li>
        <li>For educational purposes - consult financial advisor before investing</li>
    </ul>
</div>
""".format(st.session_state.risk_free_rate, st.session_state.investment_period)

st.markdown(assumptions_html, unsafe_allow_html=True)

# Info box
st.markdown("""
    <div style='background-color: #1a5f7a; padding: 1.5rem; border-radius: 0.5rem; margin-top: 2rem; border-left: 5px solid #FFD700;'>
        <p style='color: white; margin: 0;'>
            💡 <strong>Tip:</strong> Adjust the Risk-Free Rate and Investment Period above to match your 
            specific circumstances. These settings will be used throughout the portfolio optimization process.
        </p>
    </div>
    """, unsafe_allow_html=True)

render_footer()
