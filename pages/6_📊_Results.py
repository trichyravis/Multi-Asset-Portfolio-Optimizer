
import streamlit as st
import plotly.graph_objects as go
from config_enhanced import PAGE_CONFIG, ASSET_STATS
from styles_enhanced import apply_main_styles, render_header, render_footer
from portfolio_analytics_enhanced import plot_efficient_frontier_2d, calculate_portfolio_metrics

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>📊 Results</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Portfolio Optimization Results</p>
    </div>
    """, unsafe_allow_html=True)

selected_assets = list(st.session_state.get("selected_assets", {}).keys())
initial_weights = st.session_state.get("portfolio_weights", {})
optimized_weights = st.session_state.get("optimized_weights", {})
objective = st.session_state.get("optimization_objective", "Maximize Sharpe Ratio")

if not selected_assets or not initial_weights or not optimized_weights:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white;'>👈 Please complete optimization first</p>
        </div>
        """, unsafe_allow_html=True)
else:
    try:
        initial_metrics = calculate_portfolio_metrics(selected_assets, initial_weights)
        optimized_metrics = calculate_portfolio_metrics(selected_assets, optimized_weights)
        
        st.markdown("""
            <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
                <h3 style='color: #FFD700; margin-top: 0;'>📈 EFFICIENT FRONTIER ANALYSIS</h3>
                <p style='color: white;'>2D visualization showing the relationship between risk (volatility) and expected return:</p>
            </div>
            """, unsafe_allow_html=True)
        
        fig = plot_efficient_frontier_2d(selected_assets, initial_weights, optimized_weights)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("")
        
        st.markdown("""
            <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
                <h3 style='color: #FFD700; margin-top: 0;'>📊 OPTIMIZATION SUMMARY</h3>
                <p style='color: white;'>Comparison of Initial vs Optimized Portfolio:</p>
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
                <div style='background-color: #004d80; padding: 1rem; border-radius: 0.5rem;'>
                    <p style='color: #FFD700; margin: 0;'>Annual Return</p>
                    <p style='color: white;'><strong>Before:</strong> {initial_metrics['annual_return']*100:.2f}%</p>
                    <p style='color: white;'><strong>After:</strong> {optimized_metrics['annual_return']*100:.2f}%</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style='background-color: #004d80; padding: 1rem; border-radius: 0.5rem;'>
                    <p style='color: #FFD700; margin: 0;'>Volatility (Risk)</p>
                    <p style='color: white;'><strong>Before:</strong> {initial_metrics['volatility']*100:.2f}%</p>
                    <p style='color: white;'><strong>After:</strong> {optimized_metrics['volatility']*100:.2f}%</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div style='background-color: #004d80; padding: 1rem; border-radius: 0.5rem;'>
                    <p style='color: #FFD700; margin: 0;'>Sharpe Ratio</p>
                    <p style='color: white;'><strong>Before:</strong> {initial_metrics['sharpe_ratio']:.2f}</p>
                    <p style='color: white;'><strong>After:</strong> {optimized_metrics['sharpe_ratio']:.2f}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
                <div style='background-color: #004d80; padding: 1rem; border-radius: 0.5rem;'>
                    <p style='color: #FFD700; margin: 0;'>Max Drawdown</p>
                    <p style='color: white;'><strong>Before:</strong> {initial_metrics['max_drawdown']*100:.2f}%</p>
                    <p style='color: white;'><strong>After:</strong> {optimized_metrics['max_drawdown']*100:.2f}%</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("")
        
        st.markdown("""
            <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
                <h3 style='color: #FFD700; margin-top: 0;'>💡 OPTIMAL WEIGHTS</h3>
                <p style='color: white;'>Recommended asset allocation:</p>
            </div>
            """, unsafe_allow_html=True)
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=selected_assets,
            values=[optimized_weights.get(a, 0) for a in selected_assets],
            marker=dict(colors=['#003366', '#004d80', '#FFD700', '#FF6B6B', '#00D9FF', '#00FF88'])
        )])
        fig_pie.update_layout(
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(color='#333333')
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
        st.markdown("")
        
        st.markdown("""
            <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
                <h4 style='color: #FFD700; margin: 0;'>📋 Weight Details:</h4>
            </div>
            """, unsafe_allow_html=True)
        
        # Build weight details HTML
        weight_details_html = """
            <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem;'>
        """
        
        for asset in selected_assets:
            initial = initial_weights.get(asset, 0)
            optimized = optimized_weights.get(asset, 0)
            change = optimized - initial
            
            weight_details_html += f"""
                <div style='background-color: #004d80; color: white; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; border-left: 4px solid #FFD700;'>
                    <div style='display: flex; justify-content: space-between; align-items: center;'>
                        <strong style='color: white; font-size: 1.05rem;'>{ASSET_STATS[asset].get('emoji', '📊')} {asset}</strong>
                        <div style='text-align: right; color: white; font-size: 0.95rem;'>
                            <span>Before: <span style='color: #FFD700; font-weight: bold;'>{initial:.2f}%</span></span> | 
                            <span>After: <span style='color: #90EE90; font-weight: bold;'>{optimized:.2f}%</span></span> | 
                            <span>Change: <span style='color: #FFB6C1; font-weight: bold;'>{change:+.2f}%</span></span>
                        </div>
                    </div>
                </div>
            """
        
        weight_details_html += "</div>"
        
        st.markdown(weight_details_html, unsafe_allow_html=True)
        
        st.markdown("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Restart", width='stretch'):
                st.session_state.clear()
                st.switch_page("pages/1_🏠_Home.py")
        
        with col2:
            if st.button("⚖️ Adjust Weights", width='stretch'):
                st.switch_page("pages/2_⚖️_Weights.py")
        
        with col3:
            if st.button("🎯 Change Objective", width='stretch'):
                st.switch_page("pages/4_🎯_Objective.py")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")

render_footer()
