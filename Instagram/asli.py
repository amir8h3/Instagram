#******************Function********************
import instaloader
import tkinter as tk
from tkinter import *
import requests
from tkinter import *
from Download_page import *
from Download_post import *


#******************Settings********************
win_asli = tk.Tk()
win_asli.title("instageram")
win_asli.geometry('600x310')
win_asli.resizable(width=True,height=True)



#******************fremes********************
fremes1_asli= Frame(win_asli, width=400, height=50 )
fremes1_asli.pack(side="top")
fremes2_asli= Frame(win_asli, width=400, height=50 )
fremes2_asli.pack(side="top")

le1_asli = Label(fremes1_asli,text='Download from the page :', font=('Arial', 11), width=25)
le1_asli.pack(side=LEFT, padx=5, pady=5)

dok_asli =Button(fremes1_asli,text='Download',command=profail,bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30)
dok_asli.pack(side=LEFT, padx=5, pady=5)


le2_asli = Label(fremes2_asli,text='Download post :',font=('Arial', 11), width=25)
le2_asli.pack(side=LEFT, padx=5, pady=5)

dok2_asli =Button(fremes2_asli,text='Download',command=Download_post,bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30)
dok2_asli.pack(side=LEFT, padx=5, pady=5)


win_asli.mainloop()
