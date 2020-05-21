from symbols import Symbols


class MultiSymbol():
    def __init__(self, *symbols):
        super().__init__()
        assert len(symbols) > 0
        self.symbols = symbols


def all(classname):
    '''
    The deck for a given hero.
    TODO: Draw different cards different depending on the hero.
    '''
    return list(Symbols.__members__.values())


def get(card_name):
    '''
    Return card object for a given name
    '''
    return Symbols.convert(card_name)


if __name__ == '__main__':
    c = MultiSymbol(Symbols.arrow, Symbols.jump)
