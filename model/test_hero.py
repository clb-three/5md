# pylint: disable=W0201
import random

import pytest

from . import test_mocks as mock
from .heroes.complaint import Complaint
from .symbol import Symbol


class TestHero:
    def setup_method(self):
        self.hero = mock.hero('barbarian')

    def test_hero_created_empty(self):
        assert len(self.hero.hand) is 0

    def test_draw_a_lot(self):
        for _ in range(len(self.hero.deck)):
            assert self.hero.draw_card() is not None

        with pytest.raises(Complaint):
            self.hero.draw_card()

    def test_get_by_name(self):
        for _ in range(3):
            self.hero.draw_card()

        first_card = random.choice(self.hero.hand)
        self.hero.get_card_from_hand(first_card.name)

    def test_get_by_uuid(self):
        for _ in range(3):
            self.hero.draw_card()

        first_card = random.choice(self.hero.hand)
        self.hero.get_card_from_hand(first_card.uuid)

    def test_discard(self):
        card = self.hero.draw_card()
        assert len(self.hero.hand) is 1
        self.hero.discard(card)
        assert len(self.hero.hand) is 0

    def test_discard_when_hand_empty(self):
        with pytest.raises(Complaint):
            self.hero.discard(Symbol.sword)
