import streamlit as st

# **** Page layout setup ****
App_page_0 = st.Page(
    "pages/main.py",
    title="Main Page",
    default=True
)
App_page_1 = st.Page(
    "pages/page1.py",
    title="Page 1: Stocks"
)
App_page_2 = st.Page(
    "pages/page2.py",
    title="Page 2"
)
App_page_3 = st.Page(
    "pages/page3.py",
    title="Page 3"
)

# **** Set up navigation with section headers ****
pg = st.navigation(
    {
        "General": [App_page_0],
        "Specific Pages": [App_page_1, App_page_2, App_page_3],
    }
)


# **** text/images shared on all pages ****
# st.logo("files/name_of_file.png")
st.sidebar.markdown("Sidebar Prompts:")


# **** Execute the navigation code ****
pg.run()
