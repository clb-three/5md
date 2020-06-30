import random

from model.symbol import Symbol

from .hero import Hero
from .singlesymbol import SingleSymbol


def draw_deck(classname):
    '''
    The deck for a given hero.
    TODO: Draw different cards different depending on the hero.
    '''
    return list([SingleSymbol(s) for s in dict(Symbol.__members__).values()])


def hero(name, classname):
    deck = [random.choice(draw_deck(classname))
            for _ in range(0, 40)]

    return Hero(name, classname, deck)


def get_card(card_name):
    for s in dict(Symbol.__members__).values():
        if str(s) == card_name:
            return SingleSymbol(s)
    # TODO: Other card types
