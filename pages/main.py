import streamlit as st
import pandas as pd
import yfinance as yf

# Page title
st.title("Main Page: Select Stock")

# Sidebar inputs
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))

# Fetching data
st.write(f"Data for **{ticker_symbol}** from {start_date} to {end_date}.")
df = yf.download(ticker_symbol, start=start_date, end=end_date)
if df.empty:
   st.error("No data found. Please check the ticker symbol or date range.")
   st.stop()
st.session_state.data = df
