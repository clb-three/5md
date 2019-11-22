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

        # All possible moves a hero can have, used to initialize a random deck
        actions = ['sword', 'shield', 'arrow', 'scroll', 'jump']

        #A couple initialized variables so they can be appended to
        self.hero_hand = []
        num_of_actions = 5
        self.hero_deck = []

        # Takes a random sample from actions and puts it into cards, parameterized by num_of_actions
        for i in range(0, 40):
            self.hero_deck.append(random.choice(actions)) #for each index to 40 add a random item from actions to hand

        #Loop to draw the hero 5 cards from their deck
        j = 0
        while j < 5:
            self.draw_card()
            j+=1


    def has_card(self, card):
         '''
         Return true if card matches one of my cards
         Return false if none of the cards match
         '''

         return card in self.hero_hand


    def __str__(self):
        '''
        Return a list of the hero's cards
        '''
        return 'Your cards are: ' + str(self.hero_hand)


    def draw_card(self):
        '''
        Returns true if card was able to be drawn from the deck
        Return false if deck is empty or max hand size has already been reached
        '''

        if len(self.hero_deck) > 0:
            self.hero_hand.append(self.hero_deck[0])
            self.hero_deck.pop(0)
            return True
        else:
            print("You have no more cards in your deck!\n")
            return False


    def discard(self, card):
        '''
        Method to remove a card from the hero's hand
        '''
        self.hero_hand.remove(card)
