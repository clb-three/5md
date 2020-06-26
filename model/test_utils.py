from coolname import generate_slug
from .heroes.factory import hero
from .gamestate import GameState
from .doorcards.enemy import Enemy
from .doorcards.doordeck import DoorDeck
from .console_notifier import ConsoleNotifier


def mock_hero():
    return hero(generate_slug(), 'ranger')


def gen_mock_heroes(howmany):
    heroes = [mock_hero() for _ in range(howmany)]
    return {h.name: h for h in heroes}


def mock_enemy(symbols):
    return Enemy(generate_slug(), symbols)


def mock_enemy_ctx(enemy):
    dd = DoorDeck([enemy])
    return GameState(notifier=ConsoleNotifier, door_deck=dd, target=dd.current_enemy)
