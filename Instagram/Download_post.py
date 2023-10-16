#******************Function********************
import instaloader
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import threading



def Download_post():
#******************Settings********************
    win_post = tk.Tk()
    win_post.title("instageram")
    win_post.geometry('300x210')
    win_post.resizable(width=True,height=True)
#******************Function Download post********************
    def Download_p ():
        link = bak1.get()
        print(link)
        def download():
            if 'https://www.instagram.com/' in link:
                try:
                    location = filedialog.askdirectory()
                    os.chdir(location)
                    a = link.find("/",26)
                    b = link.find("/",a+3)
                    URL = link[a+1:b]
                    L = instaloader.Instaloader()
                    post = instaloader.Post.from_shortcode(L.context, URL)
                    L.download_post(post, target=URL)
                    messagebox.showinfo('Info', 'Download Compeleted!')
                except:
                    messagebox.showerror('Error', 'URL IS INCORRECT')
            else:
                messagebox.showerror('Error', 'URL NOT FOUND')
        
        threading.Thread(target=download).start()


#******************fremes********************
    fremes1_asli= Frame(win_post, width=400, height=50 )
    fremes1_asli.pack(side="top")
    fremes2_asli= Frame(win_post, width=400, height=50 )
    fremes2_asli.pack(side="top")
    fremes3_asli= Frame(win_post, width=400, height=50 )
    fremes3_asli.pack(side="top")




    bak1 = Entry(fremes1_asli,font=('Arial', 11), fg='#121212', borderwidth=3, width=35)
    bak1.pack(side=LEFT, padx=5, pady=5)

    dok =Button(fremes2_asli,text='download', bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30,command=Download_p)
    dok.pack(side=LEFT, padx=5, pady=5)

    exit_btn = Button(fremes3_asli, text='Exit', bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30, command=win_post.destroy)
    exit_btn.pack(side=LEFT, padx=5, pady=5)   


    win_post.mainloop()

