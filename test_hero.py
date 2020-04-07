import pytest
from hero import Hero


def test_hero_created_empty():
    h = Hero('benji')
    assert len(h.hand) is 0


def test_draw_a_lot():
    h = Hero('benji')
    for _ in range(h.deck_size()):
        assert h.draw_card() is not None

    assert h.draw_card() is None


def test_draw_a_lot():
    h = Hero('benji')
    for _ in range(h.deck_size()):
        assert h.draw_card() is not None

    assert h.draw_card() is None


def test_discard():
    h = Hero('benji')
    assert h.hand_size() is 0
    card = h.draw_card()
    assert h.hand_size() is 1
    h.discard(card)
    assert h.hand_size() is 0


def test_discard_dont_have():
    h = Hero('benji')

    assert h.discard('shovel') is None
