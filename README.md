# 🏔️ Multi-Asset Portfolio Optimizer

## The Mountain Path - World of Finance

A professional, interactive web application for portfolio optimization using Modern Portfolio Theory (MPT).

**Author:** Prof. V. Ravichandran  
**Experience:** 28+ Years Corporate Finance | 10+ Years Academic Excellence

---

## 📋 Features

### Portfolio Setup
- ✅ Select from 5 asset classes (Equities, Indices, Bonds, Commodities, Crypto)
- ✅ Choose from 30+ individual assets with full names and descriptions
- ✅ Set portfolio weights with 100% validation
- ✅ Pre-optimization analysis with current metrics

### Optimization
- ✅ 3 optimization strategies:
  - Maximize Returns (Growth)
  - Minimize Risk (Conservative)
  - Maximize Sharpe Ratio (Balanced - Recommended)

### Analysis & Visualization
- ✅ Efficient frontier 3D interactive visualization
- ✅ Portfolio metrics comparison (Before vs After)
- ✅ Weight allocation visualization
- ✅ Risk/return analysis with Sharpe ratios
- ✅ Performance metrics (Return, Volatility, Sharpe, Sortino, Drawdown)

### Design
- ✅ Dark blue professional theme (#003366)
- ✅ White text for excellent contrast
- ✅ Responsive layout
- ✅ Interactive charts and visualizations

---

## 🚀 Quick Start

### 1. Local Setup

```bash
# Clone repository
git clone https://github.com/trichrayvis/Multi-Asset-Portfolio-Optimizer.git
cd Multi-Asset-Portfolio-Optimizer

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### 2. Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository
5. Set main file to `app.py`
6. Click "Deploy"

---

## 📁 Project Structure

```
Multi-Asset-Portfolio-Optimizer/
│
├── app.py                          # Main entry point
├── config_enhanced.py              # Asset data & configuration
├── styles_enhanced.py              # Styling & theme
├── portfolio_analytics_enhanced.py # Analytics & optimization
├── requirements.txt                # Dependencies
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
│
├── .streamlit/
│   └── config.toml                # Streamlit configuration
│
└── pages/
    ├── 1_🏠_Home_Enhanced.py      # Home page - Portfolio setup
    └── 2_📊_Results_Enhanced.py   # Results page - Optimization output
```

---

## 📊 How It Works

### Step 1: Portfolio Setup (Home Page)
1. **Select Asset Classes** - Choose which types of assets to include
2. **Select Assets** - Choose specific investments from each class
3. **Allocate Weights** - Set percentage distribution (must sum to 100%)
4. **View Pre-Analysis** - See current portfolio metrics before optimization

### Step 2: Optimization (Choose Strategy)
1. **Maximize Returns** - Focus on growth, accept higher volatility
2. **Minimize Risk** - Focus on safety, accept lower returns
3. **Maximize Sharpe Ratio** - Balance risk and return (Recommended)

### Step 3: Results (Results Page)
1. **View Comparison** - See metrics before and after optimization
2. **Efficient Frontier** - Interactive 3D visualization of all possible portfolios
3. **Weight Changes** - See how allocation changed
4. **Recommendations** - Get strategy-specific advice

---

## 📈 Key Metrics Explained

| Metric | Definition | What It Means |
|--------|-----------|---------------|
| **Annual Return** | Expected yearly gain | Higher = More profit, but more risk |
| **Volatility** | Price fluctuation (std dev) | Higher = More risky, more price swings |
| **Sharpe Ratio** | Return per unit of risk | Higher = Better risk-adjusted returns |
| **Sortino Ratio** | Return per unit of downside risk | Higher = Better downside protection |
| **Max Drawdown** | Worst expected loss | How much could you lose from peak |

---

## 🎨 Design & Color Scheme

- **Primary Background:** Dark Blue (#003366)
- **Text Color:** White (#FFFFFF)
- **Accent Color:** Gold (#FFD700)
- **Secondary Color:** Light Blue (#ADD8E6)
- **Font:** Times New Roman (headings), Arial (body)

---

## 📚 Technologies Used

- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Plotly** - Interactive visualizations
- **Python** - Programming language

---

## 📝 Asset Classes & Assets

### Equities
- Apple (AAPL), Microsoft (MSFT), Google (GOOGL), Amazon (AMZN), Tesla (TSLA), Meta (META), NVIDIA (NVDA), JPMorgan (JPM), Visa (V), Walmart (WMT)

### Indices
- S&P 500 (SPY), Nasdaq-100 (QQQ), Russell 2000 (IWM), MSCI EAFE (EFA), Total US Market (VTI)

### Bonds
- Total Bond (BND), Aggregate Bond (AGG), Short Treasury (SHV), Long Treasury (TLT), Corporate Bonds (LQD)

### Commodities
- Gold (GLD), Silver (SLV), Oil (USO), Commodity Index (DBC), Commodity ETF (PDBC)

### Cryptocurrencies
- Bitcoin (BTC), Ethereum (ETH)

---

## ⚙️ Configuration

All configuration is in `config_enhanced.py`:

```python
# Asset classes and details
ASSET_CLASSES = {
    "Equities": {...},
    "Bonds": {...},
    ...
}

# Asset statistics (returns, volatility)
ASSET_STATS = {
    "AAPL": {"return": 0.28, "volatility": 0.32},
    ...
}

# Color scheme
COLORS = {
    "dark_blue": "#003366",
    "gold": "#FFD700",
    ...
}

# Risk-free rate for Sharpe ratio
RISK_FREE_RATE = 0.045  # 4.5%
```

---

## 🔧 Development

### Adding New Assets

1. Open `config_enhanced.py`
2. Add to appropriate `ASSET_CLASSES` section:
   ```python
   "NEW_TICKER": {"name": "Full Name", "sector": "Sector"}
   ```
3. Add to `ASSET_STATS`:
   ```python
   "NEW_TICKER": {"return": 0.15, "volatility": 0.20}
   ```

### Customizing Colors

Edit `config_enhanced.py` colors section or update CSS in `styles_enhanced.py`

### Changing Risk-Free Rate

Update `RISK_FREE_RATE` in `config_enhanced.py` (currently 4.5%)

---

## 📋 Requirements

- Python 3.8+
- Streamlit 1.28+
- Pandas 2.1+
- NumPy 1.26+
- Plotly 5.18+
- SciPy 1.11+

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push and submit a pull request

---

## 📄 License

MIT License - Feel free to use, modify, and distribute

---

## 💬 Support & Feedback

For issues, suggestions, or questions:
- Open an issue on GitHub
- Contact: Prof. V. Ravichandran

---

## 📚 Resources

- [Modern Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)
- [Sharpe Ratio](https://en.wikipedia.org/wiki/Sharpe_ratio)
- [Efficient Frontier](https://en.wikipedia.org/wiki/Efficient_frontier)
- [Streamlit Documentation](https://docs.streamlit.io)

---

## 🏔️ The Mountain Path - World of Finance

Building accessible, professional financial education and tools for investors worldwide.

**Visit:** [The Mountain Path](https://www.themountainpath.com)

---

**Last Updated:** December 31, 2025  
**Version:** 1.0.0
