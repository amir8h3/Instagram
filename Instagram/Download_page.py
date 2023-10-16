#******************Function********************
import instaloader
import tkinter as tk
from tkinter import *
import requests
from tkinter import filedialog
import os



def profail():


#******************Settings********************



    win = tk.Tk()
    win.title("instageram")
    win.geometry('400x410')
    win.resizable(width=True,height=True)
    # color='#38d963'
    # win.configure(bg=color)


    #******************fremes********************
    fremes1= Frame(win, width=400, height=50 )
    fremes1.pack(side="top")
    fremes2= Frame(win, width=400, height=50 )
    fremes2.pack(side="top")
    fremes3= Frame(win, width=400, height=50 )
    fremes3.pack(side="top")
    fremes4= Frame(win, width=400, height=50 )
    fremes4.pack(side="top")
    fremes5= Frame(win, width=400, height=50 )
    fremes5.pack(side="top")
    fremes7= Frame(win, width=400, height=50 )
    fremes7.pack(side="top")
    fremes8= Frame(win, width=400, height=50 )
    fremes8.pack(side="top")
    fremes9= Frame(win, width=400, height=50 )
    fremes9.pack(side="top")
    #******************Function********************


    def ok ():
        global profile
        global l
        l= instaloader.Instaloader()
        profile = instaloader.Profile.from_username(l.context, bak1.get())
        le1.config(text=f'full name: {profile.full_name}')
        le2.config(text=f'following: {profile.followees}')
        le3.config(text=f'follower: {profile.followers}')
        if profile.is_private == False:
            le5.config(text='is not private')
        else:
            le5.config(text='is private')
        if profile.is_verified == False:
            le6.config(text='is not verified')
        else:
            le6.config(text='is verified')
        
        
    def Download_profile():
        location = filedialog.askdirectory()
        os.chdir(location)
        image = requests.get(profile.get_profile_pic_url())
        with open('SabzDanesh-image.jpg', 'wb') as file:
            file.write(image.content)
        le4.config(text='Download Completed!')

    def Download_posts():
        n=1
        list1 =[]
        list2 =[] 
        location = filedialog.askdirectory()
        os.chdir(location)

        for post in profile.get_posts():
            if post.is_video == False or None:
                image = requests.get(post.url)
                with open(f'amir8h3-image{n}.jpg', 'wb') as file:
                    file.write(image.content)
            else:
                vido1 = requests.get(post.video_url)
                with open(f'amir8h3-vido{n}.mp4', 'wb') as file:
                    file.write(vido1.content)
            
            list1.append(f'posts{n} likes: {post.likes}')
            list2.append(f'posts{n} likes: {post.date}')
            n+=1
        print(m1.get())
        if m1.get() == True:
            like = tk.Tk()
            like.title("like")
            like.geometry("200x200")
            listbox = Listbox(like, selectmode=MULTIPLE)
            listbox.pack()
            for item in list1:
                listbox.insert(END, item)
        if m2.get() == True:
            date = tk.Tk()
            date.title("date")
            date.geometry("200x200")
            listbox = Listbox(date, selectmode=MULTIPLE)
            listbox.pack()
            for item in list2:
                listbox.insert(END, item)

        

    bak1 = Entry(fremes1,font=('Arial', 11), fg='#121212', borderwidth=3)
    bak1.pack(side=LEFT, padx=5, pady=5)
    dok =Button(fremes1,text='oky',command=ok,bg='#121212', fg='white', borderwidth=3, font=('Arial', 11))
    dok.pack(side=LEFT, padx=5, pady=5)






    le1 = Label(fremes2,text='full name:',font=('Arial', 11))
    le1.pack(side=LEFT, padx=5, pady=5)
    le2 = Label(fremes2,text='following:',font=('Arial', 11))
    le2.pack(side=LEFT, padx=5, pady=5)
    le3 = Label(fremes2,text='follower:',font=('Arial', 11))
    le3.pack(side=LEFT, padx=5, pady=5)
    le5 = Label(fremes3,text='',font=('Arial', 11))
    le5.pack(side=LEFT, padx=5, pady=5)
    le6 = Label(fremes3,text='',font=('Arial', 11))
    le6.pack(side=LEFT, padx=5, pady=5)


    dok2 =Button(fremes4,text='Download profile',command=Download_profile,bg='#121212', fg='white', borderwidth=3, font=('Arial', 11))
    dok2.pack(side=LEFT, padx=5, pady=5)
    le4 = Label(fremes4,text='',font=('Arial', 11))
    le4.pack(side=LEFT, padx=5, pady=5)

    dok2 =Button(fremes5,text='Download posts',command=Download_posts,bg='#121212', fg='white', borderwidth=3, font=('Arial', 11))
    dok2.pack(side=LEFT, padx=5, pady=5)
    m1 = BooleanVar()
    c1 = Checkbutton(fremes5,text='Like', borderwidth=3, font=('Arial', 11),variable=m1)
    c1.pack(side=LEFT, padx=5, pady=5)
    m2 = BooleanVar()
    Checkbutton(fremes5,text='date', borderwidth=3, font=('Arial', 11),variable=m2).pack(side=LEFT, padx=5, pady=5)





    win.mainloop()
