import streamlit as st

st.title("Page 2")


if "Close" in data:
   st.subheader("Closing Price Over Time")
   st.line_chart(data['Close'])
else:
   st.warning("Closing price data is not available for this stock.")
