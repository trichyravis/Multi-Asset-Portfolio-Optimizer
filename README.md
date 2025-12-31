# 🏔️ Multi-Asset Portfolio Optimization App

**Production-Ready Streamlit Application for Professional Portfolio Management**

Portfolio optimization using Modern Portfolio Theory, risk analytics, and real-time market data from Yahoo Finance.

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [User Guide](#user-guide)
6. [Asset Classes](#asset-classes)
7. [Optimization Methods](#optimization-methods)
8. [Metrics Explained](#metrics-explained)
9. [Technical Details](#technical-details)
10. [Customization](#customization)
11. [FAQ](#faq)

## 🎯 Overview

This application provides professional-grade portfolio optimization for multi-asset portfolios including:
- Indian equities and indices
- US equity futures
- Commodities futures
- Currency pairs
- Cryptocurrencies

Built with Streamlit for interactive analysis, Plotly for visualizations, and scipy for optimization algorithms.

### Key Capabilities

✅ **6 Asset Classes**: 20+ tradeable assets
✅ **Real-Time Data**: Yahoo Finance integration
✅ **3 Optimization Methods**: Max Return, Min Risk, Max Sharpe
✅ **Advanced Metrics**: Sharpe, Sortino, Calmar, VaR, Information Ratio
✅ **Visualizations**: Efficient frontier, correlation matrix, performance analysis
✅ **Comparative Analysis**: Original vs Optimized portfolio comparison
✅ **Professional Design**: Mountain Path branding with high-contrast UI

## ✨ Features

### Portfolio Analysis
- **Efficient Frontier Visualization**: See all possible risk-return combinations
- **Portfolio Metrics**: 8+ risk and return metrics
- **Asset Correlation**: Heatmap showing how assets move together
- **Performance Backtest**: Historical performance comparison
- **Risk Analysis**: VaR, expected shortfall, maximum drawdown

### Optimization
- **Maximum Returns**: Aggressive strategy maximizing portfolio return
- **Minimum Risk**: Conservative strategy minimizing volatility
- **Maximum Sharpe Ratio**: Balanced strategy optimizing risk-adjusted returns (Recommended)

### User Interface
- **5 Interactive Tabs**: Metrics, Frontier, Weights, Performance, Risk Analysis
- **High-Contrast Inputs**: Radio buttons, sliders, dropdowns optimized for readability
- **Responsive Design**: Works on desktop, tablet, mobile
- **Professional Styling**: Dark blue + gold Mountain Path branding

### Data & Calculations
- **3-Month History**: Up to 90 days for futures expiry constraints
- **Auto Equal-Weight Initialization**: Default allocation before optimization
- **Comprehensive Metrics**: Return, volatility, Sharpe, Sortino, Calmar ratios
- **Covariance Calculation**: Accurate risk modeling
- **Constraint Optimization**: SLSQP algorithm ensuring valid weights

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download Files
```bash
# Copy all files to a directory
mkdir portfolio-optimizer
cd portfolio-optimizer
# Copy config.py, styles.py, portfolio_optimizer.py, portfolio_analytics.py,
# portfolio_comparative_analysis.py, and requirements.txt here
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Packages installed:**
- `streamlit==1.28.1` - Web app framework
- `pandas==2.1.1` - Data manipulation
- `numpy==1.24.3` - Numerical computing
- `scipy==1.11.3` - Optimization algorithms
- `yfinance==0.2.33` - Financial data
- `plotly==5.17.0` - Interactive charts

### Step 3: Verify Installation
```bash
streamlit --version  # Should show 1.28.1 or higher
python -c "import yfinance; print('yfinance OK')"
```

## 🎬 Quick Start

### Run the Application
```bash
streamlit run portfolio_optimizer.py
```

The app will:
1. Start a local server
2. Open in your default browser at `http://localhost:8501`
3. Display the portfolio optimizer interface

### First Portfolio Optimization

1. **Select Time Period**: Drag to 60-90 days
2. **Choose Asset Classes**: Select 2-3 classes
3. **Pick Assets**: Select 3-5 specific assets
4. **Set Risk-Free Rate**: Use default (6%) or adjust
5. **Pick Optimization Method**: Choose "Maximum Sharpe Ratio" (recommended)
6. **Click "🚀 Fetch Data & Optimize"**

Results appear in 5-10 seconds with:
- Portfolio metrics and asset contributions
- Efficient frontier visualization
- Optimal weight allocation
- Performance backtest
- Risk analysis

## 📚 User Guide

### Input Controls (Sidebar)

#### Step 1: Lookback Period
```
Range: 30-90 days
Default: 90 days (3 months)
Recommendation: 60-90 days for stable metrics
Purpose: Historical data window for analysis
```

#### Step 2: Asset Classes
```
Available:
- 🇮🇳 Indian Equities
- 📈 Indian Indices
- 🇺🇸 US Indices Futures
- 🏆 Commodities Futures
- 💱 Currency Futures
- ₿ Cryptocurrencies

Recommendation: Select 2-3 classes for diversification
```

#### Step 3: Asset Selection
```
For each selected class, choose specific assets
Example:
- From Indian Equities: RELIANCE, TCS, INFY
- From Indices: ^NSEI (Nifty 50)
- From Commodities: GC=F (Gold)

Total assets: 2-10 recommended
```

#### Step 4: Risk-Free Rate
```
Range: 0-10%
Default: 6% (India RBI policy rate)
Used for: Sharpe ratio and Sortino ratio calculation
Adjust if: Different borrowing rate, country, scenario
```

#### Step 5: Optimization Method
```
Three options:

1. 🚀 Maximum Returns
   - Objective: Maximize portfolio return
   - Risk: Highest among three
   - Use when: Aggressive strategy desired
   - Location: Upper right of efficient frontier

2. 🛡️ Minimum Risk (MVP)
   - Objective: Minimize portfolio volatility
   - Return: Usually lowest among three
   - Use when: Conservative strategy desired
   - Location: Lower left of efficient frontier

3. ⚡ Maximum Sharpe Ratio (RECOMMENDED)
   - Objective: Maximize risk-adjusted returns
   - Formula: (Return - Risk-Free) / Volatility
   - Use when: Most situations, best theory-backed choice
   - Location: Highest point on efficient frontier
```

### Output Tabs

#### Tab 1: 📊 Metrics
**Portfolio Performance Metrics:**
- Annual Return: Expected yearly return (%)
- Volatility: Portfolio standard deviation (%)
- Sharpe Ratio: Risk-adjusted return metric
- Sortino Ratio: Downside risk metric

**Asset Composition:**
- Ticker: Asset symbol
- Weight (%): Allocation percentage
- Annual Return (%): Individual asset return
- Contribution (%): Asset's contribution to portfolio return

#### Tab 2: ⭐ Efficient Frontier
**Components:**
- **Blue Curve**: Efficient frontier showing all optimal portfolios
- **Individual Points**: Component assets
- **Gold Star (★)**: Your optimized portfolio

**Interpretation:**
- Curve shows risk-return tradeoff
- Every portfolio on curve is "efficient"
- Portfolios below curve are suboptimal
- Your portfolio (gold star) is optimal for selected method

#### Tab 3: 🎯 Portfolio Weights
**Pie Chart:**
- Visual representation of allocation
- Color-coded by weight (gold = large, blue = small)

**Allocation Table:**
- Ticker: Asset symbol
- Weight (%): Percentage allocation
- Allocation: Decimal weight (must sum to 1.0)

#### Tab 4: 📈 Performance
**Cumulative Returns Chart:**
- Orange line: Portfolio performance
- Lighter lines: Individual assets
- Shows: Historical "what if" scenario

#### Tab 5: 🔍 Risk Analysis
**Correlation Matrix Heatmap:**
- Values from -1 to +1
- Green: Negative correlation (diversification benefit)
- Red: Positive correlation (less diversification)

**Risk Metrics:**
- Calmar Ratio: Return / Maximum drawdown
- Information Ratio: Excess return vs benchmark
- VaR (95%): Worst expected loss in normal scenarios
- Expected Shortfall: Average loss in tail events
- Herfindahl Index: Concentration measure
- Effective # Assets: Equivalent equally-weighted assets

**Diversification Analysis:**
- Shows how well-diversified your portfolio is
- Higher effective # of assets = better diversification

### Comparative Analysis Section
**Original Portfolio (Equal-Weight):**
- Default equal weight for all selected assets
- Baseline for comparison

**Optimized Portfolio:**
- Result from optimization algorithm
- Should show improvement in risk-adjusted metrics

**Comparison Metrics:**
- Return, Volatility, Sharpe, Sortino ratios
- Improvements (higher return, lower risk)
- Percentage changes

**Weight Changes:**
- Which assets increased in allocation
- Which assets decreased or eliminated
- Magnitude of changes

**Insights:**
- Key findings and recommendations
- Whether optimization provided value
- Specific asset allocation changes

## 📊 Asset Classes

### 🇮🇳 Indian Equities (8 Assets)
```
RELIANCE.NS  - Reliance Industries (diversified conglomerate)
TCS.NS       - Tata Consultancy Services (IT services)
HDFC.NS      - HDFC Bank (financial services)
INFY.NS      - Infosys (IT services)
WIPRO.NS     - Wipro (IT services)
LT.NS        - Larsen & Toubro (engineering/infrastructure)
MARUTI.NS    - Maruti Suzuki (automotive)
SBIN.NS      - State Bank of India (banking)
```

### 📈 Indian Indices (3 Assets)
```
^NSEI       - Nifty 50 (50 largest Indian stocks)
^NSEBANK    - Nifty Bank (12 largest banks)
^CNXIT      - Nifty IT (IT sector companies)
```

### 🇺🇸 US Equity Futures (3 Assets)
```
ES=F   - E-mini S&P 500 (500 large-cap companies)
NQ=F   - E-mini Nasdaq-100 (100 tech-heavy stocks)
YM=F   - E-mini Dow Jones (30 blue-chip companies)
```

### 🏆 Commodities Futures (4 Assets)
```
GC=F   - Gold Futures (precious metal)
CL=F   - Crude Oil Futures (energy)
SI=F   - Silver Futures (precious metal)
NG=F   - Natural Gas Futures (energy)
```

### 💱 Currency Futures (3 Assets)
```
USDINR=X   - USD/INR Exchange Rate
EURINR=X   - EUR/INR Exchange Rate
GBPINR=X   - GBP/INR Exchange Rate
```

### ₿ Cryptocurrencies (3 Assets)
```
BTC-USD   - Bitcoin (largest cryptocurrency)
ETH-USD   - Ethereum (smart contract platform)
BNB-USD   - Binance Coin (exchange utility token)
```

## 🎯 Optimization Methods

### Mathematical Foundation

#### Modern Portfolio Theory (MPT)
**Developed by:** Harry Markowitz (Nobel Prize 1990)

**Concept:**
- Efficient Frontier: Set of portfolios with maximum return for each risk level
- Trade-off: Can't increase return without increasing risk
- Diversification: Can reduce risk without reducing return
- Correlation: Key to diversification benefits

**Math:**
```
Portfolio Return: R_p = Σ(w_i × r_i)
Portfolio Volatility: σ_p = √(w^T × Σ × w)
where:
  w = weight vector
  r = return vector
  Σ = covariance matrix
```

#### Sharpe Ratio Maximization
**Developed by:** William Sharpe (Nobel Prize 1990)

**Formula:**
```
Sharpe Ratio = (R_p - R_f) / σ_p
where:
  R_p = portfolio return
  R_f = risk-free rate
  σ_p = portfolio volatility
```

**Interpretation:**
- Measures excess return per unit of risk
- Theoretically optimal for most investors
- Higher is better (>1 excellent, >2 outstanding)
- Used by professionals for portfolio comparison

### Method 1: Maximum Returns

**Objective Function:**
```
Maximize: Σ(w_i × r_i)
```

**Characteristics:**
- Finds highest return portfolio
- Usually highest risk
- Located at upper-right of efficient frontier
- Aggressive strategy

**Use Case:**
- Long-term investors
- High risk tolerance
- Growth objectives

**Example Output:**
```
Return: 25% | Risk: 22% | Sharpe: 0.86
Suitable for: Young investors, long time horizon
```

### Method 2: Minimum Risk (MVP)

**Objective Function:**
```
Minimize: √(w^T × Σ × w)
```

**Characteristics:**
- Lowest volatility portfolio
- Usually lower return
- Located at lower-left of efficient frontier
- Conservative strategy

**Use Case:**
- Retirees, capital preservation
- Low risk tolerance
- Income objectives

**Example Output:**
```
Return: 8% | Risk: 6% | Sharpe: 0.33
Suitable for: Retirees, conservative investors
```

### Method 3: Maximum Sharpe Ratio (RECOMMENDED)

**Objective Function:**
```
Maximize: (R_p - R_f) / σ_p
```

**Characteristics:**
- Best risk-adjusted returns
- Balanced risk and return
- Located at apex of efficient frontier
- Optimal for most scenarios

**Use Case:**
- Most investors
- Balanced objectives
- Risk-aware return seeking

**Example Output:**
```
Return: 16% | Risk: 12% | Sharpe: 0.83
Suitable for: General investors, best theory-backed choice
```

**Why Maximum Sharpe Ratio is Recommended:**
1. **Theoretical Foundation**: Based on Capital Asset Pricing Model (CAPM)
2. **Practical**: Offers good return with reasonable risk
3. **Universal**: Works across market conditions
4. **Professional**: Used by institutional investors
5. **Optimal**: Represents tangency point with Capital Allocation Line

## 📈 Metrics Explained

### Return Metrics

#### Annual Return
```
Definition: Expected yearly return percentage
Formula: Average daily return × 252 trading days
Range: -50% to +100%+
Interpretation:
  >15% = High return (higher risk)
  10-15% = Above average
  5-10% = Moderate
  <5% = Conservative
```

#### Sharpe Ratio
```
Definition: Risk-adjusted return
Formula: (Portfolio Return - Risk-Free Rate) / Volatility
Range: -2 to +2 (typically)
Interpretation:
  >2.0 = Excellent (outstanding risk-adjusted returns)
  1.0-2.0 = Good
  0.5-1.0 = Fair
  <0.5 = Poor (not enough return for risk)
  <0 = Negative (losing money on risk-adjusted basis)
```

#### Information Ratio
```
Definition: Excess return vs benchmark
Formula: (Portfolio Return - Benchmark) / Tracking Error
Range: -3 to +3 (typically)
Interpretation:
  >1.0 = Excellent (beating benchmark consistently)
  0.5-1.0 = Good
  0.0-0.5 = Meeting benchmark
  <0 = Underperforming benchmark
```

### Risk Metrics

#### Volatility (Standard Deviation)
```
Definition: Portfolio price fluctuation measure
Formula: √(w^T × Covariance Matrix × w) × √252
Range: 5% to 50%+ (depends on asset class)
Interpretation:
  <10% = Low volatility (stable)
  10-20% = Moderate volatility (balanced)
  20-40% = High volatility (risky)
  >40% = Very high volatility (speculative)
```

#### Sortino Ratio
```
Definition: Return per unit of downside risk
Formula: (Portfolio Return - Risk-Free) / Downside Deviation
Range: Similar to Sharpe, focuses on losses
Key Difference: Ignores upside volatility
Use When: Concerned about downside protection
Interpretation:
  >1.0 = Good downside-adjusted returns
  <0.5 = Risk not well-compensated
```

#### Calmar Ratio
```
Definition: Return relative to worst drawdown
Formula: Annual Return / Maximum Drawdown
Range: Typically 0 to 5
Interpretation:
  >1.0 = Good (earning more than worst loss)
  0.5-1.0 = Moderate
  <0.5 = Poor recovery characteristics
Example: Calmar 2.0 means earning 2% for every 1% loss
```

#### Maximum Drawdown
```
Definition: Largest peak-to-trough decline
Formula: (Lowest Value - Peak Value) / Peak Value
Range: 0% to -100% (always negative)
Interpretation:
  -5% to -10% = Moderate drawdown
  -10% to -20% = Significant drawdown
  -20% to -50% = Severe drawdown
  <-50% = Catastrophic drawdown
Example: -20% means portfolio fell to 80% of peak value
```

#### Value at Risk (VaR)
```
Definition: Maximum expected loss at confidence level
Formula: 5th percentile of return distribution
Range: Depends on portfolio
Interpretation (95% confidence):
  VaR = -5% means 95% chance loss is less than 5%
  Or: 1 in 20 chance of loss exceeding 5%
Example: If portfolio worth $100,000:
  VaR -5% means could lose up to $5,000 (95% of time)
```

### Diversification Metrics

#### Correlation Coefficient
```
Definition: Measure of how assets move together
Range: -1 to +1
Interpretation:
  +1 = Perfect positive (move together, no diversification)
  0 = No correlation (independent movement)
  -1 = Perfect negative (move opposite, max diversification)
Goal: Lower correlations = better diversification
```

#### Herfindahl Index
```
Definition: Portfolio concentration measure
Formula: Σ(w_i²) - Sum of squared weights
Range: 1/N (equal weight) to 1 (one asset)
Interpretation:
  <0.15 = Well diversified
  0.15-0.25 = Moderately diversified
  >0.25 = Concentrated portfolio
Lower = Better diversification
```

#### Effective Number of Assets
```
Definition: Equivalent equally-weighted assets
Formula: 1 / Herfindahl Index
Example:
  If 5 equal assets = 5 effective assets
  If 90% in 1 asset = ~1.1 effective assets
Interpretation: Higher is better (more diversification)
```

## 🔧 Technical Details

### Data Source: Yahoo Finance
```
Library: yfinance
Frequency: Daily closing prices
Adjustment: Adjusted close (accounts for splits/dividends)
Time Zone: Default is market time zone
Cache: 1 hour TTL for performance
```

### Optimization Algorithm
```
Method: Sequential Least Squares Programming (SLSQP)
Library: scipy.optimize.minimize
Max Iterations: 1000
Tolerance: 1e-9
Constraints:
  - Weights sum to 1.0
  - Each weight between 0 and 1
  - Optional: Target return for frontier points
```

### Return Calculations
```
Daily Return: (Price_today - Price_yesterday) / Price_yesterday
Annualized Return: Daily_return × 252 (trading days per year)
Covariance: Daily returns correlation matrix × 252
Volatility: √(portfolio variance) × √252
```

### Performance Backtest
```
Method: Historical simulation
Period: Same as input period
Calculation: (1 + daily_returns) compounded
Limitation: Past ≠ future; backtests are hypothetical
Does NOT include: Trading costs, taxes, rebalancing
```

## 🎨 Customization

### Adding Custom Assets

Edit `config.py` ASSET_CLASSES:
```python
ASSET_CLASSES = {
    "🇮🇳 Indian Equities": {
        "RELIANCE.NS": "Reliance Industries",
        "TCS.NS": "Tata Consultancy Services",
        "YOUR_TICKER.NS": "Your Company Name",  # Add here
    },
    # ... other classes
}
```

### Changing Color Scheme

Edit `config.py` COLORS:
```python
COLORS = {
    "dark_blue": "#003366",      # Main background
    "light_blue": "#004d80",     # Accents
    "gold": "#FFD700",           # Highlights
    # ... other colors
}
```

### Adjusting Default Parameters

Edit `config.py` PORTFOLIO_PARAMS:
```python
PORTFOLIO_PARAMS = {
    "lookback_min": 30,
    "lookback_max": 90,
    "lookback_default": 90,       # Default period
    "risk_free_rate_default": 0.06,  # Default 6%
    # ... other parameters
}
```

### Changing Benchmark

Edit `portfolio_comparative_analysis.py`:
```python
# Change default benchmark from Nifty 50 to S&P 500
benchmark_ticker = "^GSPC"  # Instead of "^NSEI"
```

## ❓ FAQ

### Q: Why is my portfolio's risk higher after optimization?
**A:** You selected "Maximum Returns" which accepts higher risk for return. Try "Maximum Sharpe Ratio" for balanced approach.

### Q: Can I use more than 10 assets?
**A:** Yes, the app supports any number. More assets improve diversification but reduce clarity.

### Q: Why is the efficient frontier curved?
**A:** Due to correlation between assets. Perfect correlation = straight line. Real assets have varying correlations.

### Q: What's a good Sharpe Ratio?
**A:** >1.0 is good, >2.0 is excellent. S&P 500 historically ~0.5-0.7.

### Q: How often should I rebalance?
**A:** Monthly to quarterly typical. More frequent = higher costs. Less frequent = drift from targets.

### Q: Why doesn't the app include trading costs?
**A:** Costs vary by broker and volume. Add them manually: subtract costs from expected return.

### Q: Can I use this for stocks I don't have data for?
**A:** Not directly. The app needs historical price data from Yahoo Finance.

### Q: Is the backtest realistic?
**A:** It shows historical performance but includes no costs, taxes, or slippage. It's illustrative only.

### Q: Can I short sell (go negative weight)?
**A:** Currently no. The app enforces 0-100% long-only positions.

### Q: How accurate are the metrics?
**A:** Very accurate for calculations, but past performance ≠ future results. Use as guide, not guarantee.

---

**Start Your Journey:** Run `streamlit run portfolio_optimizer.py` and optimize your first portfolio! 🎉
