import streamlit as st

def app():
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://i.pinimg.com/originals/57/f5/fa/57f5fa649b7683b5ee4999242e873e63.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    col1, col2 = st.beta_columns([10, 6])
    col1.markdown("<h1 style='text-align: left; color: white; font-family: Marker Felt'>MixS</h1>",unsafe_allow_html=True)
    col2.markdown("<h2 style='text-align: left; color: white; font-family: URW Chancery L'>Music Mix Separation</h2>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white; font-family: Verdana'>Get high quality backing tracks!</h2>",unsafe_allow_html=True)

    col3, col4 = st.beta_columns(2)
    col3.image("equipment.jpg", width = 100)
    col4.image("electronic_music.jpg")
