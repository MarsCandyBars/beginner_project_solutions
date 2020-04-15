'''
Created on Sun 04/14/2020 06:47:44
Mad Libs Story Maker
@author: MarsCandyBars
'''

class MadLib():

    def prompts(self):
        '''
        Description:
            This method prompts the user for each
            word.
        Args:
            None.
        Returns:
            name, place_one, noun_one, noun_two, place_two
        '''

        print('MAD LIBS STORY MAKER')
        name = input('Name: ')
        
        place_one = input('Place: ')

        place_two = input('Place: ')

        noun_one = input('Noun (Singular): ')

        noun_two = input('Noun: ')

        return [name, place_one, noun_one, noun_two, place_two]

    def story(self, input_list):
        '''
        Description:
            This method prints the story, and decides
            whether a or an should be used if the following
            word begins with vowel.
        Args:
            input_list
        Returns:
            None.
        '''
        
        a_an = 'a '
        vowels = input_list[2]
        if vowels[0] == 'a':
            a_an = 'an '
        elif vowels[0] == 'e':
            a_an = 'an '
        elif vowels[0] == 'i':
            a_an = 'an '
        elif vowels[0] == 'o':
            a_an = 'an '
        elif vowels[0] == 'u':
            a_an = 'an '
        
        print('\nOne day, the sheriff went to the ' + input_list[1] + '. While he was walking to the ' + input_list[1] + ', he slipped on ' + a_an + input_list[2] +
              '. As he fell he shouted ' + input_list[3] + '! ' + input_list[0].capitalize() + ' then said, "What vulgar language!" The sheriff then got up, brushed himself off, ' +
              'and decided to go to the ' + input_list[4] + ' instead.')

#Calling MadLib()
call = MadLib()

#Calling prompts() and passing the values
#into story()
input_list = call.prompts()
call.story(input_list)
