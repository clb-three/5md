
from threading import Lock

from model.message import Message

from .doorcards.types import DoorCardTypes
from .event_timeout import EventTimeout
from .serialization.stringable import Stringable


class GameState(Stringable):
    """
    A set of boss mat, door deck, target, and a set of heroes.
    """

    def __init__(self, heroes=None, door_deck=None, boss=None):
        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss
        self.target = target
        self.event_task = None
        self.mutex = Lock()
        self.update_target()

    def play_card(self, hero, card):
        '''
        Play the given card against the current enemy
        '''

        # Check if the card is in the hero's hand
        card = hero.get_card_from_hand(card)
        if not card:
            return Message('notinhand', card)

        # Play the card
        try:
            self.mutex.acquire()
            effect = card.play(self.target, self)
            hero.discard(card)
            target_msg = self.update_target()
        finally:
            self.mutex.release()

        return [m for m in
                [Message(
                    'playcard', [hero, card]), effect, target_msg]
                if m is not None]

    def update_target(self):
        '''
        Switch to next enemy or boss when all enemies are dead
        '''

    @property
    def target(self):
        if self.door_deck.top:
            return self.door_deck.top
        else:
            self.target = self.boss

    @property
    def is_defeated(self):
        return self.target == self.boss and self.boss.is_dead()
