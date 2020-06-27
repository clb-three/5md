# pylint: disable=W0201
import pytest

from . import test_mocks as mock
from .symbol import Symbol


class TestTable():
    def setup_method(self):
        self.hero, self.table = mock.table(mock.enemy(Symbol.sword))

    def test_quit(self):
        assert not self.table.game_over
        self.table.process_command('quit')
        assert self.table.game_over

    def test_last_command(self):
        self.table.process_command('nuke')
        assert self.table.last_command == 'nuke'
        self.table.process_command('')
        assert self.table.last_command == 'nuke'
        self.table.process_command('benji play sword')
        assert self.table.last_command == 'benji play sword'

    def test_nuke(self):
        assert self.table.gamestate.target is None
        old_target = self.table.gamestate.target
        self.table.process_command('nuke')
        assert self.table.gamestate.target != old_target

    def test_draw(self):
        assert self.hero.hand_size() == 0
        assert self.hero.deck_size() == 1
        self.table.process_hero_command(self.hero, ['draw'])
        assert self.hero.hand_size() == 1
        assert self.hero.deck_size() == 0

    def test_play(self):
        assert self.hero.hand_size() == 0
        self.hero.draw_card()
        assert self.hero.hand_size() == 1
        self.table.process_hero_command(self.hero, ['play', 'sword'])
        assert self.hero.hand_size() == 0

    @pytest.mark.xfail
    def test_play_fail(self):
        assert self.hero.hand_size() == 0
        self.table.process_hero_command(self.hero, ['play', 'sword'])

    def test_discard(self):
        assert self.hero.hand_size() == 0
        self.hero.draw_card()
        assert self.hero.hand_size() == 1
        self.table.process_hero_command(self.hero, ['discard', 'sword'])
        assert self.hero.hand_size() == 0

    @pytest.mark.xfail
    def test_discard_fail(self):
        assert self.hero.hand_size() == 0
        self.table.process_hero_command(self.hero, ['discard', 'sword'])
