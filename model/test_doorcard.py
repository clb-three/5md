from .doorcards.enemy import Enemy
from .symbol import Symbol
from .multisymbol import MultiSymbol
from .test_utils import mock_enemy, mock_enemy_ctx
import pytest


def test_spawns_alive():
    d = mock_enemy([Symbol.jump, Symbol.arrow])
    assert d.is_dead() is False


def test_kill_simple():
    d = mock_enemy([Symbol.jump, Symbol.arrow])
    c = mock_enemy_ctx(d)
    assert d.is_dead() is False
    Symbol.arrow.play(c)
    assert d.is_dead() is False
    Symbol.jump.play(c)
    assert d.is_dead() is True


def test_attack_simple():
    d = mock_enemy_ctx(mock_enemy([Symbol.shield]))
    Symbol.shield.play(d)
    with pytest.raises(Exception):
        Symbol.shield.play(d)


@pytest.mark.xfail  # take this off when you implement it
def test_miss_multisymbol():
    c = mock_enemy_ctx(mock_enemy([Symbol.jump, Symbol.sword]))
    # None match
    ms_broke = MultiSymbol(Symbol.shield, Symbol.arrow)
    with pytest.raises(Exception):
        ms_broke.play(c)


@pytest.mark.xfail  # take this off when you implement it
def test_kill_multisymbol():
    d = mock_enemy([Symbol.shield, Symbol.arrow])
    c = mock_enemy_ctx(d)
    assert d.is_dead() is False
    ms = MultiSymbol(Symbol.shield, Symbol.arrow)
    ms.attack(c)
    assert d.is_dead() is True


@pytest.mark.xfail  # take this off when you implement it
def test_attack_twice_multisymbol():
    d = mock_enemy([Symbol.jump, Symbol.sword])
    # One match
    assert d.attack(MultiSymbol(Symbol.jump)) is True
    # One match (and should kill)
    assert d.attack(MultiSymbol(Symbol.sword)) is True
    assert d.is_dead() is True
