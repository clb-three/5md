from symbols import Symbols


def deck():
    '''
    The deck for a given hero.
    TODO: Make this different depending on the hero.
    '''
    return list(Symbols.__members__.values())


def get(card_name):
    '''
    Return card object for a given name
    '''
    return Symbols.convert(card_name)
