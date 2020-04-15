'''
Created on Sun 04/14/2020 07:37:33
Change Calculator
@author: MarsCandyBars
'''

class Change():

    def user_input(self):
        '''
        Description:
            This method prompts the user for the price
            and amount of money given for an item.
        Args:
            None.
        Returns:
            cost, money
        '''
        
        print('CHANGE CALCULATOR')
        cost = float(input('Price: '))
        money = float(input('Money Provided: '))

        return [cost, money]

    def calculate(self, change_data):
        '''
        Description:
            This method floor divides to get
            the total amount of each denomitation
            of coin and modulates to get the remainders
            each time.
        Args:
            change_data
        Returns:
            None.
        '''

        #Subtracts money from cost.
        change = change_data[1] - change_data[0]

        #Floor divides then modulates
        quar = change // .25
        quar_remain = change % .25

        dime = quar_remain // .10
        dime_remain = quar_remain % .10

        nick = dime_remain // .05
        nick_remain = dime_remain % .05

        penn = nick_remain // .01
        penn_remain = nick_remain % .01

        #Prints each denomination amount
        print('Quarters:', quar)
        print('Dimes:', dime)
        print('Nickels:', nick)
        print('Pennies:', penn)

#Looping program
replay = True
while replay == True:
    #Calling Change()
    call = Change()

    #Passing user_input() into calculate()
    change_data = call.user_input()
    call.calculate(change_data)

    #Giving quit option
    rerun = input('Rerun program? (Y/N)')
    print('')
    if rerun == 'N' or rerun == 'n':
        quit()
    else:
        continue
