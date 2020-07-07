# pylint: disable=W0201
import time

import pytest

from . import test_mocks as mock
from .doorcards.boss import Boss
from .doorcards.event import Event
from .event_timeout import EventTimeout
from .symbol import Symbol


class TestGameState():
    def setup_method(self):
        self.event = Event('Testy', self.trigger)
        deck = mock.door_deck([self.event, mock.enemy(Symbol.sword)])
        boss = Boss([Symbol.jump], 1)
        heroes = mock.gen_mock_heroes(1)
        self.state = mock.gamestate(deck, boss, heroes)

        self.flag = False

    def trigger(self, _):
        self.flag = True

    @pytest.mark.skip
    def test_event_timeout(self):
        assert self.state.target is self.event
        self.state.start_event(self.event)
        assert self.flag is False
        time.sleep(EventTimeout.DEFAULT_TIMEOUT_SEC + 1)
        assert self.flag is True

    def test_event_timeout_canceled(self):
        def trigger(_):
            self.flag = True

        self.state.start_event(Event('Testy', trigger))
        assert self.flag is False
        self.state.target.kill()
        self.state.update_target()
        assert self.flag is False
