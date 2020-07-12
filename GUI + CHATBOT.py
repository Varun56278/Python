import tkinter as tk
from tkinter import ttk
win = tk.Tk()
from tkinter import *
from PIL import Image, ImageTk
from nltk.chat.util import Chat, reflections

import cv2 


from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
win.title('sachin')
name = tk.Label(win, text='Enter your name : ')
name.grid(row=0, column=0, sticky=tk.W)
name.configure(foreground='Blue')

age = tk.Label(win, text='Enter your age : ')
age.grid(row=1, column=0, sticky=tk.W)
age.configure(foreground='Blue')

email = tk.Label(win, text='Enter your email : ')
email.grid(row=2, column=0, sticky=tk.W)
email.configure(foreground='Blue')
win.mainloop

gender = tk.Label(win, text='Enter your gender : ')
gender.grid(row=3, column=0, sticky=tk.W)

#create entry box
name_var = tk.StringVar()
name_entrybox = tk.Entry(win, width=16, textvariable= name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.configure(foreground='green')

age_var = tk.StringVar()
age_entrybox = tk.Entry(win, width=16, textvariable= age_var)
age_entrybox.grid(row=1, column=1)
age_entrybox.configure(foreground='green')

email_var = tk.StringVar()
email_entrybox = tk.Entry(win, width=16, textvariable= email_var)
email_entrybox.grid(row=2, column=1)
email_entrybox.configure(foreground='green')

gender_var = tk.StringVar()
gender_entrybox = tk.Entry(win, width=16, textvariable= gender_var)
gender_entrybox.grid(row=3, column=1)

#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable=gender_var, state= 'readonly')
gender_combobox['values'] = ('Male', 'Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

#radio button
usertype = tk.StringVar()
Radiobutton = ttk.Radiobutton(win, text= 'Student', value='Student', variable=usertype)
Radiobutton.grid(row=4, column=0)

usertype = tk.StringVar()
Radiobutton = ttk.Radiobutton(win, text= 'Teacher', value='Teacher', variable=usertype)
Radiobutton.grid(row=4, column=1)

#check button
checkbutton_var = tk.IntVar()
checkbutton = ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter',variable=checkbutton_var)
checkbutton.grid(row=5,columnspan=3)
#create button

def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()

    print(f'{username} is {userage} years old , {useremail}')
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbutton_var.get() ==0:
        subscribed = 'NO'
    else:
        subscribed = 'Yes'
    print(user_gender, user_type, subscribed)

    with open('file.txt','a') as f:
        f.write(f'{username},{userage},{useremail},{useremail},{user_gender},{user_type},{subscribed}\n')

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    
    
submit_button = tk.Button(win, text='Submit',command=action)
submit_button.grid(row=6, column=0)


#showbutton
def showimage():
    
    image = cv2.imread(r'C:\Users\varun\OneDrive\Desktop\bird.jpg') 

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   

  
  
    cv2.imshow('image', image)

showkbutton = tk.Button(win, text='show button',command=showimage)
showkbutton.grid(row=7,columnspan=5,sticky=tk.W)

#showbutton = show_var.get()
#print(showbutton)

def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

showkbutton = tk.Button(win, text='chatty',command=chatty)
showkbutton.grid(row=8,columnspan=6,sticky=tk.W)



win.mainloop()
