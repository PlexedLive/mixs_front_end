import streamlit as st
# import os
# import soundfile
# from mixs.youtube import YouTubeTools
# from mixs.split import splitter


# # Change background image
# page_bg_img = '''
# <style>
# body {
# background-image: url("https://www.onholdinc.com/mohblog/wp-content/uploads/2019/09/music-news.jpg");
# background-size: cover;
# }
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)


# # Markdown texts for heading
# st.markdown("<h1 style='text-align: center; color: white; font-family: Marker Felt'>MixS</h1>",unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: left; color: white; font-family: URW Chancery L'>Music Mix Separation</h2>",unsafe_allow_html=True)

# # Fetching YouTube link from the end-user
# col1, col2 = st.beta_columns([10,1])
# explanation = col1.markdown("<h4 style='text-align: left; color: white; font-family: URW Chancery L'>Enter the URL of the track to be separated</h4>",unsafe_allow_html=True)


# youtube_link = col1.text_input("")
# button = col2.button("Upload")


# # Fetching the song from YouTube
# def youtube_display(url):
#     return st.video(url)

# def np_audio(np_array, samplerate=44100):
#     soundfile.write('temp.wav', np_array, samplerate, 'PCM_24')
#     return st.audio('temp.wav', format='audio/wav')

# if button:
#     link = YouTubeTools(youtube_link)
#     youtube_display(youtube_link)
#     filename = link.get_audio_and_directory()
#     stems = splitter(filename)

#     if stems != None:
#         st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Vocals</h3>",unsafe_allow_html=True)
#         np_audio(stems['vocals'])

#         st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Piano</h3>",unsafe_allow_html=True)
#         np_audio(stems['piano'])

#         st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Drums</h3>",unsafe_allow_html=True)
#         np_audio(stems['drums'])

#         st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Bass</h3>",unsafe_allow_html=True)
#         np_audio(stems['bass'])

#         st.markdown("<h3 style='text-align: left; color: white; font-family: Monaco'>Other</h3>",unsafe_allow_html=True)
#         np_audio(stems['other'])


st.title('Worked')
