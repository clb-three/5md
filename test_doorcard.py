import pytest
from enemy import Enemy
from symbol import Symbol
from multisymbol import MultiSymbol
from test_utils import mock_enemy


def test_spawns_alive():
    d = mock_enemy([Symbol.jump, Symbol.arrow])
    assert d.is_dead() is False


def test_kill_simple():
    d = mock_enemy([Symbol.sword, Symbol.arrow])
    d.attack(Symbol.sword)
    assert d.is_dead() is False
    d.attack(Symbol.arrow)
    assert d.is_dead() is True


def test_attack_simple():
    d = mock_enemy([Symbol.shield, Symbol.arrow])
    assert d.attack(Symbol.shield) is True
    assert d.attack(Symbol.shield) is False


def test_miss_multisymbol():
    d = mock_enemy([Symbol.jump, Symbol.sword])
    # None match
    ms_broke = MultiSymbol(Symbol.shield, Symbol.arrow)
    assert d.attack(ms_broke) is False


def test_kill_multisymbol():
    d = mock_enemy([Symbol.shield, Symbol.arrow])
    assert d.is_dead() is False
    ms = MultiSymbol(Symbol.shield, Symbol.arrow)
    assert d.attack(ms) is True
    assert d.is_dead() is True


def test_attack_twice_multisymbol():
    d = mock_enemy([Symbol.jump, Symbol.sword])
    # One match
    assert d.attack(MultiSymbol(Symbol.jump)) is True
    # One match (and should kill)
    assert d.attack(MultiSymbol(Symbol.sword)) is True
    assert d.is_dead() is True
