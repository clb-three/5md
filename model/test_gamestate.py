import logging

from .gamestate import GameState


class Touchable:
    """Support class to give a flag to test simple event execution."""

    def __init__(self):
        self.touched = False

    def touch(self):
        self.touched = True


class TestGameStateEvents:
    def setup_method(self):
        self.g = GameState(logging=logging)
        self.t = Touchable()
        self.touched = False
        self.g.schedule(lambda _: self.t.touch(), 30)

    def test_simple_event(self):
        for _ in range(30):
            self.g.step()

        assert self.t.touched

    def test_too_early_event(self):
        for _ in range(3):
            self.g.step()

        assert not self.t.touched
