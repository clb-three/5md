from model.message import Message

from .complaint import Complaint
from .private.base_herocard import BaseHeroCard


class SingleSymbol(BaseHeroCard):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol

    def play(self, target, ctx=None):
        '''
        Play this symbol against the target
        '''

        if self.symbol in target.symbols:
            target.symbols.remove(self.symbol)
            return Message('removesymbol', self.symbol)
        else:
            raise Complaint(Message('nosymbol', self.symbol))

    def __lt__(self, other):
        if isinstance(other, SingleSymbol):
            return self.symbol.name < other.symbol.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.symbol.name == other
        if isinstance(other, SingleSymbol):
            return self.symbol.name == other.symbol.name
