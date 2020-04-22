'''
Created on Sun 04/20/2020 11:19:14
Fibonacci Sequence
@author: MarsCandyBars
'''

#Assigning first two elements
num1 = 0
num2 = 1

#Creating list and counter
mylist = [0, 1]
count = 0

#Getting value for nth term
user_input = int(input("Please enter a nth term: "))

#Loop to 
for i in range(0, user_input):
    total = mylist[i] + mylist[i + 1]
    mylist.append(total)
print(mylist,'\n')
print('Value of nth term:',mylist[user_input])


#Using recursion
def fibonacci(user_input):
    '''
    Description:
        This method uses recursion to find the
        nth term of a fibonacci sequence.
    Args:
        user_input
    Returns:
        fibonacci(user_input - 1) + fibonacci(user_input - 2)
    '''
    if user_input == 0:
        return 0
    elif user_input == 1:
        return 1
    else:
        return fibonacci(user_input - 1) + fibonacci(user_input - 2)

fib = fibonacci(user_input)
print('Value of nth term using recursion:', fib)

