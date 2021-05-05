import youtube_dl
from time import sleep as s
from tkinter import *
from PIL import ImageTk
import sys
import os

root = Tk()
w = 1000  # width for the Tk root
h = 600  # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def download(options, link):
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            info_dict = ydl.extract_info(link)
            video_title = info_dict.get('title', None)
            download_label = Label(upper_frame,
                                   text=f'{video_title} is downloaded')
            download_label.place(relx=0.5, rely=0.5, relheight=0.1, anchor='n')
            download_label.after(2000, lambda: download_label.destroy())
        except Exception as e:
            error_label = Label(upper_frame, text={e})
            error_label.after(2000, lambda: error_label.destroy())
            error_label.place(relx=0.5, rely=0.5, relheight=0.1, anchor='n')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("./data"), relative_path)


def clear_text():
    entry.delete(0, 'end')


def get_m4a():
    link = entry.get()
    options = {
        'noplaylist': True,
        'format': 'bestaudio[ext=m4a]/bestaudio',
    }
    download(options, link)


def get_mp4():
    link = entry.get()
    options = {'noplaylist': True, 'format': 'bestvideo+bestaudio/best'}
    download(options, link)


def get_mp3():
    link = entry.get()
    options = {'noplaylist': True, 'format': 'bestaudio[ext=mp3]/bestaudio'}
    download(options, link)


def get_wav():
    link = entry.get()
    options = {'noplaylist': True, 'format': 'bestaudio[ext=wav]/bestaudio'}
    download(options, link)


def open_folder():
    os.startfile(os.getcwd())


def buttons():
    m4a = Button(upper_frame,
                 text='m4a',
                 command=lambda: [get_m4a(), clear_text()])
    m4a.place(relx=0.8, rely=0.6, relheight=0.1, relwidth=0.1, anchor='n')
    mp4 = Button(upper_frame,
                 text='best video+audio',
                 command=lambda: [get_mp4(), clear_text()])
    mp4.place(relx=0.2, rely=0.4, relheight=0.1, anchor='n')
    mp3 = Button(upper_frame,
                 text='mp3',
                 command=lambda: [get_mp3(), clear_text()])
    mp3.place(relx=0.2, rely=0.6, relheight=0.1, relwidth=0.1, anchor='n')
    wav = Button(upper_frame,
                 text='wav',
                 command=lambda: [get_wav(), clear_text()])
    wav.place(relx=0.8, rely=0.4, relheight=0.1, relwidth=0.1, anchor='n')
    open_folder_location = Button(upper_frame,
                                  text='Open download folder location',
                                  command=open_folder)
    open_folder_location.place(relx=0.5, rely=0.7, relheight=0.1, anchor='n')
    quit = Button(upper_frame,
                  text='Quit Program',
                  command=lambda: root.destroy())
    quit.place(relx=0.5, relheight=0.1, rely=0.8, anchor='n')


#application background image
background_image = ImageTk.PhotoImage(file=resource_path("background1.png"))
background_label = Label(root, image=background_image, bd=0)
background_label.place(x=0, y=0)
#upper upper_frame
upper_frame = Frame(root)
upper_frame.place(relx=0.5,
                  rely=0.1,
                  relwidth=0.75,
                  relheight=0.75,
                  anchor='n')
upper_frame_image = ImageTk.PhotoImage(file=resource_path('background2.jpg'))
upper_frame_image_label = Label(upper_frame, image=upper_frame_image)
upper_frame_image_label.place(relwidth=1, relheight=1)
#application title
title = Label(upper_frame, text='Universal Downloader', font=50)
title.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.15, anchor='n')
entry = Entry(upper_frame)
entry.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.1, anchor='n')
buttons()
root.mainloop()
