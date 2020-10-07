# pylint: disable=W0201
import pytest

from . import test_mocks as mock
from .symbol import Symbol


class TestTable:
    def setup_method(self):
        self.hero, self.table = mock.table(mock.enemy(Symbol.sword))

    def test_draw(self):
        assert len(self.hero.hand) == 0
        assert len(self.hero.deck) == 1
        self.table.draw_card(self.hero)
        assert len(self.hero.hand) == 1
        assert len(self.hero.deck) == 0

    def test_play(self):
        assert len(self.hero.hand) == 0
        self.hero.draw_card()
        assert len(self.hero.hand) == 1
        self.table.play_card(self.hero, self.hero.hand[0])
        assert len(self.hero.hand) == 0

    @pytest.mark.xfail
    def test_play_fail(self):
        assert len(self.hero.hand) == 0
        self.table.process_hero_command(self.hero, ['play', 'sword'])

    def test_discard(self):
        assert len(self.hero.hand) == 0
        self.hero.draw_card()
        assert len(self.hero.hand) == 1
        self.table.discard_card(self.hero, self.hero.hand[0])
        assert len(self.hero.hand) == 0

    @pytest.mark.xfail
    def test_discard_fail(self):
        assert len(self.hero.hand) == 0
        self.table.process_hero_command(self.hero, ['discard', 'sword'])
