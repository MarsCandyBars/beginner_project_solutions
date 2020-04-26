'''
Created on Sun 04/25/2020 09:16:13
Base Converter
@author: MarsCandyBars
'''

class Base():
    
    def convert_ten(self):
        '''
        Description:
            This method converts any number from its base to
            base 10.
        Args:
            None.   
        Returns:
            num1, total 
        '''
        
        print('BASE CONVERTER')
        print('Numbers entered must be below ten quintillion threshold.\n')

        #Getting number to convert to base 10 and its current base
        num1 = input('Please enter number to convert: ')
        num2 = int(input('Please enter the base of the number: '))

        #Ruling out improper bases 0 and 1
        if num2 == 1 or num2 == 0:
            print('A base of 0 or 1 will not work.')
        elif num2 == 10:
            print('The number is already in base 10.')
        #If the base is not 10, create list of powers
        elif num2 != '10':  
            #Creates list of powers of num1 and reverses it
            base_powers = []
            for i in range(0, len(num1)):
                base_num = num2 ** i
                base_powers.append(base_num)

            #Reversing powers list casting num1 as a list   
            total = 0
            base_powers.reverse()
            num1_list = list(num1)

            #Multiplying the num1 list against each power and adding them together
            for i in range(0, len(num1)):
                temp = num1_list[i]
                run_count = int(temp) * base_powers[i]
                total += run_count

            print('Your number in base 10:', total, '\n')

            return [num1, total]

    def convert_base(self, num1, total):
        '''
        Description:
            This method converts any number from base 10
            to the users chosen base.
        Args:
            num1, total  
        Returns:
            None.
        '''
        
        convert_num = int(input('Please enter what base you want to convert to: '))

        #Reassign base_powers to create new powers list for desired base
        base_powers = []
        for i in range(0, len(num1) + 30):
            base_num = convert_num ** i
            base_powers.append(base_num)

        #Indexing through base_powers to find first number that is
        #divisible into the total
        for i in range(0, len(base_powers)):
            if (total // base_powers[i]) == 0:
                starter = i

        #Initialize final[] for final conversion
        final = []

        #Increment backwards from the first divisible power
        for i in range(starter, -1, -1):
            hold = total // base_powers[i]
            remain = total % base_powers[i]
            total = remain
            if hold != 0:
                final.append(hold)

        print('Your number in base', convert_num, ':', ''.join(str(x) for x in final))
        

#Calling class Base()
base_convert = Base()

#Loop gives option to do-over or quit
replay = True
while replay:
    test = base_convert.convert_ten()
    base_convert.convert_base(test[0], test[1])

    answer = input('Calculate another number? (Y/N)')

    if answer == 'Y' or answer == 'y':
        continue
    else:
        quit()











