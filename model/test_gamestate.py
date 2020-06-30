# pylint: disable=W0201
import time

from . import test_mocks as mock
from .doorcards.boss import Boss
from .doorcards.event import Event
from .event_timeout import EventTimeout
from .symbol import Symbol


class TestGameState():
    def setup_method(self):
        deck = mock.door_deck(mock.enemy([Symbol.sword]))
        boss = Boss([Symbol.jump], 1)
        heroes = mock.gen_mock_heroes(1)
        self.state = mock.gamestate(deck, boss, heroes)
        self.state.update_target()

    def test_event_timeout(self):
        self.flag = False

        def trigger(_):
            self.flag = True

        self.state.start_event(Event('Testy', trigger))
        assert self.flag is False
        time.sleep(EventTimeout.DEFAULT_TIMEOUT_SEC + 1)
        assert self.flag is True
