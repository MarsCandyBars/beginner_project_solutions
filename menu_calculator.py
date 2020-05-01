'''
Created on Sun 04/30/2020 20:39:23
Menu Calculator
@author: MarsCandyBars
'''

class POS():

    def menu(self):
        '''
        Description:
            This method prints the menu.
        Args:
            None.   
        Returns:
            None.
        '''
        
        print("""
        1) Chicken Strips - $3.50
        2) French Fries - $2.50
        3) Hamburger - $4.00
        4) Hotdog - $3.50
        5) Large Drink - $1.75
        6) Medium Drink - $1.50
        7) Milk Shake - $2.25
        8) Salad - $3.75
        9) Small Drink - $1.25
        """)

    def selections(self):
        '''
        Description:
            This method takes user input.
        Args:
            None.   
        Returns:
            selections
        '''
        
        selections = input('Please make item selections: ')
        return selections

    def running(self, select):
        '''
        Description:
            This method takes a tally of the number
            of each selected menu item.
        Args:
            select   
        Returns:
            None.
        '''
        
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        
        for i in range(0, len(select)):
            if select[i] == '1':
                one += 1
            elif select[i] == '2':
                two += 1
            elif select[i] == '3':
                three += 1
            elif select[i] == '4':
                four += 1
            elif select[i] == '5':
                five += 1
            elif select[i] == '6':
                six += 1
            elif select[i] == '7':
                seven += 1
            elif select[i] == '8':
                eight += 1
            elif select[i] == '9':
                nine += 1


        #Printing out the amount of each item selected
        #and will add ljust() later
        if one > 0:
            print('1) Chicken Strips - $3.50 x', one)
            
        if two > 0:
            print('2) French Fries - $2.50   x', two)
            
        if three > 0:
            print('3) Hamburger - $4.00      x', three)
            
        if four > 0:
            print('4) Hotdog - $3.50         x', four)
            
        if five > 0:
            print('5) Large Drink - $1.75    x', five)
            
        if six > 0:
            print('6) Medium Drink - $1.50   x', six)
            
        if seven > 0:
            print('7) Milk Shake - $2.25     x', seven)
            
        if eight > 0:
            print('8) Salad - $3.75          x', eight)
            
        if nine > 0:
            print('9) Small Drink - $1.25    x', nine)
            
    def calculate(self, select):
        '''
        Description:
            This method steps through the select
            string and creates a dollar total.
        Args:
            select
        Returns:
            total 
        '''
        
        total = 0
        for i in range(0, len(select)):
            if select[i] == '1':
                total += 3.50
            elif select[i] == '2':
                total += 2.50
            elif select[i] == '3':
                total += 4.00
            elif select[i] == '4':
                total += 3.50
            elif select[i] == '5':
                total += 1.75
            elif select[i] == '6':
                total += 1.50
            elif select[i] == '7':
                total += 2.25
            elif select[i] == '8':
                total += 3.75
            elif select[i] == '9':
                total += 1.25
        return total
        
#Calling POS()
call = POS()
end = True

#Giving option to replay
while end:
    call.menu()
    select = call.selections()
    totals = call.calculate(select)
    call.running(select)
    print('                          $', totals)
    replay = input('Place another order? (Y/N)')

    if replay == 'N' or replay == 'n':
        quit()
