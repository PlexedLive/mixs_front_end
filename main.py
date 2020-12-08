import landing_page
import app
import streamlit as st

PAGES = {
    "Landing Page": landing_page,
    "App": app
}

page_bg_img = '''
    <style>
    body {
    background-image: url("https://i.pinimg.com/originals/57/f5/fa/57f5fa649b7683b5ee4999242e873e63.jpg");
    background-size: cover;
    }
    audio { display: none; }
    .streamlit-button {
      color: white;
    }
    </style>
    '''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.title('Pages')
selection = st.sidebar.radio("",list(PAGES.keys()))
page = PAGES[selection]
page.app()
