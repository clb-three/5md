import pytest
from door_card import DoorCard


def test_is_dead():
    d = DoorCard('slime', ['jump', 'arrow'], 'monster')
    assert d.is_dead() is False


def test_kill():
    d = DoorCard('slime', ['jump', 'arrow'], 'monster')
    d.try_attack('jump')
    assert d.is_dead() is False
    d.try_attack('arrow')
    assert d.is_dead() is True


def test_try_attack():
    d = DoorCard('slime', ['jump', 'arrow'], 'monster')
    assert d.try_attack('shovel') is False
    assert d.try_attack('jump') is True
    assert d.try_attack('jump') is False
