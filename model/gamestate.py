from collections import defaultdict

from .serialization.stringable import Stringable


class GameState(Stringable):
    """
    A set of boss mat, door deck, target, and a set of heroes.
    """

    def __init__(self, door_deck=None, heroes=[]):
        self.heroes = heroes
        self.door_deck = door_deck

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

    def flip(self):
        if self.door_deck.flip():
            yield Message('enemy', self.door_deck.top)
            if self.door_deck.top.type == DoorCardTypes.event:
                self.schedule(self.door_deck.top.do_script)

    @property
    def is_defeated(self):
        return self.door_deck.top == self.door_deck.boss and self.door_deck.boss.is_dead()
