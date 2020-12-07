# from IPython.display import HTML, Audio, display, IFrame
# import librosa
import youtube_dl
import os


EMBED_BASE = "https://www.youtube.com/embed/%s?rel=0&amp;controls=0&amp;showinfo=0"

class YouTubeTools():

    def __init__(self, full_url='https://www.youtube.com/watch?v=yPYZpwSpKmA'):
        self.url = full_url.split("watch?v=", 1)[1]

    # def get_embed(self):
    #     '''
    #     this method takes the input url and returns
    #     the youtube video in embedded HTML format
    #     '''
    #     embed_url = EMBED_BASE % (self.url)
    #     # return HTML('<iframe width="560" height="315" src=' + embed_url + 'frameborder="0" allowfullscreen></iframe>')
    #     return IFrame(src=embed_url, width=560, height=315)

    def give_url(self):
        return self.url

    def get_audio_and_directory(self):
        '''
        takes the url link, downloads the audio,
        returns the name of the file to be used
        '''

        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '44100',
        }],
        'outtmpl': 'song.wav',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            status = ydl.download([self.url])

        self.file_name = 'song.wav'

        return self.file_name

    def clear_wavs(self):
        '''
        checks and deletes any .wav files from directory to keep it clean
        '''

        files_in_directory = os.listdir()
        filtered_files = [file for file in files_in_directory if file.endswith('.wav')]
        if filtered_files == []:
            return 'No files to delete'
        else:
            for file in filtered_files:
                os.remove(file)

        return 'Clear complete'


