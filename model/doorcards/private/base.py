import json


class BaseDoorCard:
    def __init__(self, symbols, card_type):
        self.symbols = symbols
        self.type = card_type
        self.do_script = None

    def is_dead(self):
        '''
        Return True if the Enemy is dead
        '''

        return len(self.symbols) == 0

    def kill(self):
        '''
        kys
        '''

        del self.symbols[:]

    def __dict__(self):
        return {
            'type': str(self.type),
            'hp': [str(s) for s in self.symbols]
        }

    def __str__(self):
        '''
        Return a list of the enemy's symbols
        '''

        selfobj = self.__dict__()
        return json.dumps(selfobj)
