from .private.base import BaseDoorCard
from .private.types import DoorCardTypes
from copy import deepcopy
# enemy.py: an Enemy is a door card that
# you have to kill with a few different attack cards.
# Certainn enemy types can be insta-killed by certain cards.


class Enemy(BaseDoorCard):
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

    def __init__(self, name, symbols, card_type=DoorCardTypes.monster):
        '''
        Constructor. This is called whenever we create an Enemy.
        '''

        super().__init__(symbols, card_type)

        self.name = name

    def __dict__(self):
        '''
        Return a list of the enemy's symbols
        '''

        selfobj = super().__dict__()
        selfobj['name'] = self.name

        return selfobj

    def deepcopy(self):
        return Enemy(deepcopy(self.name), deepcopy(self.symbols), deepcopy(self.type))
