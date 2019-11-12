from input import get_input
from enemy import Enemy

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
        self.cards = ['sword', 'shield', 'arrow']


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



