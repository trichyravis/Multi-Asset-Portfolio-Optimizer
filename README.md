# 🏔️ Multi-Asset Portfolio Optimizer

Professional portfolio optimization tool with Modern Portfolio Theory and 3D Efficient Frontier visualization.

**Built by:** Prof. V. Ravichandran  
**Platform:** The Mountain Path - World of Finance

---

## 🎯 Features

### Portfolio Setup (HOME Page)
- **Asset Class Selection:** 6 classes (Equities, Indices, Futures, Commodities, Currencies, Crypto)
- **Asset Selection:** Multiple assets per class
- **Weight Allocation:** Auto-populate equal weights, user-editable
- **Optimization Method:** 
  - Modern Portfolio Theory (Maximize Returns / Minimize Risk)
  - Maximize Sharpe Ratio

### Portfolio Analysis (RESULTS Page)
- **3D Efficient Frontier:** Interactive 3D visualization with 5000 portfolios
- **2D Risk-Return Plot:** Easy-to-read comparison
- **Weight Comparison:** Bar charts and pie charts
- **Metrics Comparison:** 7 comprehensive metrics

---

## 📊 Technology Stack

- **Frontend:** Streamlit + Plotly
- **Backend:** Python, NumPy, SciPy, Pandas
- **Data:** Yahoo Finance
- **Design:** Professional Streamlit template

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
streamlit run app.py
```

### 3. Deploy to Cloud
Push to GitHub → Deploy to Streamlit Cloud

---

## 📁 File Structure

```
portfolio_optimizer/
├── app.py                      # Main entry
├── portfolio_analytics.py       # Optimization
├── config.py                   # Design config
├── styles.py                   # CSS styles
├── components.py               # Components
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
│
└── pages/
    ├── 1_🏠_Home.py            # Setup page
    └── 2_📊_Results.py         # Analysis page
```

---

## 🔧 How It Works

1. **Select Assets** - Choose from 6 asset classes
2. **Allocate Weights** - Auto-equal or custom weights
3. **Choose Method** - MPT or Sharpe Ratio optimization
4. **View Results** - 3D efficient frontier + metrics

---

## 📈 Metrics

- Annual Return
- Annual Volatility
- Sharpe Ratio
- Sortino Ratio
- Max Drawdown
- VaR (95%)
- Expected Shortfall

---

## 🎓 Educational Value

Perfect for:
- MBA Portfolio Management courses
- CFA Risk Management studies
- FRM Risk Metrics training
- Finance professionals
- Research and teaching

---

## ⚠️ Disclaimer

Educational tool only. Past performance does not guarantee future results. Always consult financial advisors.

---

## 🏔️ The Mountain Path - World of Finance

28+ Years Corporate Finance | 10+ Years Academic Excellence

---

**Happy Optimizing!** 🚀
