import os
import tkinter
import customtkinter
from pytube import YouTube


# Function to download the YouTube Video
def download_video():
    try:
        url = url_var.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()

        download_folder = os.path.expanduser("~") + "/Downloads"

        title.configure(text=video.title, text_color="white")
        finishedLabel.configure(text="")
        video.download(download_folder)
        finishedLabel.configure(text="Video Downloaded", text_color="green")
    except:
        finishedLabel.configure(text="Error: Video not found", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    amount_downloaded = total_size - bytes_remaining
    per_downloaded = amount_downloaded / total_size * 100
    per = str(int(per_downloaded))
    percentage.configure(text=per + '%', text_color="white")  # Update the progress
    percentage.update()
    progressBar.set(float(per_downloaded) / 100)  # Update the progress bar


# System Settings
customtkinter.set_appearance_mode("System")  # default appearance of system settings
customtkinter.set_default_color_theme("blue")

# Our Application framework
app = customtkinter.CTk()
app.geometry("720x480")  # Set the size of the window
app.title("YouTube Video Downloader")  # Set the title of the window

# Addition of UI elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Video URL")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=download_video)
download.pack(padx=10, pady=10)

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=350)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

# Finished Downloading
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# Run the application
app.mainloop()
