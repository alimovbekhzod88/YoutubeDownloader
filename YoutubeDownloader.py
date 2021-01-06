from pytube import YouTube
from tkinter import messagebox, filedialog
from tkinter import *

def widgets():
    url_link  = Label(root, text="YouTube link :", bg="#05E8E0")
    url_link.grid(row = 1, column = 0, pady = 5, padx=5)

    LinkText = Entry(root, width = 55, textvariable = video_link)
    LinkText.grid(row =1, column=1, padx=5, pady=5, columnspan=2)

    detination_label = Label(root, text="Destination link :", bg="#05E8E0")
    detination_label.grid(row = 2, column = 0, padx = 5, pady=5)

    destinationText = Entry(root, width = 40, textvariable = destination_link)
    destinationText.grid(row=2, column=1, padx = 5, pady = 5)

    browse_button = Button(root,text="Browse", command = Browse, width = 10, bg="#E8D579")
    browse_button.grid(row = 2, column = 2, padx = 1, pady = 1)

    download_button = Button(root, text = "Download", command = Download, width=10, bg="#E8D579")
    download_button.grid(row=3, column=1, padx=3, pady=3)


def Browse():
    #directory selection
    download_directory = filedialog.askdirectory(initialdir= "Your directory path")
    #Displaying folder to the text area
    destination_link.set(download_directory)

def Download():
    Youtube_link = video_link.get()
    download_folder = destination_link.get()
    videoStream = YouTube(Youtube_link).streams.get_highest_resolution().download(download_folder)   # get video hight format
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_folder)

root = Tk()
root.geometry('600x120')
root.resizable(False, False)
root.title("Video Downloader")
root.config(background="#f00")

video_link = StringVar()
destination_link = StringVar()
widgets()
root.mainloop()
