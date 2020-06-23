from .symbol import Symbol


class MultiSymbol():
    def __init__(self, *symbols):
        super().__init__()
        assert len(symbols) > 0
        self.symbols = symbols

    def play(self, ctx):
        '''
        Play this multisymbol against the target
        '''
        pass  # TODO: Implement MultiSymbol


if __name__ == '__main__':
    c = MultiSymbol(Symbol.arrow, Symbol.jump)
