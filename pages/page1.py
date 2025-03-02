import streamlit as st
import pandas as pd
import yfinance as yf

# Page title
st.title("Page 1: Stock Dashboard")

# Sidebar inputs
# st.sidebar.header("BA870-AC820 StreamLit Example")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))

# Fetching data
st.write(f"Data for **{ticker_symbol}** from {start_date} to {end_date}...")
#if 'data' not in st.session_state:
#    df = yf.download(ticker_symbol, start=start_date, end=end_date)
#    if df.empty:
#       st.error("No data found. Please check the ticker symbol or date range.")
#       st.stop()
#    st.session_state.data = df

df = yf.download(ticker_symbol, start=start_date, end=end_date)
if df.empty:
   st.error("No data found. Please check the ticker symbol or date range.")
   st.stop()
st.session_state.data = df

st.session_state.data = st.data_editor(st.session_state.data)
