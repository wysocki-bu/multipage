import streamlit as st

st.title("Page 3")

if 'data' in st.session_state:
   st.write("Closing Price Over Time:")
   st.write(st.session_state.data.describe())
else:
   st.write("No DataFrame found. Please create it in the 'Create DataFrame' page.")

#    if "Close" in data:
#        st.subheader("Closing Price Over Time")
#        st.line_chart(data['Close'])
#    else:
#        st.warning("Closing price data is not available for this stock.")

#st.session_state.data = st.data_editor(st.session_state.data)
