'''
Created on Sun 04/07/2020 09:36:32
Magic 8 Ball
@author: MarsCandyBars
'''

#Program uses TKinter for Magic 8 Ball UI.
from tkinter import *
import random
import time

root = Tk()

#Gives program ending functionality to the 'Quit' button
def kill():
    quit()

#Cleans entry widget
def clean():
    entry.delete(0, END)

#Gives a response when 'Ask' button is clicked
def ask():
    global label_response
    
    response = ["I'm not sure.", 'Yes!', 'No!', 'Cannot determine at this time.',
                'It is certain.', 'I hope so.', 'Hmmmmm...', 'Maybe so.',
                "I wouldn't count on it!", 'Anything is possible.', 'I guess..',
                 'You should speak to a professional.', 'I shall make it so.',
                "I'm not sure, but you're pretty cool!", 'Ask again later.',
                 'It is not in the cards today.', 'Whatever you want.',
                'My sources tell me...Yes!', 'Thats a tough one.', 'Cough...Cough...']
    
    response_text = random.choice(response)
    label_response = Label(root,
                           text = response_text,
                           borderwidth = 2,
                           bg = '#61efce',
                           relief="solid")
    label_response.pack()
    button_ask['state'] = DISABLED

#Clears label_response to give the effect of a replay    
def replay():
    label_response.destroy()
    button_ask['state'] = NORMAL

#UI improvements
root.geometry("275x250")
root.config(bg = '#343233')
root.title("Magic 8 Ball")

#Initial dialogue for the game
label_one = Label(root,
                  fg = '#eed9b7',
                  bg = '#343233',
                  text = "I'm the Magic 8 Ball. Ask me anything!")
label_one.config(font = 'Arial')
label_one.pack()

#Entry widget
entry = Entry(root, bg = '#efdab9', width = 25)
entry.pack()
entry.insert(0, "")

#Ask button
button_ask = Button(root,
                    text = "Ask",
                    bg = '#ffd152',
                    command = lambda: [ask(), clean()])
button_ask.pack(pady = (5,5))

#Clean button
button_clean = Button(root,
                      text = "Clear",
                      bg = '#ffd152',
                      command = clean)
button_clean.pack()

#Play Again button
button_replay = Button(root,
                       text = "Play Again",
                       bg = '#ffd152',
                       command = replay)
button_replay.pack(pady = (5,5))

#Quit button
button_quit = Button(root,
                     text = "Quit",
                     bg = '#ffd152',
                     command = kill)
button_quit.pack()

#root.mainloop()
