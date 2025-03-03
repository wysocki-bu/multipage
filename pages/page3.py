import streamlit as st

st.title("Page 3: Close Price data")

if 'data' in st.session_state:
   st.write("Statistics of the DataFrame:")
   cl_prc=st.session_state.data("Close")
   st.write(cl_prc)
else:
   st.write("No stock data found. Please select stock on Main Page.")
#   st.write("Closing Price Over Time:")
#   st.line_chart(data)
else:
   st.write("No DataFrame found. Please create it in the 'Create DataFrame' page.")

