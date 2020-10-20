from .private.base_herocard import BaseHeroCard


class MultiSymbol(BaseHeroCard):
    def __init__(self, *symbols):
        super().__init__()
        assert len(symbols) > 0
        self.symbols = symbols

    @property
    def name(self):
        return str(sorted(self.symbols))

    def play(self, target, ctx=None):
        '''
        Play this multisymbol against the target
        '''
        # TODO: Implement MultiSymbol
