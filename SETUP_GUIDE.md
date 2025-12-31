# 🚀 Setup Guide - Multi-Asset Portfolio Optimizer

Complete installation, configuration, and troubleshooting guide.

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Verification](#verification)
4. [Configuration](#configuration)
5. [Deployment](#deployment)
6. [Troubleshooting](#troubleshooting)
7. [Performance Tuning](#performance-tuning)

## 💻 System Requirements

### Minimum Requirements
```
CPU:         Dual-core processor
RAM:         4 GB minimum
Storage:     500 MB free space
OS:          Windows, macOS, or Linux
Python:      3.8 or higher
```

### Recommended Requirements
```
CPU:         Quad-core processor
RAM:         8+ GB
Storage:     1 GB free space
Python:      3.9 or higher
Internet:    Stable connection for data fetching
```

### Python Version Check
```bash
python --version
# Should show: Python 3.8.x or higher
```

## 📦 Installation Steps

### Step 1: Install Python

#### Windows
1. Download from: https://www.python.org/downloads/
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

#### macOS
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from: https://www.python.org/downloads/
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Step 2: Prepare Directory

```bash
# Create project directory
mkdir portfolio-optimizer
cd portfolio-optimizer

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Download Files

Place these files in the `portfolio-optimizer` directory:
```
portfolio-optimizer/
├── config.py
├── styles.py
├── portfolio_optimizer.py
├── portfolio_analytics.py
├── portfolio_comparative_analysis.py
├── requirements.txt
└── README.md
```

### Step 4: Install Dependencies

```bash
# Upgrade pip (important!)
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installation
pip list
```

**Expected output:**
```
streamlit            1.28.1
pandas              2.1.1
numpy               1.24.3
scipy               1.11.3
yfinance            0.2.33
plotly              5.17.0
python-dateutil     2.8.2
```

## ✅ Verification

### Test 1: Python Installation
```bash
python --version
# Expected: Python 3.8.x or higher
```

### Test 2: Pip Installation
```bash
pip --version
# Expected: pip x.x.x from /path/to/python
```

### Test 3: Import Packages
```bash
python -c "import streamlit; print('Streamlit:', streamlit.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import scipy; print('SciPy:', scipy.__version__)"
python -c "import yfinance; print('yfinance OK')"
python -c "import plotly; print('Plotly:', plotly.__version__)"
```

### Test 4: Run Application
```bash
streamlit run portfolio_optimizer.py
```

**Expected:**
- Streamlit banner appears
- Browser opens to http://localhost:8501
- Sidebar with input controls appears

### Test 5: Fetch Data
1. Select time period (default: 90 days)
2. Select asset classes
3. Pick 3-4 assets
4. Click "🚀 Fetch Data & Optimize"

Should complete in 5-10 seconds with results.

## 🔧 Configuration

### Configuration File: config.py

```python
# Asset Classes - Add/remove tickers
ASSET_CLASSES = {
    "🇮🇳 Indian Equities": {
        "RELIANCE.NS": "Reliance Industries",
        # Add more assets here
    },
}

# Colors - Customize appearance
COLORS = {
    "dark_blue": "#003366",
    "light_blue": "#004d80",
    "gold": "#FFD700",
}

# Parameters - Adjust defaults
PORTFOLIO_PARAMS = {
    "lookback_default": 90,        # Default period
    "risk_free_rate_default": 0.06, # Default risk-free rate
}
```

### Adding New Assets

**Example: Add Bajaj Auto to Indian Equities**

```python
# In config.py, ASSET_CLASSES section:

ASSET_CLASSES = {
    "🇮🇳 Indian Equities": {
        "RELIANCE.NS": "Reliance Industries",
        "TCS.NS": "Tata Consultancy Services",
        "BAJAJINSURANCE.NS": "Bajaj Insurance",  # Add this line
        # ... other assets
    },
}
```

**Note:** Ticker must exist on Yahoo Finance with format:
- Indian stocks: `SYMBOL.NS`
- US assets: `SYMBOL=F` or `SYMBOL`
- Crypto: `SYMBOL-USD`

### Changing Default Risk-Free Rate

```python
# In config.py PORTFOLIO_PARAMS:

PORTFOLIO_PARAMS = {
    "risk_free_rate_min": 0.0,
    "risk_free_rate_max": 0.10,
    "risk_free_rate_default": 0.08,  # Changed from 0.06 to 8%
}
```

### Customizing Colors

```python
# In config.py COLORS:

COLORS = {
    "dark_blue": "#1a1a2e",        # Dark background
    "light_blue": "#16213e",       # Light accent
    "gold": "#00d4ff",             # Cyan instead of gold
    "text_dark": "#ffffff",        # White text
}
```

## 🌐 Deployment

### Local Development (Current Setup)
```bash
# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run app
streamlit run portfolio_optimizer.py

# Access at: http://localhost:8501
```

### Streamlit Cloud (Free Deployment)

**Step 1: Prepare GitHub**
```bash
# Create GitHub repository
# Push all files to GitHub
git init
git add .
git commit -m "Initial commit"
git push origin main
```

**Step 2: Deploy to Streamlit Cloud**
1. Go to: https://streamlit.io/cloud
2. Sign up with GitHub
3. Click "New app"
4. Select repository and `portfolio_optimizer.py`
5. Click "Deploy"

**Step 3: Access Your App**
- Streamlit Cloud generates public URL
- App auto-updates when GitHub repo changes
- Free tier: Shared resources

### Self-Hosted (AWS/Azure/GCP)

**Using Docker:**

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py .

EXPOSE 8501

CMD ["streamlit", "run", "portfolio_optimizer.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t portfolio-optimizer .
docker run -p 8501:8501 portfolio-optimizer
```

## 🔍 Troubleshooting

### Issue 1: Python Not Found
```bash
# Windows
python -c "import sys; print(sys.executable)"

# macOS/Linux
which python3
```

**Solution:** 
- Add Python to PATH (Windows)
- Use `python3` instead of `python` (macOS/Linux)
- Reinstall Python with PATH option checked

### Issue 2: pip Not Found
```bash
# Windows
py -m pip --version

# macOS/Linux
python3 -m pip --version
```

**Solution:**
- Use `python -m pip install` instead of `pip install`
- Upgrade: `python -m pip install --upgrade pip`

### Issue 3: Virtual Environment Issues

```bash
# Remove and recreate
rm -rf venv  # macOS/Linux
rmdir venv /s  # Windows PowerShell

# Create fresh
python -m venv venv

# Activate and install
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Issue 4: "Could not fetch data" Error

**Causes:**
- Invalid ticker symbols
- No internet connection
- Yahoo Finance temporary outage
- Ticker doesn't exist/no history

**Solutions:**
```bash
# Verify ticker exists
python -c "import yfinance as yf; print(yf.Ticker('RELIANCE.NS').info)"

# Test basic functionality
python -c "import yfinance as yf; data = yf.download('RELIANCE.NS', period='1mo'); print(data.head())"

# Check internet connection
python -c "import socket; socket.create_connection(('8.8.8.8', 53))"
```

### Issue 5: Slow Performance

**Causes:**
- Large number of assets (10+)
- Long lookback period (90 days)
- First run (fetching data)

**Solutions:**
```python
# In portfolio_optimizer.py, increase cache TTL:
@st.cache_data(ttl=7200)  # 2 hours instead of 1 hour
def fetch_asset_data(...):
    ...

# Reduce assets or period in first run
```

### Issue 6: Memory Issues

```bash
# Check memory usage
python -c "import psutil; print(f'Available RAM: {psutil.virtual_memory().available / 1024**3:.1f} GB')"
```

**Solutions:**
- Close other applications
- Upgrade RAM
- Reduce number of assets
- Use shorter lookback period

### Issue 7: Port 8501 Already in Use

```bash
# Use different port
streamlit run portfolio_optimizer.py --server.port 8502

# Find and kill process using port 8501
# Windows PowerShell:
Get-Process -Id (Get-NetTCPConnection -LocalPort 8501).OwningProcess

# macOS/Linux:
lsof -i :8501 | grep LISTEN | awk '{print $2}' | xargs kill
```

### Issue 8: Module Import Errors

```bash
# Clear cache
rm -rf __pycache__

# Reinstall packages
pip install --force-reinstall -r requirements.txt

# Verify imports
python -c "import portfolio_optimizer"
```

### Issue 9: Charts Not Displaying

**Cause:** Plotly rendering issue

**Solution:**
```bash
# Upgrade Plotly
pip install --upgrade plotly

# Clear Streamlit cache
streamlit cache clear

# Restart app
```

### Issue 10: Data Accuracy Questions

```python
# Verify data source
import yfinance as yf

ticker = yf.Ticker('RELIANCE.NS')
print(ticker.info)  # Check last update
print(ticker.quarterly_financials)  # Verify data
```

## ⚡ Performance Tuning

### Optimize Data Fetching

```python
# In portfolio_optimizer.py:

@st.cache_data(ttl=3600)  # Increase cache time
def fetch_asset_data(tickers: list, days: int) -> pd.DataFrame:
    # ... existing code ...
```

### Limit Assets for Speed

```python
# In config.py, reduce default selections:

ASSET_CLASSES = {
    "🇮🇳 Indian Equities": {
        "RELIANCE.NS": "Reliance Industries",  # Keep only top 3
        "TCS.NS": "Tata Consultancy Services",
        "HDFC.NS": "HDFC Bank",
    },
}
```

### Reduce Frontier Points

```python
# In portfolio_optimizer.py:

frontier_returns, frontier_vols, _ = calculate_efficient_frontier(
    annual_returns,
    cov_matrix,
    risk_free_rate,
    num_points=50  # Reduce from 100 to 50
)
```

### Browser Optimization

```bash
# Run with custom settings
streamlit run portfolio_optimizer.py \
  --client.maxMessageSize=200 \
  --client.toolbarMode=minimal
```

## 📊 Monitoring

### Track Performance

```bash
# Run with debug info
streamlit run portfolio_optimizer.py --logger.level=debug

# Check memory usage during runtime
streamlit run portfolio_optimizer.py --client.showErrorDetails=true
```

### Logs Location

```
# Windows
%APPDATA%\streamlit\logs

# macOS
~/.streamlit/logs

# Linux
~/.streamlit/logs
```

---

**Need Help?** Check README.md or START_HERE.md for more guidance.
