
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
# CUSTOM SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.5rem;'>
        <h3 style='color: #FFD700; margin-top: 0; font-size: 1.3rem;'>📚 About This Tool</h3>
        <p style='color: white; margin: 0.8rem 0; font-size: 0.95rem; line-height: 1.6;'>
            Multi-Asset Portfolio Optimizer using Modern Portfolio Theory and advanced optimization algorithms.
        </p>
        <p style='color: white; margin: 0.8rem 0; font-size: 0.95rem; line-height: 1.6;'>
            <strong style='color: #FFD700;'>Key Features:</strong>
        </p>
        <ul style='color: white; margin: 0.5rem 0 0 1rem; font-size: 0.9rem; line-height: 1.8;'>
            <li>📊 Multi-asset class optimization</li>
            <li>🎯 Risk-return analysis</li>
            <li>📈 Sharpe ratio maximization</li>
            <li>⚖️ Efficient frontier calculation</li>
            <li>💼 Portfolio rebalancing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: #004d80; margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem;'>
        <h3 style='color: #FFD700; margin-top: 0; font-size: 1.3rem;'>👨‍🏫 Creator</h3>
        <p style='color: white; margin: 1rem 0 0.5rem 0; font-size: 1.1rem; font-weight: bold;'>
            Prof. V. Ravichandran
        </p>
        <p style='color: #FFD700; margin: 0.3rem 0; font-size: 0.85rem; font-weight: 600;'>
            ✨ 28+ Years Corporate Finance & Banking
        </p>
        <p style='color: #FFD700; margin: 0.3rem 0 1rem 0; font-size: 0.85rem; font-weight: 600;'>
            ✨ 10+ Years Academic Excellence
        </p>
        <p style='color: #90EE90; margin: 0.5rem 0; font-size: 0.85rem; line-height: 1.5;'>
            Specializing in Advanced Financial Risk Management, Portfolio Optimization, and Quantitative Finance.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("""
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='https://www.linkedin.com/in/trichyravis' target='_blank' style='text-decoration: none;'>
            <button style='
                background-color: #0A66C2; 
                color: white; 
                padding: 0.6rem 1.5rem; 
                border: none; 
                border-radius: 0.4rem; 
                font-weight: 600; 
                font-size: 0.9rem;
                cursor: pointer;
                width: 100%;
            '>
                🔗 LinkedIn Profile
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# INITIALIZE SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

# Initialize required state variables
if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}
if "asset_weights_adjusted" not in st.session_state:
    st.session_state.asset_weights_adjusted = {}
if "weights_validated" not in st.session_state:
    st.session_state.weights_validated = False

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
    # Tech Giants
    "AAPL": {"return": 28.5, "volatility": 32.1}, "MSFT": {"return": 26.3, "volatility": 28.9},
    "GOOGL": {"return": 24.7, "volatility": 30.2}, "AMZN": {"return": 22.1, "volatility": 34.5},
    "NVDA": {"return": 35.2, "volatility": 45.8}, "META": {"return": 25.8, "volatility": 38.4},
    "INTC": {"return": 18.9, "volatility": 31.5}, "AMD": {"return": 22.4, "volatility": 42.1},
    
    # Financial Services
    "JPM": {"return": 15.3, "volatility": 25.6}, "BAC": {"return": 12.5, "volatility": 28.3},
    "WFC": {"return": 11.8, "volatility": 27.5}, "GS": {"return": 14.2, "volatility": 29.8},
    "V": {"return": 19.5, "volatility": 24.3}, "MA": {"return": 20.1, "volatility": 25.6},
    "PYPL": {"return": 16.8, "volatility": 38.2},
    
    # Healthcare & Pharma
    "JNJ": {"return": 10.2, "volatility": 18.4}, "UNH": {"return": 17.6, "volatility": 22.1},
    "PFE": {"return": 8.9, "volatility": 21.3}, "LLY": {"return": 14.3, "volatility": 20.2},
    "ABBV": {"return": 12.7, "volatility": 19.8},
    
    # Consumer & Retail
    "PG": {"return": 9.7, "volatility": 16.8}, "KO": {"return": 7.3, "volatility": 18.2},
    "PEP": {"return": 8.5, "volatility": 17.3}, "HD": {"return": 13.2, "volatility": 21.5},
    "MCD": {"return": 10.8, "volatility": 19.2}, "COST": {"return": 11.5, "volatility": 20.1},
    "WMT": {"return": 9.3, "volatility": 17.8},
    
    # Energy & Utilities
    "XOM": {"return": 8.9, "volatility": 22.4}, "CVX": {"return": 8.2, "volatility": 23.1},
    "SO": {"return": 6.5, "volatility": 14.2},
    
    # Media & Entertainment
    "NFLX": {"return": 20.3, "volatility": 42.8}, "DIS": {"return": 12.4, "volatility": 26.3},
    
    # Transportation & Other
    "TSLA": {"return": 32.1, "volatility": 58.3}, "BA": {"return": 9.8, "volatility": 29.4},
    
    # Bonds
    "BND": {"return": 4.2, "volatility": 6.3}, "AGG": {"return": 4.5, "volatility": 6.8},
    "LQD": {"return": 5.1, "volatility": 7.4}, "TLT": {"return": 3.8, "volatility": 8.9},
    "SHV": {"return": 3.2, "volatility": 2.1},
    
    # Commodities
    "GLD": {"return": 6.5, "volatility": 14.2}, "SLV": {"return": 5.8, "volatility": 18.6},
    "USO": {"return": 3.2, "volatility": 22.1}, "DBC": {"return": 2.1, "volatility": 19.8},
    "UUP": {"return": 1.5, "volatility": 8.3},
    
    # Cryptocurrencies
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
    # VALUE AT RISK (VAR) ANALYSIS - 95% CONFIDENCE LEVEL
    # ═══════════════════════════════════════════════════════════════════════════════

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h2 style='color: #FFD700; margin-top: 0;'>⚠️ VALUE AT RISK (VAR) - OPTIMIZED PORTFOLIO</h2>
        </div>
        """, unsafe_allow_html=True)

    # VAR calculation at 95% confidence level
    # Z-score for 95% confidence level (one-tailed) = 1.645
    z_score_95 = 1.645
    
    # Calculate VAR for optimized portfolio
    opt_var_95 = opt_vol * z_score_95
    current_var_95 = current_vol * z_score_95
    
    # VAR improvement (lower VAR is better)
    var_improvement = ((current_var_95 - opt_var_95) / current_var_95 * 100) if current_var_95 != 0 else 0
    
    # Create columns for VAR metrics
    var_col1, var_col2, var_col3 = st.columns(3)
    
    with var_col1:
        st.metric(
            "Optimized Portfolio VAR",
            f"-{opt_var_95:.2f}%",
            delta=f"Annual loss @ 95% confidence",
            delta_color="off"
        )
    
    with var_col2:
        st.metric(
            "Current Portfolio VAR",
            f"-{current_var_95:.2f}%",
            delta=f"Annual loss @ 95% confidence",
            delta_color="off"
        )
    
    with var_col3:
        st.metric(
            "VAR Reduction",
            f"{var_improvement:+.2f}%",
            delta="Risk reduction from optimization",
            delta_color="inverse"
        )
    
    # Detailed VAR explanation
    st.markdown("""
    <div style='background-color: #004d80; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;'>
        <h3 style='color: #FFD700; margin-top: 0;'>📖 VAR Interpretation at 95% Confidence Level</h3>
        <p style='color: white; margin: 0.8rem 0; font-size: 0.95rem; line-height: 1.6;'>
            <strong style='color: #FFD700;'>Optimized Portfolio VAR:</strong> With 95% confidence, the portfolio's annual loss 
            will not exceed <strong style='color: #FFD700;'>{:.2f}%</strong> under normal market conditions.
        </p>
        <p style='color: white; margin: 0.8rem 0; font-size: 0.95rem; line-height: 1.6;'>
            This means there is only a <strong style='color: #FFD700;'>5% probability</strong> of experiencing 
            losses greater than this amount in any given year.
        </p>
        <p style='color: white; margin: 0.8rem 0; font-size: 0.95rem; line-height: 1.6;'>
            <strong style='color: #FFD700;'>Example:</strong> On a $1,000,000 portfolio, the maximum expected loss 
            with 95% confidence would be <strong style='color: #FFD700;'>${:.2f}</strong> annually.
        </p>
    </div>
    """.format(opt_var_95, opt_var_95 * 10000), unsafe_allow_html=True)
    
    # VAR comparison table
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📊 VAR COMPARISON TABLE</h3>
        </div>
        """, unsafe_allow_html=True)
    
    var_comparison_data = {
        'Metric': [
            'Annual Return (%)',
            'Annual Volatility (%)',
            'Value at Risk @ 95% (%)',
            'Sharpe Ratio',
            'Risk per Unit Return'
        ],
        'Current Portfolio': [
            f'{current_return:.2f}',
            f'{current_vol:.2f}',
            f'{current_var_95:.2f}',
            f'{current_sharpe:.3f}',
            f'{current_vol / current_return:.3f}' if current_return > 0 else '∞'
        ],
        'Optimized Portfolio': [
            f'{opt_return:.2f}',
            f'{opt_vol:.2f}',
            f'{opt_var_95:.2f}',
            f'{opt_sharpe:.3f}',
            f'{opt_vol / opt_return:.3f}' if opt_return > 0 else '∞'
        ]
    }
    
    var_df = pd.DataFrame(var_comparison_data)
    
    # Display table with custom styling
    st.markdown(var_df.to_html(index=False), unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # VAR VISUALIZATIONS
    # ═══════════════════════════════════════════════════════════════════════════════

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📈 VAR DISTRIBUTION ANALYSIS</h3>
        </div>
        """, unsafe_allow_html=True)

    # Create two columns for visualizations
    var_viz_col1, var_viz_col2 = st.columns(2)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # VISUALIZATION 1: NORMAL DISTRIBUTION WITH VAR THRESHOLD
    # ═════════════════════════════════════════════════════════════════════════════
    
    with var_viz_col1:
        fig_dist, ax_dist = plt.subplots(figsize=(10, 6))
        
        # Generate normal distribution data
        x = np.linspace(-6, 4, 1000)
        y = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
        
        # Plot normal distribution
        ax_dist.plot(x, y, color='#FFD700', linewidth=2.5, label='Normal Distribution')
        ax_dist.fill_between(x, y, alpha=0.3, color='#FFD700')
        
        # Mark VAR threshold (at -1.645 for 95% confidence)
        var_z_score = -1.645
        ax_dist.axvline(var_z_score, color='#E74C3C', linestyle='--', linewidth=2.5, label='VAR @ 95% Confidence')
        
        # Shade the tail (5% area)
        x_tail = x[x <= var_z_score]
        y_tail = y[:len(x_tail)]
        ax_dist.fill_between(x_tail, y_tail, alpha=0.7, color='#E74C3C', label='5% Tail Risk')
        
        # Formatting
        ax_dist.set_xlabel('Standard Deviations (σ)', fontsize=11, color='white', fontweight='bold')
        ax_dist.set_ylabel('Probability Density', fontsize=11, color='white', fontweight='bold')
        ax_dist.set_title('Portfolio Return Distribution @ 95% Confidence', 
                         fontsize=12, color='#FFD700', fontweight='bold', pad=15)
        ax_dist.legend(loc='upper right', fontsize=10, facecolor='#003366', 
                      edgecolor='#FFD700', labelcolor='white')
        ax_dist.set_facecolor('#003366')
        ax_dist.grid(True, alpha=0.2, color='white')
        ax_dist.tick_params(colors='white', labelsize=10)
        
        # Add text annotation
        ax_dist.text(var_z_score - 0.5, max(y) * 0.7, f'VAR = {opt_var_95:.2f}%\n(Max Loss)', 
                    fontsize=10, color='white', bbox=dict(boxstyle='round', 
                    facecolor='#E74C3C', alpha=0.8, edgecolor='#FFD700', linewidth=2))
        
        # Set spine colors
        for spine in ax_dist.spines.values():
            spine.set_color('#FFD700')
            spine.set_linewidth(1.5)
        
        st.pyplot(fig_dist)
        st.markdown("""
        <p style='color: white; font-size: 0.9rem; text-align: center; margin-top: -10px;'>
        <strong style='color: #FFD700;'>Interpretation:</strong> The red shaded area represents 5% tail risk. 
        The portfolio can lose {:.2f}% with 95% confidence.
        </p>
        """.format(opt_var_95), unsafe_allow_html=True)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # VISUALIZATION 2: VAR COMPARISON BAR CHART
    # ═════════════════════════════════════════════════════════════════════════════
    
    with var_viz_col2:
        fig_comp, ax_comp = plt.subplots(figsize=(10, 6))
        
        portfolios = ['Current\nPortfolio', 'Optimized\nPortfolio']
        var_values = [current_var_95, opt_var_95]
        colors = ['#FF6B6B', '#2ECC71']
        
        # Create bar chart
        bars = ax_comp.bar(portfolios, var_values, color=colors, alpha=0.8, 
                          edgecolor='#FFD700', linewidth=2.5, width=0.6)
        
        # Add value labels on bars
        for i, (bar, value) in enumerate(zip(bars, var_values)):
            height = bar.get_height()
            ax_comp.text(bar.get_x() + bar.get_width()/2., height,
                        f'-{value:.2f}%',
                        ha='center', va='bottom', fontsize=12, color='white', 
                        fontweight='bold',
                        bbox=dict(boxstyle='round', facecolor=colors[i], alpha=0.9, 
                                edgecolor='#FFD700', linewidth=1.5))
        
        # Add improvement line
        if var_improvement > 0:
            ax_comp.plot([0, 1], [current_var_95, opt_var_95], 'o--', 
                        color='#FFD700', linewidth=2.5, markersize=8, label='Risk Reduction')
            mid_point = (current_var_95 + opt_var_95) / 2
            ax_comp.text(0.5, mid_point, f'↓ {var_improvement:.1f}%', 
                        ha='center', fontsize=11, color='#2ECC71', fontweight='bold',
                        bbox=dict(boxstyle='round', facecolor='#003366', 
                                edgecolor='#2ECC71', linewidth=2))
        
        # Formatting
        ax_comp.set_ylabel('Value at Risk (%)', fontsize=11, color='white', fontweight='bold')
        ax_comp.set_title('VAR Comparison: Current vs Optimized', 
                         fontsize=12, color='#FFD700', fontweight='bold', pad=15)
        ax_comp.set_facecolor('#003366')
        ax_comp.set_ylim(0, max(var_values) * 1.2)
        ax_comp.grid(True, alpha=0.2, axis='y', color='white')
        ax_comp.tick_params(colors='white', labelsize=10)
        
        # Set spine colors
        for spine in ax_comp.spines.values():
            spine.set_color('#FFD700')
            spine.set_linewidth(1.5)
        
        st.pyplot(fig_comp)
        st.markdown("""
        <p style='color: white; font-size: 0.9rem; text-align: center; margin-top: -10px;'>
        <strong style='color: #FFD700;'>Result:</strong> Optimization reduces portfolio risk by {:.2f}% at 95% confidence level.
        </p>
        """.format(var_improvement), unsafe_allow_html=True)
    
    # ═════════════════════════════════════════════════════════════════════════════
    # VISUALIZATION 3: RISK PROFILE COMPARISON
    # ═════════════════════════════════════════════════════════════════════════════

    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0 1rem 0;'>
            <h3 style='color: #FFD700; margin-top: 0;'>📊 RISK METRICS COMPARISON</h3>
        </div>
        """, unsafe_allow_html=True)
    
    fig_risk, ax_risk = plt.subplots(figsize=(12, 6))
    
    # Create grouped bar chart for all metrics
    metrics_labels = ['Return\n(%)', 'Volatility\n(%)', 'VAR @ 95%\n(%)', 'Sharpe\nRatio']
    current_metrics = [current_return, current_vol, current_var_95, current_sharpe * 10]  # Scale Sharpe for visibility
    optimized_metrics = [opt_return, opt_vol, opt_var_95, opt_sharpe * 10]
    
    x = np.arange(len(metrics_labels))
    width = 0.35
    
    bars1 = ax_risk.bar(x - width/2, current_metrics, width, label='Current Portfolio',
                       color='#FF6B6B', alpha=0.8, edgecolor='#FFD700', linewidth=1.5)
    bars2 = ax_risk.bar(x + width/2, optimized_metrics, width, label='Optimized Portfolio',
                       color='#2ECC71', alpha=0.8, edgecolor='#FFD700', linewidth=1.5)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax_risk.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.2f}',
                        ha='center', va='bottom', fontsize=9, color='white', fontweight='bold')
    
    ax_risk.set_ylabel('Value', fontsize=11, color='white', fontweight='bold')
    ax_risk.set_title('Complete Risk Profile Comparison', 
                     fontsize=12, color='#FFD700', fontweight='bold', pad=15)
    ax_risk.set_xticks(x)
    ax_risk.set_xticklabels(metrics_labels, fontsize=10, color='white', fontweight='bold')
    ax_risk.legend(loc='upper left', fontsize=10, facecolor='#003366', 
                  edgecolor='#FFD700', labelcolor='white', framealpha=0.95)
    ax_risk.set_facecolor('#003366')
    ax_risk.grid(True, alpha=0.2, axis='y', color='white')
    ax_risk.tick_params(colors='white', labelsize=10)
    
    # Set spine colors
    for spine in ax_risk.spines.values():
        spine.set_color('#FFD700')
        spine.set_linewidth(1.5)
    
    st.pyplot(fig_risk)
    st.markdown("""
    <p style='color: white; font-size: 0.9rem; text-align: center; margin-top: -10px;'>
    <strong style='color: #FFD700;'>Note:</strong> Sharpe Ratio scaled by 10 for chart visibility. 
    Lower VAR and volatility indicate better risk-adjusted returns.
    </p>
    """, unsafe_allow_html=True)
    
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
