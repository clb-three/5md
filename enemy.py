from doorcard import DoorCard
# enemy.py: an Enemy is a door card that
# you have to kill with a few different attack cards

# TODO Issue #11: Load door cards from store.
# This could be anything - a database, JSON, hardcoded Python, plaintext file, your gramma's panties.
# More details in the issue description.


class Enemy(DoorCard):
    '''
    Class for an Enemy. A class is like a blueprint for an object, and you'll use
    the constructor __init__ by calling Enemy() to make an instance of Enemy.
    Right now it's just a bundle of cards.
    '''

    # Name
    # Which symbols needed to defeat it
    # Type (Monster, Obstacle, or Person).
    # Some classes have special cards that let them instantly
    # destroy certain types of door cards.

    def __init__(self, name, symbols, card_type):
        '''
        Constructor. This is called whenever we create an Enemy.
        '''

        super().__init__(symbols, card_type)

        self.name = name

    def __str__(self):
        '''
        Return a list of the enemy's symbols
        '''

        return ' '.join([
            f'Name: "{self.name}"',
            f'type: "{self.card_type}"',
            f'{super().__str__()}'
        ])
