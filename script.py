from pytube import YouTube
from sys import argv
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

yt = YouTube("https://www.youtube.com/watch?v=vEQ8CXFWLZUnk")

print(yt.thumbnail_url)
