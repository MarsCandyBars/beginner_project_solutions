'''
Created on Sun 04/07/2020 11:00:02
Pythagorean Triple
@author: MarsCandyBars
'''
import math

class Calculate():

    def __init__(self):
        '''
        Description:
            This method contains attributes that provide responses.
        Args:
            None.
        Returns:
            affirmative, negative
        '''
        
        affirmative = ('This is a pythagorean triple.')
        self.affirmative = affirmative

        negative = ('This is not a pythagorean triple.')
        self.negative = negative
        
    def list_input(self):
        '''
        Description:
            This method prompts the user 3 times in order to
            get all the sides of the triangle.
        Args:
            None.
        Returns:
            sides
        '''

        #Set counter for loop and creates list to store sides
        count = 0
        sides = []
        
        while count < 3:
            answers = float(input('Please enter the sides of the triangle: '))
            sides.append(answers)
            count += 1
        return sides

    def pythag_check(self, sides):
        '''
        Description:
            This method utilizes a^2 + b^2 = c^2 to determine if
            any variant of sides entered is a pythagorean triple.
        Args:
            sides
        Returns:
            None.
        '''
        
        call = Calculate()
        num1 = ((sides[0] ** 2) + (sides[1] ** 2))
        num2 = (sides[2] ** 2)

        num3 = ((sides[2] ** 2) + (sides[1] ** 2))
        num4 = (sides[0] ** 2)

        num5 = ((sides[2] ** 2) + (sides[0] ** 2))
        num6 = (sides[1] ** 2)

        #Checks if any variant of the list is valid
        if num1 == num2:
            print(call.affirmative)
        elif num3 == num4:
            print(call.affirmative)
        elif num5 == num6:
            print(call.affirmative)
        else:
            print(call.negative)

#Prints title of program, calls class, and passes pythag_check the
#list from list_input. This is looped so that users may enter up to
#50 triple sets.
count = 0

while count < 50:
    print('PYTHAGOREAN TRIPLE CHECKER')
    call = Calculate()
    sides = call.list_input()
    call.pythag_check(sides)
    count += 1

















