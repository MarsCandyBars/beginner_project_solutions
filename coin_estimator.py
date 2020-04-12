'''
Created on Sun 04/11/2020 09:51:55
Coin Estimator By Weight
@author: MarsCandyBars
'''

class Coins():

    def weights(self):
        '''
        Description:
            This method gathers input from the user for each coin variant.
        Args:
            None.
        Returns:
            quarters, dimes, nickels, pennies
        '''
        quarters = float(input('Enter the weight for quarters: '))
        dimes = float(input('Enter the weight for dimes: '))
        nickels = float(input('Enter the weight for nickels: '))
        pennies = float(input('Enter the weight for pennies: '))
        return [quarters, dimes, nickels, pennies]

    def count(self, quarters, dimes, nickels, pennies):
        '''
        Description:
            This method calculates the number of each coin and
            the total of the value of all of the coins.
        Args:
            quarters, dimes, nickels, pennies
        Returns:
            quar_num, dime_num, nick_num, penn_num
        '''

        #Dividing the weights by the individual
        #weight of each coin.
        quar_num = (quarters / 5.67)
        dime_num = (dimes / 2.268)
        nick_num = (nickels / 5.00)
        penn_num = (pennies / 2.50)

        print('\n')
        print('Number of coins:')
        print('Quarters =', round(quar_num))
        print('Dimes =', round(dime_num))
        print('Nickels =', round(nick_num))
        print('Pennies =', round(penn_num))

        #Multiplying the number of each coin
        #variant by their monetary values.
        quar_total = quar_num * .25
        dime_total = dime_num * .10
        nick_total = nick_num * .05
        penn_total = penn_num * .01
        
        total = (quar_total + dime_total + nick_total + penn_total)
        print('\nTotal Value: ${}'.format(round(total)))
        
        return [quar_num, dime_num, nick_num, penn_num]

    def sleeves(self, quar_num, dime_num, nick_num, penn_num):
        '''
        Description:
            This method calculates the number of sleeves for
            each coin type.
        Args:
            quar_num, dime_num, nick_num, penn_num
        Returns:
            None.
        '''

        #Dividing the number of coins of each variant by
        #the amount each sleeve will hold
        quar_sleeve_num = (quar_num / 40.0)
        dime_sleeve_num = (dime_num / 50.0)
        nick_sleeve_num = (nick_num / 40.0)
        penn_sleeve_num = (penn_num / 50.0)

        print('\nNumber of wrappers:')
        print('Quarters =', round(quar_sleeve_num))
        print('Dimes =', round(dime_sleeve_num))
        print('Nickels =', round(nick_sleeve_num))
        print('Pennies =', round(penn_sleeve_num))

#Calls the Coins() class
call = Coins()

weights_list = call.weights()

count_list = call.count(weights_list[0], weights_list[1], weights_list[2], weights_list[3])
call.sleeves(count_list[0], count_list[1], count_list[2], count_list[3])
