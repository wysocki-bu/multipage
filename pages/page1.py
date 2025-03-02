import streamlit as st
import pandas as pd
import numpy as np
import plotly 

# df = pd.read_csv('msft.csv')

st.title("Page 1: Stock Dashboard")
# st.dataframe(df)

ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

price_history = fetch_weekly_price_history(symbol)
st.header('Chart')
price_history = price_history.rename_axis('Date').reset_index
candle_stick_chart = go.Figure(data=[go.Candlestick(x=price_history['Date'],
                               open=price_history['Opem'],
                               low=price_history['Low'],
                               high=price_history['High'],
                               close=price_history['Close'])])

# candle_stick_chart.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(candle_stick_chart, use_container_width=True)




