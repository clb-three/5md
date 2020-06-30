
import json

from .doorcards.types import DoorCardTypes
from .event_timeout import EventTimeout


class GameState:
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
        hero.discard(card)
        effect = card.play(self.target, self)
        self.notifier.info(f'playcard "{hero.name}" "{card}" "{effect}"')

        self.update_target()

    def draw(self):
        if self.door_deck.try_draw():
            self.target = self.door_deck.current_enemy

            if self.target.type == DoorCardTypes.event:
                self.notifier.info(f'nowevent {self.target}')
                self.start_event(self.target)
                return self.draw()
            else:
                msg = f'nowenemy "{self.target}"'
        else:
            msg = f'nowboss "{self.boss}'
            self.target = self.boss
        return msg

    def update_target(self):
        '''
        Switch to next enemy or boss when all enemies are dead
        '''

        if self.target.is_dead():
            if self.target == self.boss:
                msg = 'killboss'
            else:
                msg = self.draw()

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

    def __str__(self):
        heroes = {n: o.__dict__() for n, o in self.heroes.items()}
        selfobj = {
            'heroes': heroes,
            'door_deck': self.door_deck.__dict__(),
            'boss': self.boss.__dict__(),
            'target': self.target.__dict__(),
        }
        return json.dumps(selfobj)
