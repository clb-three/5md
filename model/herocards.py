from .symbol import Symbol
from .singlesymbol import SingleSymbol


def all(classname):
    '''
    The deck for a given hero.
    TODO: Draw different cards different depending on the hero.
    '''
    return list([SingleSymbol(s) for s in Symbol.__members__.values()])
