from .heroes.hero import Hero
from .heroes.complaint import Complaint
from .test_utils import mock_hero
from .symbol import Symbol
import pytest


def test_hero_created_empty():
    h = mock_hero()
    assert len(h.hand) is 0


def test_draw_a_lot():
    h = mock_hero()
    for _ in range(h.deck_size()):
        assert h.draw_card() is not None

    with pytest.raises(Complaint):
        assert h.draw_card() is None


def test_discard():
    h = mock_hero()
    assert len(h.hand) is 0
    card = h.draw_card()
    assert len(h.hand) is 1
    h.discard(card)
    assert len(h.hand) is 0


def test_discard_when_hand_empty():
    h = mock_hero()

    with pytest.raises(Complaint):
        assert h.discard(Symbol.sword) is None
