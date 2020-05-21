import pytest
from enemy import Enemy
from symbols import Symbols


def test_is_dead():
    d = Enemy('slime', [Symbols.jump, Symbols.arrow])
    assert d.is_dead() is False


def test_kill():
    d = Enemy('slime', [Symbols.jump, Symbols.arrow])
    d.attack(Symbols.jump)
    assert d.is_dead() is False
    d.attack(Symbols.arrow)
    assert d.is_dead() is True


def test_attack():
    d = Enemy('slime', [Symbols.jump, Symbols.arrow])
    assert d.attack(Symbols.jump) is True
    assert d.attack(Symbols.jump) is False
