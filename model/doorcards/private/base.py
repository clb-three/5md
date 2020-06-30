from abc import ABC, abstractmethod

from .dictable import Dictable


class BaseDoorCard(ABC, Dictable):
    def __init__(self, symbols, card_type):
        self.symbols = symbols
        self.type = card_type
        self.script = None

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

    # TODO: Make this shit work with with copy.deepcopy
    @abstractmethod
    def deepcopy(self):
        '''Return a deep copy of this class.'''
