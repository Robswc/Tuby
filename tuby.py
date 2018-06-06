from threading import Thread
import subprocess
import os
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import youtubeQuery
import sys
from pydub import AudioSegment

#def getAudioDownload(src):
#    src = youtubeQuery.search(src)
#    src = YouTube(src)
#    print('Downloading...')
#    src.streams.filter(only_audio=True).first().download(DOWNLOAD_FOLDER)
#    print('Download Finished...')


def getVideoDownload(src):
    src = youtubeQuery.search(src)
    src = YouTube(src)
    print('Downloading...')
    src.streams.filter(only_audio=True).first().download(DOWNLOAD_FOLDER)

    print('Download Finished...')
    searchEntry.delete(0, 'end')


DOWNLOAD_FOLDER = 'downloads/'
RESULT = 'http://youtube.com/watch?v=9bZkp7q19f0'
placeholder_text = 'search...'


root = Tk()
root.title("Tuby")
root.geometry("360x512+0+0")
root.iconbitmap("icon.ico")
root.configure(background='#DADADA')

userSearch = StringVar()
searchEntry = Entry(root,text="search...", textvariable=userSearch, font="Helvetica 22 bold", borderwidth="0")
searchEntry.pack(fill=X, padx=(10,10), pady=(10,10))

#class getAudioDownload(threading.Thread):
#    def run(self):
#        src = str(threading.currentThread().getName())
#        src = youtubeQuery.search(src)
#        src = YouTube(src)
#        print('Downloading...')
#        src.streams.filter(only_audio=True).first().download(DOWNLOAD_FOLDER)
#        print('Download Finished...')
#


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



listbox = Listbox(root, bg="#C3C3C3", borderwidth="0", font="Helvetica 13 bold")
def listResults(src):
    for item in youtubeQuery.getResults(src):
        listbox.insert(END, item)
listResults("gangnam style")
listbox.pack(fill=X, padx=(10,10), pady=(0,10))
downloadAudio = Button(root, borderwidth="0", bg="#548235", fg="white", font="Helvetica 13 bold", text="Audio", command=(lambda: getAudioDownload(userSearch.get())))
downloadVideo = Button(root, borderwidth="0", bg="#2F5597", fg="white", font="Helvetica 13 bold", text="Video", command=(lambda: getVideoDownload(userSearch.get())))
openFolderButton = Button(root, borderwidth="0", bg="#C3C3C3", text="Open", command=(lambda: openFolder()))
writeToDiskButton = Button(root, borderwidth="0", bg="#C3C3C3", text="Write", command=(lambda: getVideoDownload(userSearch.get())))
status = Label(root, text="Tuby // Created by Robert Carroll", bg="#DADADA", font="Helvetica 7", fg="grey", anchor=W)

#getAudioThread = getAudioDownload(name=userSearch.get())
#getAudioThread.start()

downloadAudio.pack(fill=X, padx=(10,10))
downloadVideo.pack(fill=X, padx=(10,10))
openFolderButton.pack(fill=X, padx=(10,5), pady=(10,10))
writeToDiskButton.pack(fill=X, padx=(5,10), pady=(10,10))
status.pack(side=BOTTOM, fill=X)

def clear_entry(event, searchEntry):
    searchEntry.delete(0, END)

searchEntry.bind("<Button-1>", lambda event: clear_entry(event, searchEntry))

searchEntry.insert(0, placeholder_text)
root.mainloop()





