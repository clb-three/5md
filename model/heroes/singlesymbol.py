from .complaint import Complaint
from .private.base_herocard import BaseHeroCard


class SingleSymbol(BaseHeroCard):
    def __init__(self, symbol):
        self.symbol = symbol

    def play(self, target, ctx=None):
        '''
        Play this symbol against the target
        '''

        if self.symbol in target.symbols:
            target.symbols.remove(self.symbol)
            return f'target removesymbol "{self.symbol}"'
        else:
            raise Complaint(f'target nosymbol {self.symbol}')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.symbol.__str__()

    def __lt__(self, other):
        if isinstance(other, SingleSymbol):
            return self.symbol.name < other.symbol.name
