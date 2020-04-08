


class DoorCard:
    def __init__(self, symbols, card_type, script=None):
        self.symbols = symbols
        self.type = card_type
        self.script = script

    def is_dead(self):
        '''
        Return True if the Enemy is dead
        '''

        return len(self.symbols) == 0

    def attack(self, symbol):
        '''
        Attack this enemy with the given card and return True if it's a success,
        else return False
        '''

        if symbol in self.symbols:
            self.symbols.remove(symbol)
            return True

        return False

    def kill(self):
        '''
        kys
        '''

        del self.symbols[:]

    def __str__(self):
        '''
        Return a list of the enemy's symbols
        '''

        return f'type: {self.type} HP: {str(self.symbols)}'