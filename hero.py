from input import get_input
from enemy import Enemy
import random

class Hero:
    '''
    A hero is a player character, eventually will need to have different heros with set decks.
    Main goal for now is to have a 'deck' that can be used in game.py to allow drawing cards.
    '''
    

    def __init__(self):
        '''
        Constructor. This is called whenever we create a Hero.
        '''

        # All possible moves a hero can have, used to initialize a random hand
        actions = ['sword', 'shield', 'arrow', 'scroll', 'jump']

        # randomly selects the number of actions the hero will receive
        num_of_actions = 5
        self.cards = []
        # Takes a random sample from actions and puts it into cards, parameterized by num_of_actions
        for i in range(0, num_of_actions):
            self.cards.append(random.choice(actions)) #for each index to num_of_actions add a random item from actions to hand


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


    def draw_card(self, card):
        '''
        Returns true if card was able to be drawn from the deck
        Return false if deck is empty or max hand size has already been reached
        '''
