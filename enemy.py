# enemy.py: an Enemy is a door card that
# you have to kill with a few different attack cards

class Enemy:
    def __init__(self):
        '''
        Constructor
        '''

        # TODO: Randomly select a set of attack cards from all possibilities
        self.cards = ['sword', 'shield', 'bow']
    
    def matches(self, card: str):
        '''
        Return true if card matches one of my cards
        Return false if none of the cards match
        '''

        match = None

        # Take a field off the enemy
        # When we play that card
        for enemy_card in self.cards:
            if card == enemy_card:
                match = enemy_card # marking card for removal

        if match != None:
            return True
        else:
            return False

    def attack(self, card):    
        '''
        Test for a match and remove it from the
        enemy's health if it's a match
        '''

        if self.matches(card):
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
