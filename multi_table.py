'''
Created on Sun 04/20/2020 20:29:08
Multiplication Table
@author: MarsCandyBars
'''

def table(user_num):
    '''
    Description:
        This function creates the table in a matrix format
        with nested for loops, left justifying the numbers,
        and not causing endlines until the loop is broken.
    Args:
        user_num
    Returns:
        None.
    '''
    for i in range(1, (user_num + 1)):
        for j in range(1, (user_num + 1)):
            print((str(i * j)).ljust(10), end = '')
        print('')

#Title
print('MULTIPLICATION TABLE GENERATOR')
user_num = int(input('Please enter a number you would like to print a table for: '))

#Calling function and passing value.
table(user_num)
