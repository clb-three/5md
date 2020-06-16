
from doordeck import DoorDeck
from enemy import Enemy
from event import Event
from miniboss import Miniboss
import random
from symbol import Symbol
import copy
import json


class DoorDeckFactory:
    '''
    Takes care of loading DoorCards from wherever they come from :)
    '''

    def init_enemy(self, dict):
        return None

    def __init__(self, ctx):
        def init_symbols(symbols): return [Symbol.convert(s) for s in symbols]

        with open('resources/door_cards.json', 'r') as file:
            self.door_cards = [
                Enemy(c['name'], init_symbols(c['symbols']), c['type']) for c in json.load(file)]
        with open('resources/minibosses.json', 'r') as minibosses, open('resources/events.json', 'r') as events:
            self.challenge_cards = \
                [Miniboss(c['name'], init_symbols(c['symbols']))
                 for c in json.load(minibosses)] + \
                [Event(c['name'], ctx, c['script_name'])
                 for c in json.load(events)]

    def deal(self, num_door_cards, num_challenge_cards):
        '''
        Deal out and return a DoorDeck with the given num_cards.
        '''

        def draw_challenge_card():
            '''
            Draw a random challenge card from our big stash and initialize it.
            '''

            return copy.deepcopy(random.choice(self.challenge_cards))

        def draw_door_card():
            '''
            Draw a random door card from our big stash and initialize it.
            '''

            return copy.deepcopy(random.choice(self.door_cards))

        # Draw num_cards
        cards = [draw_door_card() for _ in range(0, num_door_cards)]

        # Add 2 challenge cards per player
        cards += [draw_challenge_card() for _ in range(0, num_challenge_cards)]

        # Shuffle challenge cards in
        random.shuffle(cards)

        return DoorDeck(cards)
