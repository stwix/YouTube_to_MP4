import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets():
    link_label = Label(root,text="Lien YouTube :",bg="#E8D579")
    link_label.grid(row=1,column=0,pady=5,padx=5)
    root.linkText = Entry(root,width=55,textvariable=video_Link)
    root.linkText.grid(row=1,column=1,pady=5,padx=5,columnspan = 2)
    destination_label = Label(root,text="Destination :",bg="#E8D579")
    destination_label.grid(row=2,column=0,pady=5,padx=5)
    root.destinationText = Entry(root,width=44,textvariable=download_Path)
    root.destinationText.grid(row=2,column=1,pady=5,padx=5)
    recherche_B = Button(root,text="Recherche",command=Recherche,width=9,bg="#05E8E0")
    recherche_B.grid(row=2,column=2,pady=1,padx=1)
    Download_B = Button(root,text="Download",command=Download,width=20,bg="#05E8E0")
    Download_B.grid(row=3,column=1,pady=3,padx=3)
def Recherche():
    download_Directory = filedialog.askdirectory(initialdir="Votre dossier de sauvegarde")
    download_Path.set(download_Directory)
def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("Parfait !","Télechargé et sauvgardé dans \n"+ download_Folder)
root = tk.Tk()
root.geometry("600x120")
root.resizable(False, False)
root.title("YouTube Downloader by Enzo")
root.config(background="#000000")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()