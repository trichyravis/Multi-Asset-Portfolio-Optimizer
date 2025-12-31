FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY portfolio_optimizer.py .
COPY config.py .
COPY styles.py .
COPY portfolio_analytics.py .
COPY portfolio_comparative_analysis.py .
COPY portfolio_comparative_analysis_enhanced.py .

# Create .streamlit directory
RUN mkdir -p .streamlit

# Copy Streamlit config
COPY .streamlit/config.toml .streamlit/

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "portfolio_optimizer.py", "--server.port=8501", "--server.address=0.0.0.0"]
