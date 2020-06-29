import json
from abc import ABC, abstractmethod


class BaseDoorCard(ABC):
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

    @abstractmethod
    def __dict__(self):
        '''
        Return a dict representation of this class
        '''
        return {
            'type': str(self.type),
            'hp': [str(s) for s in self.symbols]
        }

    def __str__(self):
        '''
        Return a list of the enemy's symbols
        '''

        d = self.__dict__

        return json.dumps(d)

    # TODO: Make this shit work with with copy.deepcopy
    @abstractmethod
    def deepcopy(self):
        '''Return a deep copy of this class.'''
