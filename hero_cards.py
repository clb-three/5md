from symbols import Symbols


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
