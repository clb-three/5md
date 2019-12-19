from input import get_input
from enemy import DoorCard
import random
import cards

class Hero:
    '''
    A hero is a player character, eventually will need to have different heros with set decks.
    The hero is initialized with a deck that is chosen randomly from a set of 5 basic actions
    From this deck the hero draws five cards at the start of the game
    The hero can then discard any card they like (used when playing the game) or draw a card from the deck
    The deck can be shuffled
    '''


    def __init__(self):
        '''
        Constructor. This is called whenever we create a Hero.
        '''

        # A couple lists to hold our hero's hand and their deck
        self.hero_deck = []
        self.hero_hand = []

        # Takes a random sample from actions and puts it into cards, parameterized by num_of_actions
        for i in range(0, 40):
            self.hero_deck.append(random.choice(cards.action_cards)) #for each index to 40 add a random item from actions to hand

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
        # TODO: Make hero_hand just list out how many of each card we have.
        # sword: 2: shield: 3, etc.
        return 'Your cards are: ' + str(self.hero_hand)


    def draw_card(self):
        '''
        Returns true if card was able to be drawn from the deck
        Return false if deck is empty or max hand size has already been reached
        '''

        # If there are cards in the deck to draw from add them to the hero's hand
        if len(self.hero_deck) > 0:
            # Adds to the hand
            self.hero_hand.append(self.hero_deck[0])
            # Removes from the deck
            self.hero_deck.pop(0)
            return True
        else:
            print("You have no more cards in your deck!\n")
            return False


    def discard(self, card):
        '''
        Method to remove a card from the hero's hand
        '''

        # Checks if the card is valid
        if card == "sword" or card == "shield" or card == "arrow" or card == "jump" or card == "scroll":
            # Checks if the card is held by the hero
            if self.has_card(card):
                # If it is a valid card to remove, remove it
                self.hero_hand.remove(card)
            else:
                print("You can't discard a card you don't have!\n")
        else:
            print("That's not a card!\n")


    def shuffle(self):
        '''
        Shuffles the given hero deck
        '''
        random.shuffle(self.hero_deck)
