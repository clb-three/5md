from input import get_input
from enemy import Enemy
from random import random

class Hero:
    '''
    A hero is a player character, eventually will need to have different heros with set decks.
    Main goal for now is to have a 'hand' that can be used in game.py to make sure a play is valid.
    '''


    def __init__(self):
        '''
        Constructor. This is called whenever we create a Hero.
        '''

        # TODO Issue #6: Randomly select a set of attack cards from all possibilities
        # All possible moves a hero can have, used to initialize a random hand
        actions = ['sword', 'shield', 'arrow', 'scroll', 'jump']

        # randomly selects the number of actions the hero will receive
        num_of_actions = random.randInt(1, 4)
        # Takes a random sample from actions and puts it into cards, parameterized by numOfActions
        self.cards = random.sample(actions, num_of_actions) # TODO change from sample to a loop that allows for repeated types



    def has_card(self, card):
         '''
         Return true if card matches one of my cards
         Return false if none of the cards match
         '''

         return card in self.cards



    def __str__(self):
        '''
        Return a list of the hero's cards
        '''

        return 'Your cards are: ' + str(self.cards)



