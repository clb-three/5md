# enemy.py: an Enemy is a door card that
# you have to kill with a few different attack cards

class Enemy:
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

    def __init__(self):
        '''
        Constructor. This is called whenever we create an Enemy.
        '''

        # TODO Assign enemy stats from 
        self.cards = ['sword', 'shield', 'arrow']

    def has_card(self, card):
        '''
        Return true if card matches one of my cards
        Return false if none of the cards match
        '''

        return card in self.cards

    def try_attack(self, card):    
        '''
        Test for a match
        remove the card from the enemy's health and return true if it's a match
        else return None
        '''

        if self.has_card(card):
            self.cards.remove(card)
            return True

        return False
            
    def __str__(self):
        '''
        Return a list of the enemy's cards
        '''

        return 'Enemy HP: ' + str(self.cards)

    def is_dead(self):
        '''
        Return true if the Enemy is dead
        '''
        return len(self.cards) == 0
