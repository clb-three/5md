import uuid
from abc import ABC, abstractmethod

from model.serialization.stringable import Stringable


class BaseHeroCard(ABC, Stringable):
    def __init__(self):
        self.uuid = str(uuid.uuid4())

    @abstractmethod
    def play(self, target, ctx=None):
        '''Play this card on the given game state, with the given target'''

    def __eq__(self, other):
        return str(self) == str(other)
