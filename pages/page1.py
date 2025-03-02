import streamlit as st
import pandas as pd
import numpy as np
#import yfinance as yf

st.title("Page 1: Stock Dashboard")
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

