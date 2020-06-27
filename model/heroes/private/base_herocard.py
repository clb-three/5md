from abc import ABC, abstractmethod


class BaseHeroCard(ABC):
    @abstractmethod
    def play(self, target, ctx=None):
        '''Play this card on the given game state, with the given target'''

    def __eq__(self, other):
        return self.__str__() == other.__str__()
