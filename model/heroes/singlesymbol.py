from .private.base_herocard import BaseHeroCard


class SingleSymbol(BaseHeroCard):
    def __init__(self, symbol):
        self.symbol = symbol

    def play(self, ctx):
        '''
        Play this symbol against the target
        '''
        if self.symbol in ctx.target.symbols:
            ctx.target.symbols.remove(self.symbol)
        else:
            raise Exception(f'{self.symbol} not in ctx.target.symbols')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.symbol.name

    def __lt__(self, other):
        if isinstance(other, SingleSymbol):
            return self.symbol.name < other.symbol.name
