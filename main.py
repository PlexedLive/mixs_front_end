import landing_page
import app
import streamlit as st

PAGES = {
    "Landing Page": landing_page,
    "App": app
}

st.sidebar.title('Pages')
selection = st.sidebar.radio("",list(PAGES.keys()))
page = PAGES[selection]
page.app()
