import pytest
from doorcard import DoorCard


def test_is_dead():
    d = DoorCard('slime', ['jump', 'arrow'], 'monster')
    assert d.is_dead() is False


def test_kill():
    d = DoorCard('slime', ['jump', 'arrow'], 'monster')
    d.attack('jump')
    assert d.is_dead() is False
    d.attack('arrow')
    assert d.is_dead() is True


def test_attack():
    d = DoorCard('slime', ['jump', 'arrow'], 'monster')
    assert d.attack('shovel') is False
    assert d.attack('jump') is True
    assert d.attack('jump') is False
