import threading
import subprocess
import os
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import youtubeQuery
import sys
import shutil

#This is a huge mess that needs to be cleaned up btw
#will get to it """eventually"""(tm)

DOWNLOAD_FOLDER = 'downloads/'
TEMP_FOLDER = 'downloads/_tmp'
FFMPEG_LOC = 'C:/Program Files/FFMPEG/ffmpeg.exe'
RESULT = 'http://youtube.com/watch?v=9bZkp7q19f0'
placeholder_text = 'search...'

def getVideoDownload(src):
    src = youtubeQuery.search(src)
    src = YouTube(src)
    print('Downloading...')
    src.streams.filter(subtype='mp4').first().download(DOWNLOAD_FOLDER)

    print('Download Finished...')
    searchEntry.delete(0, 'end')

root = Tk()
root.title("Tuby")
root.geometry("360x360+0+0")
root.minsize(width=360, height=360)
root.maxsize(width=900, height=360)
#root.iconbitmap("icon.ico")
root.configure(background='#DADADA')

root.grid_columnconfigure(0, weight=1, uniform="group1")
root.grid_columnconfigure(1, weight=1, uniform="group1")

userSearch = StringVar()
searchEntry = Entry(root,text="search...", textvariable=userSearch, font="Helvetica 22 bold", borderwidth="0", fg="#8F8F8F")
searchEntry.grid(row=0, column=0, columnspan=2, ipadx=10, sticky="new", pady=(10,0))


#class getAudioDownload(threading.Thread):
#    def run(self):
#        src = str(threading.currentThread().getName())
#        src = youtubeQuery.search(src)
#        src = YouTube(src)
#        print('Downloading...')
#        src.streams.filter(only_audio=True).first().download(DOWNLOAD_FOLDER)
#        print('Download Finished...')
#
def FFMPEGCheck():
    if os.path.isfile('C:/Program Files/FFMPEG/ffmpeg.exe'):
        print("True")
    else:
        print("C:/Program Files/FFMPEG/ffmpeg.exe")
        messagebox.askyesno("Tuby", '"' + str(FFMPEG_LOC) + '"' + ' not found! FFMPEG is required for .mp3 downloads. Do you wish to download FFMPEG?')

def startAudioDownload():
    getAudioThread = threading.Thread(target=lambda: getAudioDownload((userSearch.get())))
    getAudioThread.start()

def startVideoDownload():
    getVideoThread = threading.Thread(target=lambda: getVideoDownload((userSearch.get())))
    getVideoThread.start()

def getAudioDownload(src):
    downloadSuccess(str(src))
    src = youtubeQuery.search(src)
    src = YouTube(src)
    print('Downloading...')
    src.streams.filter(only_audio=True).first().download(DOWNLOAD_FOLDER)
    print('Download Finished...')



def downloadSuccess(MEDIA):
    searchEntry.delete(0, 'end')
    messagebox.showinfo("Tuby", '"' + str(MEDIA) + '"' + ' is Downloading!')
    searchEntry.insert(0, placeholder_text)

def openFolder():
     cwd = os.getcwd()
     cwd = str(cwd + "\downloads")
     subprocess.Popen('explorer ' + str(cwd))
     print("Opening..." + str(cwd))

def writeToDisk():
    messagebox.showinfo("Tuby", 'Not yet available :( Write to Disk feature coming soon!')


listbox = Listbox(root, bg="#C3C3C3", borderwidth="0", font="Helvetica 9 bold")
listbox.grid(row=1, column=0, columnspan=2, sticky="new")
def listResults(src):
    for item in youtubeQuery.getResults(src):
        listbox.insert(END, item)


downloadVideo = Button(root, borderwidth="0", bg="#D82523", fg="white", font="Helvetica 13 bold", text="Download Video", command=(lambda: startVideoDownload()))
downloadVideo.grid(row=2, column=0, columnspan=2, sticky="new")
downloadAudio = Button(root, borderwidth="0", bg="#B11F1D", fg="white", font="Helvetica 13 bold", text="Download Audio", command=(lambda: startAudioDownload()))
downloadAudio.grid(row=3, column=0, columnspan=2, sticky="new")
openFolderButton = Button(root, borderwidth="0", bg="#C3C3C3", text="Open", font="Helvetica 13 bold", command=(lambda: openFolder()))
openFolderButton.grid(row=5, column=0, sticky="nsew", pady=(10,10), padx=(10,5), rowspan=2)
writeToDiskButton = Button(root, borderwidth="0", bg="#C3C3C3", text="Write", font="Helvetica 13 bold", command=(lambda: writeToDisk()))
writeToDiskButton.grid(row=5, column=1, sticky="nsew", pady=(10,10), padx=(5,10), rowspan=2)

#getAudioThread = getAudioDownload(name=userSearch.get())
#getAudioThread.start()


#statusframe = Frame(root)
#statusframe.pack(side=BOTTOM, fill=X)
#status = Label(statusframe, text="Tuby // Created by Robert Carroll", bg="#DADADA", font="Helvetica 7", fg="grey", anchor=W)
#status.pack(side=BOTTOM, expand=True)

def clear_entry(event, searchEntry):
    searchEntry.delete(0, END)

searchEntry.bind("<Button-1>", lambda event: clear_entry(event, searchEntry))

searchEntry.insert(0, placeholder_text)

def clear_temp():
    try:
        shutil.rmtree(TEMP_FOLDER)
    except:
        print("Error:")

def create_downloads():
    try:
        os.makedirs(DOWNLOAD_FOLDER)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

create_downloads()

root.mainloop()

clear_temp()



