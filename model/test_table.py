from .test_utils import mock_enemy
from .heroes.hero import Hero
from .gamestate import GameState
from .doorcards.doordeck import DoorDeck
from .doorcards.event import Event
from .symbol import Symbol
from .heroes.singlesymbol import SingleSymbol
from .doorcards.boss import Boss
from .table import Table
import pytest


def mock_scenario():
    benji = Hero('benji', 'ranger', [SingleSymbol(Symbol.sword)])
    heroes = {
        'benji': benji
    }
    target = mock_enemy([Symbol.sword])
    door_deck = DoorDeck([mock_enemy([Symbol.arrow]), Event('ooo'), target])
    assert target == door_deck.current_enemy
    boss = Boss([Symbol.jump], 10)
    state = GameState(heroes, door_deck, door_deck.current_enemy, boss)
    return benji, Table(state)


def test_quit():
    _, table = mock_scenario()
    assert table.game_over == False
    table.process_command('quit')
    assert table.game_over == True


def test_last_command():
    _, table = mock_scenario()
    table.process_command('nuke')
    assert table.last_command == 'nuke'
    table.process_command('')
    assert table.last_command == 'nuke'
    table.process_command('benji play sword')
    assert table.last_command == 'benji play sword'


def test_nuke():
    _, table = mock_scenario()
    assert table.gamestate.target != None
    old_target = table.gamestate.target
    table.process_command('nuke')
    assert table.gamestate.target != old_target


def test_draw():
    hero, table = mock_scenario()
    assert hero.hand_size() == 0
    assert hero.deck_size() == 1
    table.process_hero_command(hero, ['draw'])
    assert hero.hand_size() == 1
    assert hero.deck_size() == 0


def test_play():
    hero, table = mock_scenario()
    assert hero.hand_size() == 0
    hero.draw_card()
    assert hero.hand_size() == 1
    table.process_hero_command(hero, ['play', 'sword'])
    assert hero.hand_size() == 0


@pytest.mark.xfail
def test_play_fail():
    hero, table = mock_scenario()
    assert hero.hand_size() == 0
    table.process_hero_command(hero, ['play', 'sword'])


def test_discard():
    hero, table = mock_scenario()
    assert hero.hand_size() == 0
    hero.draw_card()
    assert hero.hand_size() == 1
    table.process_hero_command(hero, ['discard', 'sword'])
    assert hero.hand_size() == 0


@pytest.mark.xfail
def test_discard_fail():
    hero, table = mock_scenario()
    assert hero.hand_size() == 0
    table.process_hero_command(hero, ['discard', 'sword'])
