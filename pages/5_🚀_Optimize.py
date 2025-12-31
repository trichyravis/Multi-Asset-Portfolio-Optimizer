import streamlit as st
from config_enhanced import PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer
from portfolio_analytics_enhanced import optimize_portfolio, calculate_portfolio_metrics

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

if "optimized_weights" not in st.session_state:
    st.session_state.optimized_weights = {}

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🚀 Optimize Portfolio</h1>
        <p style='color: #003366; font-size: 1.1rem;'>STEP 6: Running Optimization Algorithm</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>🚀 OPTIMIZE PORTFOLIO</h3>
        <p style='color: white;'>Running optimization with your selected strategy...</p>
    </div>
    """, unsafe_allow_html=True)

selected_assets = list(st.session_state.get("selected_assets", {}).keys())
weights = st.session_state.get("portfolio_weights", {})
objective = st.session_state.get("optimization_objective", "Maximize Sharpe Ratio")

if not selected_assets or not weights:
    st.markdown("""
        <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white;'>👈 Please complete previous steps</p>
        </div>
        """, unsafe_allow_html=True)
else:
    try:
        with st.spinner("⏳ Running optimization..."):
            initial_metrics = calculate_portfolio_metrics(selected_assets, weights)
            optimized_weights_dict = optimize_portfolio(selected_assets, objective)
            optimized_metrics = calculate_portfolio_metrics(selected_assets, optimized_weights_dict)
            
            st.session_state.optimized_weights = optimized_weights_dict
            
            st.markdown("""
                <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; text-align: center; margin-bottom: 2rem;'>
                    <h3 style='color: #FFD700; margin-top: 0;'>✅ Optimization Complete!</h3>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                ret_change = ((optimized_metrics['annual_return'] - initial_metrics['annual_return']) / initial_metrics['annual_return'] * 100)
                st.markdown(f"""
                    <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                        <p style='color: #FFD700; margin: 0;'>Return</p>
                        <p style='color: white; font-size: 1.2rem;'>{initial_metrics['annual_return']*100:.2f}% → {optimized_metrics['annual_return']*100:.2f}%</p>
                        <p style='color: #FFD700; margin: 0;'>{ret_change:+.1f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                vol_change = ((optimized_metrics['volatility'] - initial_metrics['volatility']) / initial_metrics['volatility'] * 100)
                st.markdown(f"""
                    <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                        <p style='color: #FFD700; margin: 0;'>Risk</p>
                        <p style='color: white; font-size: 1.2rem;'>{initial_metrics['volatility']*100:.2f}% → {optimized_metrics['volatility']*100:.2f}%</p>
                        <p style='color: #FFD700; margin: 0;'>{vol_change:+.1f}%</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col3:
                sharpe_change = optimized_metrics['sharpe_ratio'] - initial_metrics['sharpe_ratio']
                st.markdown(f"""
                    <div style='background-color: #003366; padding: 1rem; border-radius: 0.5rem; text-align: center;'>
                        <p style='color: #FFD700; margin: 0;'>Sharpe Ratio</p>
                        <p style='color: white; font-size: 1.2rem;'>{initial_metrics['sharpe_ratio']:.2f} → {optimized_metrics['sharpe_ratio']:.2f}</p>
                        <p style='color: #FFD700; margin: 0;'>{sharpe_change:+.2f}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("➡️ NEXT: View Results", use_container_width=True, type="primary"):
                    st.switch_page("pages/6_📊_Results.py")
    
    except Exception as e:
        st.error(f"Error during optimization: {str(e)}")

render_footer()
