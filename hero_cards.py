from symbols import Symbols



def deck():
    '''
    The deck for a given hero.
    TODO: Make this different depending on the hero.
    '''
    return Symbols.__members__.values()



def is_valid(card):
    '''
    Return whether card is valid
    '''
    return card in Symbols.__members__.keys()
