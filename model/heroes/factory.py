from ..symbol import Symbol
from .singlesymbol import SingleSymbol
from .hero import Hero
import random


def draw_deck(classname):
    '''
    The deck for a given hero.
    TODO: Draw different cards different depending on the hero.
    '''
    return list([SingleSymbol(s) for s in Symbol.__members__.values()])


def hero(name, classname):
    deck = [random.choice(draw_deck(classname))
            for _ in range(0, 40)]

    return Hero(name, classname, deck)


def get_card(card_name):
    for s in Symbol.__members__.values():
        if s.__str__() == card_name:
            return SingleSymbol(s)
    # TODO: Other card types