import tkinter as tk
from tkinter import ttk
win = tk.Tk()
from tkinter import *
from PIL import Image, ImageTk
from nltk.chat.util import Chat, reflections

import cv2 


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
showkbutton.grid(row=7,columnspan=5)

#showbutton = show_var.get()
#print(showbutton)

win.mainloop()
