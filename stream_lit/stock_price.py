# Stock Price Tracker
# pip install streamlit pandas yfinance plotly
# Run: streamlit run stock_price.py

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def get_company_name(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Try to get the long name, if not available, use the ticker symbol
        return ticker.info.get('longName', ticker_symbol)
    except Exception as e:
        print(f"Error fetching company name: {e}")
        return ticker_symbol  # Return the ticker symbol if name can't be fetched

# Set page config
st.set_page_config(page_title="Stock Price Tracker", layout="wide")

# Title
st.title("📈 Stock Price Tracker")

# Sidebar for user inputs
st.sidebar.header("Settings ⚙️")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", value=datetime.now())
notes = st.sidebar.text_area("Try With", value="AAPL\nMSFT\nGOOGL\nMETA\nTSLA")

# Function to fetch stock data
@st.cache_data
def load_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load data
df = load_data(ticker, start_date, end_date)

# Display data
if df is not None and not df.empty:
    # Get company name
    company_name = get_company_name(ticker)
    # Show basic stats
    st.subheader(f"{ticker} Stock Price")
    st.caption(f"{company_name}")
    col1, col2, col3 = st.columns(3)
    with col1:
        current_price = float(df['Close'].iloc[-1])
        st.metric("Current Price", f"${current_price:.2f}")
    with col2:
        price_change = float(df['Close'].iloc[-1] - df['Close'].iloc[-2])
        percent_change = (price_change / float(df['Close'].iloc[-2])) * 100
        st.metric("Change", f"{percent_change:.2f}%")
    
    # Create interactive chart
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index,
                                open=df['Open'],
                                high=df['High'],
                                low=df['Low'],
                                close=df['Close'],
                                name='Market Data'))
    
    fig.update_layout(
        title=f"{ticker} Stock Price",
        yaxis_title="Price (USD)",
        xaxis_title="Date",
        template="plotly_dark"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Show raw data
    if st.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        st.dataframe(df)
else:
    st.warning("Please enter a valid stock ticker and date range.")