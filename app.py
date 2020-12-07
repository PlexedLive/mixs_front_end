import streamlit as st
import os
import soundfile
from mixs.youtube import YouTubeTools
from mixs.split import splitter


# Change background image
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


    # Markdown texts for heading
    col1, col2 = st.beta_columns([10,6])
    col1.markdown("<h1 style='text-align: left; color: white; font-family: Marker Felt'>MixS</h1>",unsafe_allow_html=True)
    col2.markdown("<h2 style='text-align: left; color: white; font-family: URW Chancery L'>Music Mix Separation</h2>",unsafe_allow_html=True)

    # st.markdown("<h2 style='text-align: center; color: white; font-family: Verdana'>Get high quality backing tracks!</h2>",unsafe_allow_html=True)
    # Fetching YouTube link from the end-user
    col3, col4 = st.beta_columns([10,1])
    explanation = st.markdown("<h4 style='text-align: left; color: white; font-family: Ariel'>Enter the URL of the track to be separated</h4>",unsafe_allow_html=True)

    youtube_link = st.text_input("")
    # button = col4.button("Upload")


    # Fetching the song from YouTube
    def youtube_display(url):
        return st.video(url)

    def np_audio(np_array, samplerate=44100):
        soundfile.write('temp.wav', np_array, samplerate, 'PCM_24')
        return st.audio('temp.wav', format='audio/wav')

    if youtube_link != "":
        link = YouTubeTools(youtube_link)
        button = st.button("Proceed with Separation?")


        if button:
            filename = link.get_audio_and_directory()
            stems, rate = splitter(filename)
            rate = int(rate)
            st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Vocals</h3>",unsafe_allow_html=True)
            np_audio(stems['vocals'], samplerate = rate)

            st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Piano</h3>",unsafe_allow_html=True)
            np_audio(stems['piano'], samplerate = rate)

            st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Drums</h3>",unsafe_allow_html=True)
            np_audio(stems['drums'], samplerate = rate)

            st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Bass</h3>",unsafe_allow_html=True)
            np_audio(stems['bass'], samplerate = rate)

            st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Other</h3>",unsafe_allow_html=True)
            np_audio(stems['other'], samplerate = rate)

            link.clear_wavs()
        else:
            youtube_display(youtube_link)




