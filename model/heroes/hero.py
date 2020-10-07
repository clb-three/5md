from model.message import Message
from model.serialization.stringable import Stringable

from .complaint import Complaint


class Hero(Stringable):
    '''
    A hero is a player character
    '''

    def __init__(self, name, classname, deck):
        '''
        Constructor. This is called whenever we create a Hero.
        '''

        self.name = name
        self.classname = classname

        # A couple lists to hold our hero's hand and their deck
        self.hand = []

        # Takes a random sample from actions and puts it into cards, parameterized by num_of_actions
        self.deck = deck

    def get_card_from_hand(self, card_in_bush):
        '''
        Return whether card matches one of my cards.
        '''
        for card_in_hand in self.hand:
            if card_in_hand == card_in_bush:
                return card_in_hand

    def draw_card(self):
        '''
        Draw a card into your hand and return it.
        Return default None if your deck is empty.
        '''

        # If there are cards in the deck to draw from add them to the hero's hand
        if len(self.deck) > 0:
            # Adds to the hand
            self.hand.append(self.deck[0])
            # Removes from the deck
            card = self.deck.pop(0)
            return card
        else:
            raise Complaint(Message('error', 'deckempty'))

    def discard(self, card):
        '''
        Method to remove a card from the hero's hand
        '''

        # Checks if the card is held by the hero
        if self.get_card_from_hand(card):
            # If it is a valid card to remove, remove it
            self.hand.remove(card)
        else:
            raise Complaint(Message('error', 'nocard'))
