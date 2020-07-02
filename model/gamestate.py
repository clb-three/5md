
from threading import Lock

from .doorcards.types import DoorCardTypes
from .event_timeout import EventTimeout
from .serialization.stringable import Stringable


class GameState(Stringable):
    '''
    A set of boss mat, door deck, target, and a set of heroes.
    '''

    def __init__(self, notifier, heroes=None, door_deck=None, target=None, boss=None):
        self.notifier = notifier

        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss
        self.target = target
        self.event_task = None
        self.mutex = Lock()

    def play_card(self, hero, card):
        '''
        Play the given card against the current enemy
        '''

        # If card is not valid, don't let it be played
        if not card:
            self.notifier.error('invalidcard')
            return

        # Check if the card is in the hero's hand
        if not hero.has_card(card):
            self.notifier.error('notinhand')
            return

        # Play the card
        try:
            self.mutex.acquire()
            effect = card.play(self.target, self)
            hero.discard(card)
            self.update_target()
        finally:
            self.mutex.release()

        self.notifier.info(f'playcard {hero.name} {card} {effect}')

    def update_target(self):
        '''
        Switch to next enemy or boss when all enemies are dead
        '''

        if self.target.is_dead():
            if self.target == self.boss:
                msg = 'killboss'
            else:
                if self.door_deck.try_draw():
                    self.target = self.door_deck.current_enemy

                    if self.target.type == DoorCardTypes.event:
                        self.start_event(self.target)
                        return f'nowevent {self.target}'

                    msg = f'nowenemy "{self.target}"'
                else:
                    self.target = self.boss
                    msg = f'nowboss "{self.boss}'

            self.notifier.info(msg)

    def start_event(self, event):
        '''
        Schedule running the event's script on the model.
        '''

        if not event.do_script:
            return

        # Else run the script
        # self.notifier.log('Running target script')

        self.event_task = EventTimeout(event, self)
        self.event_task.start()

    def is_defeated(self):
        return self.target == self.boss and self.boss.is_dead()
