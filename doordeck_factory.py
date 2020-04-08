
from doordeck import DoorDeck
from enemy import Enemy
from event import Event
from miniboss import Miniboss
import random
from symbols import Symbols
import copy
import json


class DoorDeckFactory:
    '''
    Takes care of loading DoorCards from wherever they come from :)
    '''

    def __init__(self):
        with open('resources/door_cards.json', 'r') as file:
            self.door_cards = json.loads(file.read())
        with open('resources/challenge_cards.json', 'r') as file:
            self.challenge_cards = json.loads(file.read())

        # Convert symbol names to enums
        for card in self.door_cards:
            card['symbols'] = [Symbols.convert(s) for s in card['symbols']]

    def deal(self, num_door_cards, num_challenge_cards):
        '''
        Deal out and return a DoorDeck with the given num_cards.
        '''

        def draw_challenge_card():
            '''
            Draw a random challenge card from our big stash and initialize it.
            '''

            pick = copy.deepcopy(random.choice(self.challenge_cards))
            if pick['challenge_type'] == 'miniboss':
                # We drew a Miniboss
                return Miniboss(pick['name'], pick['symbols'])
            else:
                # We draw an Event
                return Event(pick['name'])

        def draw_door_card():
            '''
            Draw a random door card from our big stash and initialize it.
            '''

            pick = copy.deepcopy(random.choice(self.door_cards))

            return Enemy(pick['name'], pick['symbols'], pick['type'])

        # Draw num_cards
        cards = [draw_door_card() for _ in range(0, num_door_cards)]

        # Add 2 challenge cards per player
        cards += [draw_challenge_card() for _ in range(0, num_challenge_cards)]

        # Shuffle challenge cards in
        random.shuffle(cards)

        return DoorDeck(cards)
