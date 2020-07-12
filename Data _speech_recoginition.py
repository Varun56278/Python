import speech_recognition as sr
import mysql.connector
from chatbot import *
from photo import *
from voice import *
from speak import *
from validate import *
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
from tkinter import *

win.title('sachin')



Name = tk.Label(win, text='WELCOME TECH VISION ')
Name.grid(row=0, column=0, sticky=tk.W)
Name.configure(foreground='Red')

Email = tk.Label(win, text='Enter your Email : ')
Email.grid(row=1, column=0, sticky=tk.W)
Email.configure(foreground='Blue')

Password = tk.Label(win, text='Enter your Password : ')
Password.grid(row=2, column=0, sticky=tk.W)
Password.configure(foreground='Blue')




Click = tk.Label(win, text='CREATE A NEW ACCOUNT , ITS QUICK AND EASY.\n ')
Click.grid(row=4, column=0, sticky=tk.W)
Click.configure(foreground='Red')


name = tk.Label(win, text='Enter your name : ')
name.grid(row=5, column=0, sticky=tk.W)
name.configure(foreground='Blue')

age = tk.Label(win, text='Enter your age : ')
age.grid(row=6, column=0, sticky=tk.W)
age.configure(foreground='Blue')


email = tk.Label(win, text='Enter your email : ')
email.grid(row=7, column=0, sticky=tk.W)
email.configure(foreground='Blue')

password = tk.Label(win, text='Enter your password : ')
password.grid(row=8, column=0, sticky=tk.W)
password.configure(foreground='Blue')



gender = tk.Label(win, text='Enter your gender : ')
gender.grid(row=9, column=0, sticky=tk.W)
gender.configure(foreground='Blue')

#create entry box
Email_var = tk.StringVar()
Email_entrybox = tk.Entry(win, width=16, textvariable= Email_var)
Email_entrybox.grid(row=1, column=1)
Email_entrybox.configure(foreground='green')


Password_var = tk.StringVar()
Password_entrybox = tk.Entry(win, width=16, textvariable= Password_var)
Password_entrybox.grid(row=2, column=1)
Password_entrybox.configure(foreground='green')


name_var = tk.StringVar()
name_entrybox = tk.Entry(win, width=16, textvariable= name_var)
name_entrybox.grid(row=5, column=1)
name_entrybox.configure(foreground='green')

age_var = tk.StringVar()
age_entrybox = tk.Entry(win, width=16, textvariable= age_var)
age_entrybox.grid(row=6, column=1)
age_entrybox.configure(foreground='green')

email_var = tk.StringVar()
email_entrybox = tk.Entry(win, width=16, textvariable= email_var)
email_entrybox.grid(row=7, column=1)
email_entrybox.configure(foreground='green')

password_var = tk.StringVar()
password_entrybox = tk.Entry(win, width=16, textvariable= password_var)
password_entrybox.grid(row=8, column=1)
password_entrybox.configure(foreground='green')



#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable=gender_var, state= 'readonly')
gender_combobox['values'] = ('Male', 'Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=9, column=1)


#check button
checkbutton_var = tk.IntVar()
checkbutton = ttk.Checkbutton(win, text='By clicking Sign Up, you agree to our Terms, Data Policy and Cookie Policy. You may receive SMS notifications from us and can opt out at any time',variable=checkbutton_var)
checkbutton.grid(row=12,columnspan=3)
#create button


def login():
    Email = Email_var.get()
    Password = Password_var.get()
    mydb = mysql.connector.connect(host="localhost",user="root",password="Sachin",database="db")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM details")
    data = mycursor.fetchall()
    
    is_login = False
    for col in data:
        if col[2] == Email and col[3] ==  Password:
            is_login = True


        if is_login==True:
            print('login_sucess')
            win = tk.Tk()
            win.title("mahi")
            record_button = Button(win, text="Record",command=record)
            record_button.grid(row=2, column=0)
            photo_button = Button(win, text="Image",command=showimage)
            photo_button.grid(row=4, column=0)
            chatbot_button = Button(win, text="Chat",command=chatty)
            chatbot_button.grid(row=10, column=0)

        else:
                print('user id and password is not valid , plz try again')
                      

    
    Email_entrybox.delete(0, tk.END)
    Password_entrybox.delete(0, tk.END)
                    
    
submit_button = tk.Button(win, text='LOGIN',command=login)
submit_button.grid(row=3, column=0)

def forget():
    AUDIO_FILE = ("output.wav")
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        try:
            print("The audio file contains: " + r.recognize_google(audio))
            win = tk.Tk()
            win.title("book")
            speak_button = Button(win, text="SPEAK",command=speak)
            speak_button.grid(row=2, column=0)
            validate_button = Button(win, text="VALIDATE",command=validate)
            validate_button.grid(row=2, column=6)
            
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

submit_button = tk.Button(win, text='FORGET PASSWORD',command=forget)
submit_button.grid(row=3, column=6)
          


    

def action():
    name = name_var.get()
    age = age_var.get()
    email = email_var.get()
    password = password_var.get()

    print(f'{name} is {age} years old ,{email} , {password}')
    gender = gender_var.get()
    if checkbutton_var.get() ==0:
        subscribed = 'NO'
    else:
        subscribed = 'Yes'
    print(gender, subscribed)

    mydb = mysql.connector.connect(host="localhost",user="root",password="Sachin",database="db")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE details (name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255), gender VARCHAR(255))")
    mycursor.execute("INSERT INTO details values('"+ name +"','"+ age +"','"+ email +"','"+ password +"','"+ gender +"')")  
    mydb.commit()
    mydb.close()

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    password_entrybox.delete(0, tk.END)
    
    
submit_button = tk.Button(win, text='SIGNUP',command=action)
submit_button.grid(row=14, column=0)

win.mainloop()




