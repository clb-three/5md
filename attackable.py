


class Attackable:
    def __init__(self, symbols):
        self.symbols = symbols

    def is_dead(self):
        '''
        Return True if the Enemy is dead
        '''

        return len(self.symbols) == 0

    def try_attack(self, symbol):
        '''
        Test for a match and
        remove the card from the enemy's health and return true if it's a match
        else return False
        '''

        if symbol in self.symbols:
            self.symbols.remove(symbol)
            return True

        return False

    def __str__(self):
        '''
        Return a list of the enemy's symbols
        '''

        return f'HP: {str(self.symbols)}'