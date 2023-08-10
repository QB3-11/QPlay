from pytube import YouTube
from sys import argv
 

defaultpath = "//home//qb3//Music"

def download(url, title = None, path = defaultpath):
    video = YouTube(url)
    file = video.streams.get_by_itag(251)
    file.download(output_path=path, filename=title)

if len(argv) == 3:
    download(argv[1], argv[2])

elif len(argv) == 4:
    download(argv[1], argv[2], argv[3])

else:
    download(argv[1])
