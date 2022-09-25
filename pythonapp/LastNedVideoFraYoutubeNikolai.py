from __future__ import unicode_literals
import ffmpeg
import youtube_dl


ydl_opts = {'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=oolpPmuK2I8&list=PLycVTiaj8OI-kwvNjgvvopMJt__x-y5mD'])
