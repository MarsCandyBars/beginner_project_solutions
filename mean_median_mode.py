'''
Created on Sun 04/17/2020 13:27:33
Mean, Median, Mode
@author: MarsCandyBars
'''

class MMM():

    def addto(self):
        '''
        Description:
            This method prompts the user to input
            values to create user_list.
        Args:
            None.
        Returns:
            user_list
        '''
        
        user_list = []
        counter = True
        choice = 'y'

        while counter == True:
            if choice == 'y':
                user_list.append(int(input('Enter list number: ')))
                choice = input('Add another? (Y/N)')
            elif choice == 'n':
                break

        return user_list

    def mean(self, user_list):
        '''
        Description:
            This method prompts the user for the amount
            of decimal places to round the mean. It calculates
            the mean.
        Args:
            user_list
        Returns:
            None.
        '''
        
        round_size = int(input('How many places would you like to round the Mean to? '))
        total = 0
        divi = len(user_list)
        
        for i in user_list:
            total = total + i
            
        mean = (total / divi)

        rounded_mean = round(mean, round_size)
        print('\nMean:', rounded_mean)

    def median(self, user_list):
        '''
        Description:
            This method calculates the median of
            user_list.
        Args:
            user_list
        Returns:
            user_list
        '''
        
        swap = True

        #Bubble sorting user_list
        while swap:
            swap = False
            for i in range(len(user_list) - 1):
                if user_list[i] > user_list[i + 1]:
                    temp = user_list[i]
                    user_list[i] = user_list[i + 1]
                    user_list[i + 1] = temp

                    swap = True

        #Original prompt called for returning 2 median
        #numbers if they exist. It was more difficult to
        #return the floating point median. So thats what
        #I did instead.
                    
        med_len = len(user_list)
        med_num = len(user_list) // 2

        if med_len % 2 == 0:
            summed = user_list[med_num] + user_list[med_num - 1]
            divi_med = summed / 2
            print('\nMedian:', divi_med)
        else:    
            print('\nMedian:', user_list[med_num])
        return user_list

    def mode(self, sort):
        '''
        Description:
            This method calculates the mode, and
            multiple modes if applicable.
        Args:
            sort
        Returns:
            None.
        '''
        
        max_count = 1
        mode = sort[0]
        old_mode = sort[0]
        current_count = 1

        #Linear traversal and assigment through sorted
        #list gathered from median()
        for i in range(len(sort)):
            if sort[i] == sort[i - 1]:
                current_count +=1
                old_mode = sort[i]
            else:
                if current_count > max_count:
                    max_count = current_count
                    mode = sort[i - 1]

                current_count = 1

        if current_count > max_count:
            max_count = current_count
            mode = sort[len(sort) - 1]

        if old_mode == mode:
            print('\nMode:', mode)
        else:
             print('\nMode:', mode, old_mode)
        


#Instantiating class MMM()
call = MMM()

#Calling addto()
user_list = call.addto()

#Calling mean()
call.mean(user_list)

#Calling median()
sort = call.median(user_list)

#Calling mode()
call.mode(sort)
