'''
Created on Sun 04/10/2020 03:48:07
Rock, Paper, Scissors
@author: MarsCandyBars
'''
import random

class RPC():

    def start(self):
        '''
        Description:
            This method takes user input and has error checking.
        Args:
            None.
        Returns:
            user_move
        '''
        choice = input('Choose either (A.)Rock, (B.)Paper, or (C.)Scissors:')

        if choice == 'a' or choice == 'A':
            user_move = 'Rock'
        elif choice == 'b' or choice == 'B':
            user_move = 'Paper'
        elif choice == 'c' or choice == 'C':
            user_move = 'Scissors'
        else:
            print('Invalid selection, please select either A, B, or C.')

        return user_move

    def compare(self, user_move):
        '''
        Description:
            This method prints the choice of user and computer. It also
            calculates who wins each hand.
        Args:
            user_move
        Returns:
            None.
        '''
        #Calling function
        call = RPC()

        auto_list = ['Rock', 'Paper', 'Scissors']
        auto_choice = random.choice(auto_list)
        print('YOUR CHOICE: ' + user_move + ' MY CHOICE: ' + auto_choice + '\n')
        
        if user_move == 'Rock':
            if auto_choice == 'Rock':
                print('Draw')
            elif auto_choice == 'Paper':
                print('My Paper beats your Rock. You lose!')
            elif auto_choice == 'Scissors':
                print('Rock beats Scissors. You win!')
        elif user_move == 'Paper':
            if auto_choice == 'Paper':
                print('Draw')
            elif auto_choice == 'Scissors':
                print('My Scissors beat your Paper. You lose!')
            elif auto_choice == 'Rock':
                print('Paper beats Rock. You win!')
        elif user_move == 'Scissors':
            if auto_choice == 'Scissors':
                print('Draw')
            elif auto_choice == 'Rock':
                print('My Rock beats your Scissors. You lose!')
            elif auto_choice == 'Paper':
                print('Scissors beat Paper. You win!')

#Setting up loop and replay functionality    
count = 0
while count < 50:
    call = RPC()
    user_move = call.start()
    call.compare(user_move)
    replay = input('Play again? (Y/N) ')
    print('---------------------------------------------------')
    count += 1
    #Gives the option to quit
    if replay == 'n':
        quit()

