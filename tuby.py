from pytube import YouTube

DOWNLOAD_FOLDER = '/tuby Downloads/'

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
print(yt.streams.filter(adaptive=True).all())
yt.streams.filter(only_audio=True).first().download('downloads/')