# enemy.py: an Enemy is a door card that
# you have to kill with a few different attack cards

class Enemy:
    '''
    Class for an Enemy. A class is like a blueprint for an object, and you'll use
    the constructor __init__ by calling Enemy() to make an instance of Enemy.
    Right now it's just a bundle of cards.
    '''

    def __init__(self):
        '''
        Constructor. This is called whenever we create an Enemy.
        '''

        # TODO Issue #6: Randomly select a set of attack cards from all possibilities
        self.cards = ['sword', 'shield', 'bow']
    
    def has_card(self, card):
        '''
        Return true if card matches one of my cards
        Return false if none of the cards match
        '''

        return card in self.cards

    def attack(self, card):    
        '''
        Test for a match and remove it from the
        enemy's health if it's a match
        '''

        if self.has_card(card):
            self.cards.remove(card)
        else:
            print('No match')
            
    def __str__(self):
        '''
        Return a list of the enemy's cards
        '''

        return 'Enemy HP:' + str(self.cards)

    def is_dead(self):
        '''
        Return true if the Enemy is dead
        '''
        return len(self.cards) == 0
