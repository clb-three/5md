import random

from coolname import generate_slug

from .console_notifier import ConsoleNotifier
from .doorcards import factory as doordeck_factory
from .doorcards.boss import Boss
from .doorcards.doordeck import DoorDeck
from .doorcards.enemy import Enemy
from .gamestate import GameState
from .heroes import factory as hero_factory
from .heroes.hero import Hero
from .heroes.singlesymbol import SingleSymbol
from .symbol import Symbol
from .table import Table


def hero(classname):
    '''Create a Hero with a random name and the given class.'''
    return hero_factory.hero(generate_slug(), classname)


def gen_mock_heroes(howmany):
    '''Create many heroes with random names and classes.'''
    classes = ['ranger', 'barbarian', 'mage']
    heroes = [hero(random.choice(classes)) for _ in range(howmany)]
    return {h.name: h for h in heroes}


def enemy(*symbols):
    '''Create an Enemy with a random name and the given symbols.'''
    return Enemy(generate_slug(), list(symbols))


def door_deck(deck_contents):
    '''Create a DoorDeck with the given cards.'''
    if deck_contents is not list:
        deck_contents = [deck_contents]
    return DoorDeck(deck_contents)


def gamestate(deck=None, boss=None, heroes=None):
    '''Create a GameState with ConsoleNotifier and the given DoorDeck.'''
    target = deck.current_enemy if None is None else deck
    return GameState(notifier=ConsoleNotifier, door_deck=deck, target=target, boss=boss, heroes=heroes)


def table(top_enemy):
    heroname = generate_slug()
    my_hero = Hero(heroname, 'ranger', [SingleSymbol(Symbol.sword)])
    heroes = {
        heroname: my_hero
    }

    deck = doordeck_factory.deal_deck(9, 1)
    deck.put_on_top(top_enemy)
    boss = Boss([Symbol.jump], 10)

    state = GameState(ConsoleNotifier(), heroes,
                      deck, deck.current_enemy, boss)

    return my_hero, Table(state)
