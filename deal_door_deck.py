
from door_card import DoorCard
import random

door_cards = [
    {
        "name": "Slime",
        "symbols": ["jump", "arrow"],
        "type": "monster",
    },
    {
        "name": "Sir Fuzzylumps",
        "symbols": ["jump", "arrow", "arrow"],
        "type": "monster",
    }
]


def random_door_card():
    return random.choice(door_cards)


def draw_door_card():
    '''
    Draw a random door card from our big stash and initialize it.
    '''

    card = random_door_card()

    return DoorCard(card["symbols"])


def deal_door_deck(num_cards):
    '''
    Deal out and return a DoorDeck with the given num_cards.
    '''

    # TODO: Add 2 challenge cards per player.

    symbols = ['sword', 'shield', 'arrow']
    return [draw_door_card() for _ in range(0, num_cards)]
