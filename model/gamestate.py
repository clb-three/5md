
from threading import Lock

from model.message import Message

from .doorcards.types import DoorCardTypes
from .event_timeout import EventTimeout
from .serialization.stringable import Stringable


class GameState(Stringable):
    '''
    A set of boss mat, door deck, target, and a set of heroes.
    '''

    def __init__(self, heroes=None, door_deck=None, target=None, boss=None):
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

        # If card is not valid, don't let it be played
        if not card:
            return Message('invalidcard')

        # Check if the card is in the hero's hand
        if not hero.has_card(card):
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
                [target_msg, Message(
                    'playcard', [hero, card]), effect]
                if m is not None]

    def update_target(self):
        '''
        Switch to next enemy or boss when all enemies are dead
        '''

        if self.target is not None and self.target.is_dead():
            if self.target == self.boss:
                return Message('state', 'killboss')
            else:
                if self.door_deck.try_draw():
                    self.target = self.door_deck.current_enemy

                    if self.target.type == DoorCardTypes.event:
                        self.start_event(self.target)
                        return Message('event', self.target)

                    return Message('enemy', self.target)
                else:
                    self.target = self.boss
                    return Message('boss', self.target)

    def start_event(self, event):
        '''
        Schedule running the event's script on the model.
        '''

        if not event.do_script:
            return

        # Else run the script

        self.event_task = EventTimeout(event, self)
        self.event_task.start()

    def is_defeated(self):
        return self.target == self.boss and self.boss.is_dead()
