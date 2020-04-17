'''
Created on Sun 04/17/2020 18:15:41
Higher Lower Guessing Game
@author: MarsCandyBars
'''

#Program was short and simple, so it is layed out
#linearly
import random

#Using random to represent the computers
#number
item = random.randint(1, 100)
counter = 0

#Introduction
print('HIGHER LOWER GUESSING GAME')
print('The computer will pick a number between 1 and 100. '
      'The object of the game is to guess the number '
      'the computer has chosen. Each turn the computer '
      'will tell you if your guess is higher or lower '
      'than the answer.\n')

#Looping through, 100 chances
while counter < 100:
    counter += 1
    guess = int(input('Guess the number:'))
    if guess > item:
        print('Your guess is higher.')
    elif guess < item:
        print('Your guess is lower.')
    else:
        print('\nYou guessed it! You win!')
        print('Number of guesses:', counter)
        replay = input('Play again? (Y/N)\n')

        #Giving the ability to replay
        if replay == 'y':
            continue
        else:
            quit()
