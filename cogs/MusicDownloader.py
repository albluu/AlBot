import youtube_dl

class MusicDownloader():

    def __init__(self):
        print('hello')

    ytdl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

    def download_audio(self, url: str):
        '''Downloads audio using youtube_dl and ffmpeg to convert'''
        with youtube_dl.YoutubeDL(self.ytdl_opts) as ydl:
            ydl.download([url])