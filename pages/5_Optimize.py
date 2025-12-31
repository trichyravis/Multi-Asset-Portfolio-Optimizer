
"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE
🚀 Portfolio Optimization - Run Optimization
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from config_enhanced import PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()
render_header()

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "optimized_weights" not in st.session_state:
    st.session_state.optimized_weights = {}
if "risk_free_rate" not in st.session_state:
    st.session_state.risk_free_rate = 4.5
if "optimization_objective" not in st.session_state:
    st.session_state.optimization_objective = "Maximize Sharpe Ratio"
if "run_optimization" not in st.session_state:
    st.session_state.run_optimization = False

# ═══════════════════════════════════════════════════════════════════════════════
# ASSET DATA
# ═══════════════════════════════════════════════════════════════════════════════

ASSET_DATA = {
    "AAPL": {"return": 28.5, "volatility": 32.1}, "MSFT": {"return": 26.3, "volatility": 28.9},
    "GOOGL": {"return": 24.7, "volatility": 30.2}, "AMZN": {"return": 22.1, "volatility": 34.5},
    "NVDA": {"return": 35.2, "volatility": 45.8}, "JPM": {"return": 15.3, "volatility": 25.6},
    "BAC": {"return": 12.5, "volatility": 28.3}, "XOM": {"return": 8.9, "volatility": 22.4},
    "PG": {"return": 9.7, "volatility": 16.8}, "KO": {"return": 7.3, "volatility": 18.2},
    "BND": {"return": 4.2, "volatility": 6.3}, "AGG": {"return": 4.5, "volatility": 6.8},
    "LQD": {"return": 5.1, "volatility": 7.4}, "TLT": {"return": 3.8, "volatility": 8.9},
    "SHV": {"return": 3.2, "volatility": 2.1}, "GLD": {"return": 6.5, "volatility": 14.2},
    "SLV": {"return": 5.8, "volatility": 18.6}, "USO": {"return": 3.2, "volatility": 22.1},
    "DBC": {"return": 2.1, "volatility": 19.8}, "UUP": {"return": 1.5, "volatility": 8.3},
    "BTC": {"return": 65.3, "volatility": 78.5}, "ETH": {"return": 58.2, "volatility": 82.3},
    "BNB": {"return": 52.1, "volatility": 88.2}, "ADA": {"return": 45.3, "volatility": 92.4},
    "SOL": {"return": 48.9, "volatility": 95.1},
}

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🚀 Run Optimization</h1>
        <p style='color: #003366; font-size: 1.1rem;'>Execute portfolio optimization</p>
    </div>
    """, unsafe_allow_html=True)

# Check if assets are selected
if not st.session_state.selected_assets:
    st.error("⚠️ No assets selected! Please go back and select assets first.")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZATION EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>⚙️ OPTIMIZATION PARAMETERS</h2>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Objective", st.session_state.optimization_objective)

with col2:
    st.metric("🎯 Assets", len(st.session_state.selected_assets))

with col3:
    st.metric("💰 Risk-Free Rate", f"{st.session_state.risk_free_rate:.2f}%")

# ═══════════════════════════════════════════════════════════════════════════════
# RUN OPTIMIZATION BUTTON
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
        <h2 style='color: #FFD700; margin-top: 0;'>🚀 EXECUTE OPTIMIZATION</h2>
    </div>
    """, unsafe_allow_html=True)

run_button_col1, run_button_col2, run_button_col3 = st.columns([1, 2, 1])

with run_button_col2:
    if st.button("▶️ RUN OPTIMIZATION NOW", key="run_opt_button", use_container_width=True, help="Click to run portfolio optimization with your selected objective"):
        st.session_state.run_optimization = True

