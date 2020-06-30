from abc import ABC, abstractmethod

from model.dictable import Dictable


class BaseHeroCard(ABC, Dictable):
    @abstractmethod
    def play(self, target, ctx=None):
        '''Play this card on the given game state, with the given target'''

    def __eq__(self, other):
        return str(self) == str(other)
