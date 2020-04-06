
from door_deck import DoorDeck
from door_card import DoorCard
import random


class DoorDeckFactory:
    '''
    Takes care of loading DoorCards from wherever they come from :)
    '''

    def __init__(self):
        self.door_cards = [
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

    def random_door_card(self):
        return random.choice(self.door_cards)

    def draw_door_card(self):
        '''
        Draw a random door card from our big stash and initialize it.
        '''

        card = self.random_door_card()

        return DoorCard(card["name"], card["symbols"], card["type"])

    def create(self, num_cards):
        '''
        Deal out and return a DoorDeck with the given num_cards.
        '''

        # TODO: Add 2 challenge cards per player.

        symbols = ['sword', 'shield', 'arrow']
        cards = [self.draw_door_card() for _ in range(0, num_cards)]

        return DoorDeck(cards)