# Only run if button was clicked
if st.session_state.get("run_optimization", False):
    
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>🔄 OPTIMIZATION IN PROGRESS...</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Run optimization based on objective
    selected_assets_list = list(st.session_state.selected_assets.keys())
    current_weights = list(st.session_state.selected_assets.values())

    # Calculate metrics for current portfolio
    current_return = sum(current_weights[i] * ASSET_DATA[asset]["return"] 
                         for i, asset in enumerate(selected_assets_list) if asset in ASSET_DATA)
    current_vol = np.sqrt(sum((current_weights[i] ** 2) * (ASSET_DATA[asset]["volatility"] ** 2) 
                               for i, asset in enumerate(selected_assets_list) if asset in ASSET_DATA))
    current_sharpe = (current_return - st.session_state.risk_free_rate) / current_vol if current_vol > 0 else 0

    # Optimization
    if st.session_state.optimization_objective == "Maximize Sharpe Ratio":
        # Allocate more to high sharpe ratio assets
        sharpe_ratios = {}
        for asset in selected_assets_list:
            if asset in ASSET_DATA:
                sharpe = (ASSET_DATA[asset]["return"] - st.session_state.risk_free_rate) / ASSET_DATA[asset]["volatility"]
                sharpe_ratios[asset] = max(sharpe, 0)
        
        total_sharpe = sum(sharpe_ratios.values())
        if total_sharpe > 0:
            optimized_weights = {asset: sharpe_ratios[asset] / total_sharpe for asset in selected_assets_list}
        else:
            optimized_weights = {asset: 1.0 / len(selected_assets_list) for asset in selected_assets_list}

    elif st.session_state.optimization_objective == "Minimize Risk":
        # Allocate inversely to volatility
        inv_vols = {}
        for asset in selected_assets_list:
            if asset in ASSET_DATA:
                inv_vols[asset] = 1.0 / ASSET_DATA[asset]["volatility"]
        
        total_inv_vol = sum(inv_vols.values())
        optimized_weights = {asset: inv_vols[asset] / total_inv_vol for asset in selected_assets_list}

    elif st.session_state.optimization_objective == "Maximize Return":
        # Allocate 100% to highest return asset
        max_asset = max(selected_assets_list, 
                        key=lambda x: ASSET_DATA[x]["return"] if x in ASSET_DATA else 0)
        optimized_weights = {asset: (1.0 if asset == max_asset else 0.0) for asset in selected_assets_list}

    else:  # Equal Weight
        optimized_weights = {asset: 1.0 / len(selected_assets_list) for asset in selected_assets_list}

    # Calculate optimized metrics
    opt_return = sum(optimized_weights[asset] * ASSET_DATA[asset]["return"] 
                     for asset in selected_assets_list if asset in ASSET_DATA)
    opt_vol = np.sqrt(sum((optimized_weights[asset] ** 2) * (ASSET_DATA[asset]["volatility"] ** 2) 
                           for asset in selected_assets_list if asset in ASSET_DATA))
    opt_sharpe = (opt_return - st.session_state.risk_free_rate) / opt_vol if opt_vol > 0 else 0

    st.session_state.optimized_weights = optimized_weights

    # Display success message
    st.success("""
    ✅ **Optimization Complete!**

    Optimization has been executed successfully using your selected objective.
    """)

    # ═══════════════════════════════════════════════════════════════════════════════
    # IMPROVEMENT METRICS
    # ═══════════════════════════════════════════════════════════════════════════════

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>📈 OPTIMIZATION RESULTS</h2>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    improvement_return = ((opt_return - current_return) / current_return * 100) if current_return != 0 else 0
    improvement_sharpe = ((opt_sharpe - current_sharpe) / current_sharpe * 100) if current_sharpe != 0 else 0

    with col1:
        st.metric(
            "Return Improvement",
            f"{improvement_return:+.2f}%",
            delta=f"{opt_return - current_return:.2f}%"
        )

    with col2:
        st.metric(
            "Volatility Change",
            f"{opt_vol:.2f}%",
            delta=f"{opt_vol - current_vol:.2f}%"
        )

    with col3:
        st.metric(
            "Sharpe Improvement",
            f"{improvement_sharpe:+.2f}%",
            delta=f"{opt_sharpe - current_sharpe:.3f}"
        )

    # ═══════════════════════════════════════════════════════════════════════════════
    # EFFICIENT FRONTIER VISUALIZATION
    # ═══════════════════════════════════════════════════════════════════════════════

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>📊 EFFICIENT FRONTIER</h2>
        </div>
        """, unsafe_allow_html=True)

    # Generate efficient frontier by simulating random portfolios
    np.random.seed(42)
    num_simulations = 5000
    selected_assets_list = list(st.session_state.selected_assets.keys())
    num_assets = len(selected_assets_list)

    # Store simulation results
    frontier_returns = []
    frontier_vols = []
    frontier_sharpes = []

    for _ in range(num_simulations):
        # Random weights
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        
        # Calculate portfolio metrics
        port_return = sum(weights[i] * ASSET_DATA[selected_assets_list[i]]["return"] 
                          for i in range(num_assets) if selected_assets_list[i] in ASSET_DATA)
        port_vol = np.sqrt(sum((weights[i] ** 2) * (ASSET_DATA[selected_assets_list[i]]["volatility"] ** 2) 
                                for i in range(num_assets) if selected_assets_list[i] in ASSET_DATA))
        port_sharpe = (port_return - st.session_state.risk_free_rate) / port_vol if port_vol > 0 else 0
        
        frontier_returns.append(port_return)
        frontier_vols.append(port_vol)
        frontier_sharpes.append(port_sharpe)

    # Create Efficient Frontier plot
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot all simulated portfolios
    scatter = ax.scatter(frontier_vols, frontier_returns, c=frontier_sharpes, 
                         cmap='viridis', alpha=0.5, s=30, label='Simulated Portfolios')

    # Plot current portfolio
    ax.scatter(current_vol, current_return, color='orange', s=200, marker='o', 
              edgecolors='black', linewidth=2, label='Current Portfolio', zorder=5)

    # Plot optimized portfolio
    ax.scatter(opt_vol, opt_return, color='lime', s=200, marker='*', 
              edgecolors='black', linewidth=2, label='Optimized Portfolio', zorder=5)

    # Plot Capital Allocation Line (CAL)
    max_vol_for_cal = max(frontier_vols) * 1.2
    cal_vols = np.linspace(0, max_vol_for_cal, 100)
    risk_free_rate = st.session_state.risk_free_rate

    if opt_sharpe > 0:
        cal_returns = risk_free_rate + opt_sharpe * cal_vols
        ax.plot(cal_vols, cal_returns, 'r--', linewidth=2, label='Capital Allocation Line', zorder=4)

    # Risk-free rate point
    ax.scatter(0, risk_free_rate, color='red', s=150, marker='D', 
              edgecolors='black', linewidth=2, label='Risk-Free Rate', zorder=5)

    # Formatting
    ax.set_xlabel('Portfolio Volatility (Risk) %', fontsize=12, fontweight='bold')
    ax.set_ylabel('Expected Return %', fontsize=12, fontweight='bold')
    ax.set_title('Efficient Frontier - Portfolio Optimization', fontsize=14, fontweight='bold', color='#003366')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('white')

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Sharpe Ratio', fontweight='bold')

    st.pyplot(fig)

    # Add explanation
    st.markdown("""
    **Efficient Frontier Explanation:**

    - **Orange Circle (●)** = Your current portfolio allocation
    - **Green Star (★)** = Your optimized portfolio (based on selected objective)
    - **Red Diamond (◆)** = Risk-free rate (4.5% with zero volatility)
    - **Colored Dots** = Other possible portfolio allocations (simulated)
    - **Red Dashed Line** = Capital Allocation Line (optimal risk-return trade-off)

    The optimized portfolio should be on or near the efficient frontier, representing the best risk-adjusted returns for your chosen objective.
    """)

    # ═══════════════════════════════════════════════════════════════════════════════
    # NEXT STEPS
    # ═══════════════════════════════════════════════════════════════════════════════

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>🎯 NEXT STEPS</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>🔄 NAVIGATION</h2>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("← Back to Objective", key="optimize_to_objective", use_container_width=True, help="Go back to Objective"):
            st.switch_page("pages/4_Objective.py")

    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 0.75rem; background-color: #004d80; border-radius: 0.5rem;'>
                <p style='color: #FFD700; font-weight: bold; margin: 0;'>Step 5/6</p>
                <p style='color: #90EE90; font-size: 0.9rem; margin: 0.25rem 0 0 0;'>Optimize</p>
            </div>
            """, unsafe_allow_html=True)

    with col3:
        if st.button("Next: Results →", key="optimize_to_results", use_container_width=True, help="Go to Results"):
            st.switch_page("pages/6_Results.py")

else:
    # Show message if optimization hasn't been run
    st.markdown("""
        <div style='background-color: #FFE6E6; padding: 2rem; border-radius: 0.5rem; text-align: center; margin: 2rem 0;'>
            <h3 style='color: #CC0000; margin-top: 0;'>⏳ Ready to Optimize</h3>
            <p style='color: #333; font-size: 1.1rem;'>Click the <strong>"▶️ RUN OPTIMIZATION NOW"</strong> button above to execute the optimization with your selected objective.</p>
            <p style='color: #666; margin: 1rem 0 0 0;'><strong>Your Selection:</strong><br>
            Objective: <span style='color: #003366; font-weight: bold;'>{}</span></p>
        </div>
        """.format(st.session_state.optimization_objective), unsafe_allow_html=True)

render_footer()
