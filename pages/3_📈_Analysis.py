import streamlit as st
import plotly.graph_objects as go
from config_enhanced import PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer
from portfolio_analytics_enhanced import calculate_portfolio_metrics

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>📈 Portfolio Analysis</h1>
        <p style='color: #003366; font-size: 1.1rem;'>STEP 4: Pre-Optimization Analysis</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>📊 PRE-OPTIMIZATION ANALYSIS</h3>
        <p style='color: white;'>Analysis of your current portfolio before optimization:</p>
    </div>
    """, unsafe_allow_html=True)

selected_assets = list(st.session_state.get("selected_assets", {}).keys())
weights = st.session_state.get("portfolio_weights", {})

if not selected_assets or not weights:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white;'>👈 Please complete previous steps</p>
        </div>
        """, unsafe_allow_html=True)
else:
    try:
        metrics = calculate_portfolio_metrics(selected_assets, weights)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
                <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                    <p style='color: #FFD700; margin: 0;'>Annual Return</p>
                    <h3 style='color: white; margin: 0;'>{metrics['annual_return']*100:.2f}%</h3>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                    <p style='color: #FFD700; margin: 0;'>Volatility</p>
                    <h3 style='color: white; margin: 0;'>{metrics['volatility']*100:.2f}%</h3>
                </div>
                """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                    <p style='color: #FFD700; margin: 0;'>Sharpe Ratio</p>
                    <h3 style='color: white; margin: 0;'>{metrics['sharpe_ratio']:.2f}</h3>
                </div>
                """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
                <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                    <p style='color: #FFD700; margin: 0;'>Max Drawdown</p>
                    <h3 style='color: white; margin: 0;'>{metrics['max_drawdown']*100:.2f}%</h3>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("")
        st.markdown("""
            <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
                <h4 style='color: #FFD700; margin-top: 0;'>💼 Portfolio Composition:</h4>
            </div>
            """, unsafe_allow_html=True)
        
        fig = go.Figure(data=[go.Pie(
            labels=selected_assets,
            values=[weights.get(a, 0) for a in selected_assets],
            marker=dict(colors=['#003366', '#004d80', '#FFD700', '#FF6B6B', '#00D9FF'])
        )])
        fig.update_layout(
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(color='#333333')
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("➡️ NEXT: Choose Objective", use_container_width=True, type="primary"):
                st.switch_page("pages/4_🎯_Objective.py")
    
    except Exception as e:
        st.error(f"Error calculating metrics: {str(e)}")

render_footer()
