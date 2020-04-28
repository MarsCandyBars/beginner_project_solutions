'''
Created on Sun 04/28/2020 18:42:19
Hangman Game
@author: MarsCandyBars
'''

import random

#All functions contain pictures for each
#phase of the game
def pic1():
        print("""\

              ______
             |    |
             |    |
                  |
                  |
                  |
                  |
                  |
           ===========


        """)

def pic2():
        print("""\

              ______
             |    |
             |    |
             O    |
                  |
                  |
                  |
                  |
           ===========


        """)

def pic3():
        print("""\

              ______
             |    |
             |    |
             O    |
             |    |
                  |
                  |
                  |
           ===========


        """)

def pic4():
        print("""\

              ______
             |    |
             |    |
             O    |
             |\   |
                  |
                  |
                  |
           ===========


        """)

def pic5():
        print("""\

              ______
             |    |
             |    |
             O    |
            /|\   |
                  |
                  |
                  |
           ===========


        """)

def pic6():
        print("""\

              ______
             |    |
             |    |
             O    |
            /|\   |
            /     |
                  |
                  |
           ===========


        """)

def pic7():
        print("""\

              ______
             |    |
             |    |
             O    |
            /|\   |
            / \   |
                  |
                  |
           ===========


        """)



#Initializing blank list for spaces
blank = []
#Initializing list to hold wrong answers
wrong_list = []
#The word bank is for random word selection
word_bank = ['boots','neptune','castle','gorilla','pumpkin']

#This section chooses a random word and shows the initial
#picture
word_random = random.choice(word_bank)
word = list(word_random)
pic1()

#Initializing the number of tries and count for
#seeing if the answer was correct
tries = 6
count = 0

#Using len() to set spaces length for word
for i in range(0, len(word)):
        blank.append('_')

#Repeats guess input
while True:
        if str(blank) == str(word):
                print('YOU WIN!')
                quit()

        guess = input('GUESS: ')
        for i in range(0, len(word)):

                if word[i] == guess:
                        blank[i] = guess
                        print('CORRECT:')
                        print(blank)

                        print('WRONG:')
                        print(wrong_list, '\n')
                        count += 1
                        
        #Prints each picture depending on the stage of the game                
        if count == 0:
                tries -= 1
                wrong_list.append(guess)
                if tries == 5:
                        pic2()
                elif tries == 4:
                        pic3()
                elif tries == 3:
                        pic4()
                elif tries == 2:
                        pic5()
                elif tries == 1:
                        pic6()

                print('CORRECT:')
                print(blank)

                print('WRONG:')
                print(wrong_list, '\n')
        else:
                count = 0

        if tries == 0:
                pic7()
                print('YOU LOSE!')
                quit()

                
