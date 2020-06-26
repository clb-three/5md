
from .doordeck import DoorDeck
from .enemy import Enemy
from .event import Event
from .miniboss import Miniboss
from .boss import Boss
from ..symbol import Symbol
import random
import copy
import json
from pathlib import Path


def draw_deck():
    def init_symbols(symbols): return [Symbol.convert(s) for s in symbols]

    resources_dir = Path(__file__).parent / 'resources'

    with open(resources_dir / 'door_cards.json', 'r') as file:
        door_cards = [
            Enemy(c['name'], init_symbols(c['symbols']), c['type']) for c in json.load(file)]

    with open(resources_dir / 'minibosses.json', 'r') as minibosses, open(resources_dir / 'events.json', 'r') as events:
        challenge_cards = \
            [Miniboss(c['name'], init_symbols(c['symbols']))
                for c in json.load(minibosses)] + \
            [Event(c['name'], c['script_name'])
                for c in json.load(events)]

    return door_cards, challenge_cards


def deal_deck(num_door_cards, num_players):
    '''
    Deal out and return a DoorDeck with the given num_cards.
    '''

    def draw_random(deck): return random.choice(deck)
    door_cards, challenge_cards = draw_deck()

    cards = []

    # Draw num_cards door cards
    cards += [draw_random(door_cards) for _ in range(0, num_door_cards)]

    # Add 2 challenge cards per player
    cards += [draw_random(challenge_cards)
              for _ in range(0, 2 * num_players)]

    # Shuffle challenge cards in
    random.shuffle(cards)

    return DoorDeck(cards)


def create_boss():
    return Boss([Symbol.arrow, Symbol.jump], 20)
