import pytest

from . import test_mocks as mock
from .heroes.complaint import Complaint
from .symbol import Symbol


class TestHero():
    def __init__(self):
        self.hero = None

    def setup_method(self):
        self.hero = mock.hero('barbarian')

    def test_hero_created_empty(self):
        assert len(self.hero.hand) is 0

    def test_draw_a_lot(self):
        for _ in range(self.hero.deck_size()):
            assert self.hero.draw_card() is not None

        with pytest.raises(Complaint):
            self.hero.draw_card()

    def test_discard(self):
        card = self.hero.draw_card()
        assert len(self.hero.hand) is 1
        self.hero.discard(card)
        assert len(self.hero.hand) is 0

    def test_discard_when_hand_empty(self):
        with pytest.raises(Complaint):
            self.hero.discard(Symbol.sword)
