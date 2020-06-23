from coolname import generate_slug
from .hero import Hero
from .enemy import Enemy
from .game import Game
from .doordeck import DoorDeck


def mock_hero():
    return Hero(generate_slug(), 'ranger')


def gen_mock_heroes(howmany):
    heroes = [mock_hero() for _ in range(howmany)]
    return {h.name: h for h in heroes}


def mock_enemy(symbols):
    return Enemy(generate_slug(), symbols)


def mock_enemy_ctx(enemy):
    dd = DoorDeck([enemy])
    return Game(door_deck=dd, target=dd.current_enemy)
