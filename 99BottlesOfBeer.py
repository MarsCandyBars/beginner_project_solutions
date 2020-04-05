'''
Created on Sat 04/04/2020 11:55:38
99 Bottles of Beer
@author: MarsCandyBars
'''

class BottlesOfBeer():

    def __init__(self):

        '''
        Description:
            This method provides attributes for the main lyrics
            of the song to make looping cleaner.
        Args:
            None.
        Returns:
            Attributes for the lyrics of '99 Bottles of Beer' up
            to the last bottle.
        '''
        
        lyric1 = ('bottles of beer on the wall,')
        self.lyric1 = lyric1

        lyric2 = ('bottles of beer. Take one down and pass it around,')
        self.lyric2 = lyric2

        lyric3 = ('bottles of beer on the wall.\n')
        self.lyric3 = lyric3


def lyric_print():

    '''
    Description:
        This function provides looping for the main song
        and adds the last 2 lines.
    Args:
        None.
    Returns:
        Prints the lyrics for the entire song.
    '''
    #Calling class BottlesOfBeer()     
    call = BottlesOfBeer()

    #Setting counter for loop
    beer_count = 99

    for i in range(99, -1, -1):

        if beer_count > 1:
            print(beer_count, call.lyric1, beer_count, call.lyric2, (beer_count - 1), call.lyric3)
            beer_count -= 1
        #Exits if-statement in order to provide the last two lines of the song, whose format
        #is different from the rest of the song.
        else:
            print(beer_count, 'bottle of beer on the wall,', beer_count, 'bottle of beer.',
                 'Take one down and pass it around, no more bottles of beer on the wall.\n')
            beer_count = 99
            print('No more bottles of beer on the wall, no more bottles of beer. Go to the',
                  'store and buy some more,', beer_count, 'bottles of beer on the wall.')
            #Breaks from the loop at the end of the song.
            break
#Calling lyric_print() function.
lyric_print()


