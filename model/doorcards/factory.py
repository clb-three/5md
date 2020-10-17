import json
import random
from pathlib import Path

from model.symbol import Symbol
from .boss import Boss
from .doordeck import DoorDeck
from .enemy import Enemy
from .event import Event
from .miniboss import Miniboss
from .scripts import scripts


def draw_deck():
    def init_symbols(symbols):
        return [Symbol.convert(s) for s in symbols]

    def get_script(name):
        if name is not None:
            if name not in scripts:
                raise Exception(f'Script "{name}" not found.')
            return scripts[name]

    resources_dir = Path(__file__).parent / 'resources'

    with open(resources_dir / 'door_cards.json', 'r') as file:
        door_cards = [
            Enemy(c['name'], init_symbols(c['symbols']), c['type']) for c in json.load(file)]

    with open(resources_dir / 'minibosses.json', 'r') as minibosses, \
            open(resources_dir / 'events.json', 'r') as events:
        challenge_cards = \
            [Miniboss(c['name'], init_symbols(c['symbols']))
             for c in json.load(minibosses)] + \
            [Event(c['name'], get_script(c['script_name']))
             for c in json.load(events)]

    return door_cards, challenge_cards


def deal_deck(num_door_cards, num_players, boss):
    '''
    Deal out and return a DoorDeck with the given num_cards.
    '''

    def draw_random(deck): return random.choice(deck).deepcopy()

    door_cards, challenge_cards = draw_deck()

    cards = []

    # Draw num_cards door cards
    cards += [draw_random(door_cards) for _ in range(0, num_door_cards)]

    # Add 2 challenge cards per player
    cards += [draw_random(challenge_cards)
              for _ in range(0, 2 * num_players)]

    # Shuffle challenge cards in
    random.shuffle(cards)

    return DoorDeck(cards, boss)


def create_boss():
    return Boss([Symbol.arrow, Symbol.jump], 20)
