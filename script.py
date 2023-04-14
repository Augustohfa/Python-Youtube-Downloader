from pytube import YouTube
from pytube import Playlist
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

get_video_url = input('Type video URL: ')

yt = YouTube(get_video_url)

print(yt.thumbnail_url)  # Get thubmail URL

yt.streams.first().download()
# Creating a playlist with PyTube

get_yt_playlist = input('Type the playlist URL: ')
yt_playlist = Playlist(get_yt_playlist)

for video in yt_playlist.videos:
    video.streams.first().download

# Can also just print the URL's

for url in yt_playlist.video_urls:
    print(url)

# Currently working