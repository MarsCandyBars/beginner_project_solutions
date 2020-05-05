'''
Created on Sun 05/05/2020 18:29:38
Seat Reservation
@author: MarsCandyBars
'''

class Seat_Reserve():

    def text(self):
        '''
        Description:
            This method prints the initial menu.
        Args:
            None.   
        Returns:
            None.
        '''
        
        row1 = ['1a','1b','1c','1d','1e','1f','1g','1h','1i','1j']
        row2 = ['2a','2b','2c','2d','2e','2f','2g','2h']
        row3 = ['3a','3b','3c','3d','3e','3f']
        row4 = ['4a','4b','4c','4d']
        row5 = ['5a','5b']
        
        print('''
          _    _                      _     _____                          _      _    _       _ _ 
         | |  | |                    | |   / ____|                        | |    | |  | |     | | |
         | |  | |_ __  _ __ ___  __ _| |  | |     ___  _ __   ___ ___ _ __| |_   | |__| | __ _| | |
         | |  | | '_ \| '__/ _ \/ _` | |  | |    / _ \| '_ \ / __/ _ \ '__| __|  |  __  |/ _` | | |
         | |__| | | | | | |  __/ (_| | |  | |___| (_) | | | | (_|  __/ |  | |_   | |  | | (_| | | |
          \____/|_| |_|_|  \___|\__,_|_|   \_____\___/|_| |_|\___\___|_|   \__|  |_|  |_|\__,_|_|_|
          
              ''')
        
        #Weird formatting for nicer menu layout
        print('                     ',row1)
        print('                          ', row2)
        print('                                ', row3)
        print('                                      ', row4)
        print('                                            ', row5)

        print('''

         1) Row 1
         2) Row 2
         3) Row 3
         4) Row 4
         5) Row 5

              ''')

    def seats(self):
        '''
        Description:
            This method initializes the rows, prompts for row, # of seats,
            and each individual seat. It then replaces chosen seats with
            the value 'X'.
        Args:
            None.   
        Returns:
            None.
        '''

        #Row initialization
        row1 = ['1a','1b','1c','1d','1e','1f','1g','1h','1i','1j']
        row2 = ['2a','2b','2c','2d','2e','2f','2g','2h']
        row3 = ['3a','3b','3c','3d','3e','3f']
        row4 = ['4a','4b','4c','4d']
        row5 = ['5a','5b']

        #Replay gives loop funcionality for entire program
        replay = True
        while replay:
            #Gathering inputs
            row = input('Select a row: ')
            num = input('Select number of seats: ')

            #Steps through each list and replaces values with 'X'
            #were applicable
            for i in range(0, int(num)):
                seat = input('Select individual seats: ')

                if row == '1':
                    for i in range(0, len(num)):
                        for i in range(0, len(row1)):
                            if seat == row1[i]:
                                row1[i] = ('X')
                elif row == '2':
                    for i in range(0, len(num)):
                        for i in range(0, len(row2)):
                            if seat == row2[i]:
                                row2[i] = 'X'
                elif row == '3':
                    for i in range(0, len(num)):
                        for i in range(0, len(row3)):
                            if seat == row3[i]:
                                row3[i] = 'X'
                elif row == '4':
                    for i in range(0, len(num)):
                        for i in range(0, len(row4)):
                            if seat == row4[i]:
                                row4[i] = 'X'
                elif row == '5':
                    for i in range(0, len(num)):
                        for i in range(0, len(row5)):
                            if seat == row5[i]:
                                row5[i] = 'X'

            no_replay = input('Would you like to reserve another seat? (Y/N)')
            if no_replay == 'Y' or no_replay == 'y':
                print('''
                  _    _                      _     _____                          _      _    _       _ _ 
                 | |  | |                    | |   / ____|                        | |    | |  | |     | | |
                 | |  | |_ __  _ __ ___  __ _| |  | |     ___  _ __   ___ ___ _ __| |_   | |__| | __ _| | |
                 | |  | | '_ \| '__/ _ \/ _` | |  | |    / _ \| '_ \ / __/ _ \ '__| __|  |  __  |/ _` | | |
                 | |__| | | | | | |  __/ (_| | |  | |___| (_) | | | | (_|  __/ |  | |_   | |  | | (_| | | |
                  \____/|_| |_|_|  \___|\__,_|_|   \_____\___/|_| |_|\___\___|_|   \__|  |_|  |_|\__,_|_|_|
                  
                       ''')

                print('                     ',row1)
                print('                          ', row2)
                print('                                ', row3)
                print('                                      ', row4)
                print('                                            ', row5)

                print('''

                 1) Row 1
                 2) Row 2
                 3) Row 3
                 4) Row 4
                 5) Row 5

                      ''')
                continue
                
            elif no_replay == 'N' or no_replay == 'n':
                replay = False
                            
        print('''
          _    _                      _     _____                          _      _    _       _ _ 
         | |  | |                    | |   / ____|                        | |    | |  | |     | | |
         | |  | |_ __  _ __ ___  __ _| |  | |     ___  _ __   ___ ___ _ __| |_   | |__| | __ _| | |
         | |  | | '_ \| '__/ _ \/ _` | |  | |    / _ \| '_ \ / __/ _ \ '__| __|  |  __  |/ _` | | |
         | |__| | | | | | |  __/ (_| | |  | |___| (_) | | | | (_|  __/ |  | |_   | |  | | (_| | | |
          \____/|_| |_|_|  \___|\__,_|_|   \_____\___/|_| |_|\___\___|_|   \__|  |_|  |_|\__,_|_|_|
          
               ''')

        print('                     ',row1)
        print('                          ', row2)
        print('                                ', row3)
        print('                                      ', row4)
        print('                                            ', row5)

        print('''

         1) Row 1
         2) Row 2
         3) Row 3
         4) Row 4
         5) Row 5

              ''')


call = Seat_Reserve()
call.text()
call.seats()




