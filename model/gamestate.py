from collections import defaultdict

from .serialization.stringable import Stringable


class GameState(Stringable):
    """
    A set of boss mat, door deck, target, and a set of heroes.
    """

    def __init__(self, heroes=None, door_deck=None, boss=None):
        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss

        self.time = 0
        self.events = defaultdict(list)

    def step(self):
        """
        Step time forward and do the action that's scheduled.
        """

        self.time += 1
        for event in self.events[self.time]:
            event(self)
        del self.events[self.time]

    def schedule(self, event, how_far):
        """
        Schedule an event how_far into the future.
        """

        scheduled_time = self.time + how_far
        assert (scheduled_time > self.time)
        self.events[scheduled_time].append(event)

    @property
    def target(self):
        if self.door_deck.top:
            return self.door_deck.top
        else:
            return self.boss

    @property
    def is_defeated(self):
        return self.target == self.boss and self.boss.is_dead()
