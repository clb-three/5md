import pytest
from enemy import Enemy
from symbols import Symbols
from hero_cards import MultiSymbol


from coolname import generate_slug


def mock_enemy(symbols):
    return Enemy(generate_slug(), symbols)


def test_spawns_alive():
    d = mock_enemy([Symbols.jump, Symbols.arrow])
    assert d.is_dead() is False


def test_kill_simple():
    d = mock_enemy([Symbols.sword, Symbols.arrow])
    d.attack(Symbols.sword)
    assert d.is_dead() is False
    d.attack(Symbols.arrow)
    assert d.is_dead() is True


def test_attack_simple():
    d = mock_enemy([Symbols.shield, Symbols.arrow])
    assert d.attack(Symbols.shield) is True
    assert d.attack(Symbols.shield) is False


def test_miss_multisymbol():
    d = mock_enemy([Symbols.jump, Symbols.sword])
    # None match
    ms_broke = MultiSymbol(Symbols.shield, Symbols.arrow)
    assert d.attack(ms_broke) is False


def test_kill_multisymbol():
    d = mock_enemy([Symbols.shield, Symbols.arrow])
    assert d.is_dead() is False
    ms = MultiSymbol(Symbols.shield, Symbols.arrow)
    assert d.attack(ms) is True
    assert d.is_dead() is True


def test_attack_twice_multisymbol():
    d = mock_enemy([Symbols.jump, Symbols.sword])
    # One match
    assert d.attack(MultiSymbol(Symbols.jump)) is True
    # One match (and should kill)
    assert d.attack(MultiSymbol(Symbols.sword)) is True
    assert d.is_dead() is True
