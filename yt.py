import pytube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
video = pytube.YouTube("www.youtube.com/watch?v=SGpr20KzoEk")
print(video.title)
print(video.thumbnail_url)
streams=video.streams
for stream in streams:
    print(stream)
