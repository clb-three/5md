from .private.base_herocard import BaseHeroCard


class MultiSymbol(BaseHeroCard):
    def __init__(self, *symbols):
        super().__init__()
        assert len(symbols) > 0
        self.symbols = symbols

    def play(self, ctx):
        '''
        Play this multisymbol against the target
        '''
        pass  # TODO: Implement MultiSymbol

    def __str__(self):
        return [str(s) for s in self.symbols]
