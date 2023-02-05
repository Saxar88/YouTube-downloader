import tkinter
import customtkinter
from pytube import YouTube
import os

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if format.get() == "mp3":
            file = ytObject.streams.get_audio_only()
            file.download()
            base = os.path.splitext(file)
            new_file = base + '.mp3'
            os.rename(file, new_file)
        else:
            file = ytObject.streams.get_highest_resolution()
            file.download()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        finishLabel.configure(text="Donwload complete!", text_color="green")
    except:
        finishLabel.configure(text="Invalid link", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = bytes_downloaded / total_size * 100
    per = str(int(percent_completed))
    progressPercentage.configure(text = per + "%")
    progressPercentage.update()
    progressBar.set(float(percent_completed) / 100)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text="Insert YouTube link:")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,  textvariable=url_var)
link.pack()

format = tkinter.StringVar(value="mp3")
radiobutton_mp3 = customtkinter.CTkRadioButton(master=app, text="mp3", variable=format, value="mp3")
radiobutton_mp3.pack(padx=20, pady=10)
radiobutton_hd = customtkinter.CTkRadioButton(master=app, text="HD", variable=format, value="HD")
radiobutton_hd.pack(padx=20, pady=10)

finishLabel = customtkinter.CTkLabel(app,  text="")
finishLabel.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

progressPercentage = customtkinter.CTkLabel(app, text="0%")
progressPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

app.mainloop()