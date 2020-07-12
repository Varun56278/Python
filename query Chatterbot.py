import tkinter as tk
from tkinter import ttk
from tkinter import *
from nltk.chat.util import Chat, reflections

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
list_trainer = ListTrainer(my_bot)


small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines','c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

#print(small_talk)
#print(math_talk_1)
#print(math_talk_2)

list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)
    #print(item)

root = Tk()
topframe = Frame(root)

entry = Entry(topframe)
entry.pack()
   
topframe.pack(side = TOP)
bottomframe = Frame(root)

scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT,  fill=Y)
answer = Text(bottomframe, width=100, height=50, yscrollcommand = scroll.set)

scroll.config(command=answer.yview)
answer.pack()

bottomframe.pack()

def chatty():
    entry_value = entry.get()
    #print(entry_value)
    #answer_value = Chat(pairs, reflections)
    #res = my_bot.get_response(entry_value)
    
    #print(answer_value)
    answer.insert(INSERT, my_bot.get_response(entry_value)) #answer_value.converse()
    

button = Button(topframe, text="Submit", command=chatty)
button.pack()


root.mainloop()

