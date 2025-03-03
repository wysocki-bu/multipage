import streamlit as st
import pandas as pd
import yfinance as yf

# Page title
st.title("Page 1: View Stock Data")

st.data_editor(st.session_state.data)

#st.session_state.data = st.data_editor(st.session_state.data)
