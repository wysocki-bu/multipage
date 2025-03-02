import streamlit as st

st.title("Page 3")

if 'data' in st.session_state:
   st.write("Closing Price Over Time:")
   st.line_chart(data)
else:
   st.write("No DataFrame found. Please create it in the 'Create DataFrame' page.")

