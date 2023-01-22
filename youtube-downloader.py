from pytube import YouTube
import os

yt = YouTube(
    str(input("Enter YouTube link: \n>> ")))

format = int(input("1. mp3 or 2. HD video: \n>> "))

try:
    video = yt.streams.filter(only_audio=True).first() if format == 1 else yt.streams.get_highest_resolution() if format == 2 else "Try again!"

    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
  
    out_file = video.download(output_path=destination)
  
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

except:
    print("An error has occurred")

print(yt.title + " has been successfully downloaded.")