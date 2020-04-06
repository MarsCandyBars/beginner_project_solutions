'''
Created on Sun 04/05/2020 07:07:14
Armstrong Number
@author: MarsCandyBars
'''

def armstrong(user_num):
    
    '''
    Description:
        This function assesses a number and determines if it
        is an armstrong number.
    Args:
        user_num
    Returns:
        Prints whether or not user_num is an armstrong number
        not.
    '''
    
    sum = 0
    num = user_num

    #Creating variable used to represent the power that each digit must
    #be raised to.
    power = len(str(user_num))
    print(power)

    #Loop calculates if number is or is not an armstrong number.
    while num > 0:
        index = num % 10
        sum += index ** power
        num = num // 10
    #If-else statements print the output for armstrong().
    if user_num == sum:
        print(user_num, 'is indeed an Armstrong number.')
    else:
        print(user_num, 'is not an Armstrong number.')

user_num = int(input('Please enter a number to check if it is an Armstrong number: '))
armstrong(user_num)
