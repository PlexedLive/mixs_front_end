import streamlit as st
import requests
import os
import json
import soundfile
from scipy.io.wavfile import write
from mixs.youtube import YouTubeTools
from mixs.split import splitter
import streamlit.components.v1 as components
from streamlit.media_file_manager import _calculate_file_id, STATIC_MEDIA_ENDPOINT
import logging

# stem_urls = []

# Change background image
# def app():

def read_local_asset(file_name, type='style'):
    with open(file_name) as f:
        return f'<{type}>{f.read()}</{type}>'

spinner = '<div class="loader">Loading...</div>'

st.set_page_config(page_title='MixS', page_icon=None, layout='wide', initial_sidebar_state='auto')

# Loading stylesheets from Github
app_stylesheet = requests.get("https://raw.githubusercontent.com/PlexedLive/mixs_front_end/main/styles/app.css").content.decode('utf-8')
mixer_stylesheet = requests.get("https://raw.githubusercontent.com/PlexedLive/mixs_front_end/main/styles/mixer.css").content.decode('utf-8')
st.markdown(read_local_asset('styles/app.css'), unsafe_allow_html=True)

# Markdown texts for heading
col1, col2 = st.beta_columns(2)
col2.image("logo_transparent.png", width=260)
# col2.markdown("## Practice like a Pro!")

# st.markdown("<h2 style='text-align: center; color: white; font-family: Verdana'>Get high quality backing tracks!</h2>",unsafe_allow_html=True)
# Fetching YouTube link from the end-user
col3, col4 = st.beta_columns([10,1])

st.markdown("## Practice like a pro: Extract vocals and instruments from your favorite songs!")

# youtube_link = st.text_input("", "Enter YouTube URL")


# Fetching the song from YouTube
def youtube_display(url):
    return st.video(url)


youtube_display('https://www.youtube.com/watch?v=CdvITn5cAVc')

stem_urls = []

def np_audio(stem_name, np_array=None, samplerate=44100, audio_path=None):
    if audio_path == None:
        audio_path = 'temp.wav'
        soundfile.write(audio_path, np_array, samplerate, 'PCM_24')

    st.audio(audio_path, format='audio/wav')
    with open(audio_path, "rb") as f:
        file_id = _calculate_file_id(f.read(), "audio/wav")
        wav_url = f'{STATIC_MEDIA_ENDPOINT}/{file_id}.wav'
        stem_urls.append({
            'src': wav_url,
            'name': stem_name,
            'customClass': stem_name,
            })

# if youtube_link != "Enter YouTube URL":
#     stem_urls = []
#     link = YouTubeTools(youtube_link)
#     button = st.button("Separate")
#     logging.info('loading link')

#     if button:
#         spinner = st.markdown(spinner, unsafe_allow_html=True)
#         link.clear_wavs()
#         filename = link.get_audio_and_directory()
#         stems, rate = splitter(filename)
#         rate = int(rate)
#         logging.info('splitting song')
#         spinner.write("")

stems = {
'vocals': 'Samples/Vocals.wav',
'piano': 'Samples/Piano.wav',
'drums': 'Samples/Drums.wav',
'bass': 'Samples/Bass.wav',
'other': 'Samples/Other.wav'
}

for stem, audio_path in stems.items():
    np_audio(stem, audio_path=audio_path)
    logging.info('displaying stems')

components.html(f'''
<head>
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" />
  {read_local_asset('styles/waveform.css')}
  {read_local_asset('styles/mixer.css')}

</head>
<body>
  <div id="top-bar" class="playlist-top-bar">
    <div class="playlist-toolbar">
        <div class="btn-group">
          <span class="btn-pause btn btn-warning"><i class="fa fa-pause"></i></span>
          <span class="btn-play btn btn-success"><i class="fa fa-play"></i></span>
          <span class="btn-stop btn btn-danger"><i class="fa fa-stop"></i></span>
          <span class="btn-rewind btn btn-success"><i class="fa fa-fast-backward"></i></span>
          <span class="btn-fast-forward btn btn-success"><i class="fa fa-fast-forward"></i></span>
        </div>
      <span class="audio-pos">00:00:00.0</span>
    </div>
  </div>
  <div id='playlist' data-urls='{json.dumps(stem_urls)}'>
    <input type="range" class="master-gain" min=0 max=100 value=100>
  </div>

  <script src="//code.jquery.com/jquery-2.1.4.min.js"></script>
  {read_local_asset('scripts/waveform-playlist.var.js', type='script')}
  <script type="text/javascript">
    var playlist = WaveformPlaylist.init({{
    samplesPerPixel: 3000,
    mono: true,
    waveHeight: 120,
    timescale: true,
    container: document.getElementById("playlist"),
    state: "cursor",
    colors: {{
      waveOutlineColor: "black",
      timeColor: "white",
      fadeColor: "red"
    }},
    controls: {{
      show: true,
      width: 150
    }},
    zoomLevels: [500, 1000, 3000, 5000, 10000]
  }});

  playlist
    .load(JSON.parse(document.getElementById("playlist").dataset.urls))
    .then(function() {{
      // can do stuff with the playlist.
    }});
  </script>
  {read_local_asset('scripts/emitter.js', type='script')}
</body>
    ''', height=1000)

#     else:
#         youtube_display(youtube_link)
#         logging.info('displaying video')
# else:
#   st.image("guitar.jpg", width=1000)
#   logging.info('displaying guitar')


