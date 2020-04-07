import random
import hero_cards


class Hero:
    '''
    A hero is a player character, eventually will need to have different heros with set decks.
    The hero is initialized with a deck that is chosen randomly from a set of 5 basic actions
    From this deck the hero draws five cards at the start of the game
    The hero can then discard any card they like (used when playing the game) or draw a card from the deck
    The deck can be shuffled
    '''

    def __init__(self, name):
        '''
        Constructor. This is called whenever we create a Hero.
        '''

        self.name = name

        # A couple lists to hold our hero's hand and their deck
        self.hand = []

        # Takes a random sample from actions and puts it into cards, parameterized by num_of_actions
        self.deck = []
        # TODO: Each Hero should have a class so that we can know
        # which cards to put in his/her/xer/its/helixopter's deck.
        for i in range(0, 40):
            # for each index to 40 add a random item from actions to hand
            self.deck.append(random.choice(hero_cards.deck()))
        random.shuffle(self.deck)

    def has_card(self, card):
        '''
        Return whether card matches one of my cards.
        '''
        return card in self.hand

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        '''
        Return a list of the hero's cards
        '''
        # TODO: Make hand just list out how many of each card we have.
        # sword: 2: shield: 3, etc.
        return f'{self.name}: {self.hand}'

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
            print("You have no more cards in your deck!\n")

    def discard(self, card):
        '''
        Method to remove a card from the hero's hand
        '''

        # Checks if the card is held by the hero
        if self.has_card(card):
            # If it is a valid card to remove, remove it
            return self.hand.remove(card)
        else:
            print("You can't discard a card you don't have!\n")

    def deck_size(self):
        return len(self.deck)

    def hand_size(self):
        return len(self.hand)
