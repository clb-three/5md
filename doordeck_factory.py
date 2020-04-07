
from doordeck import DoorDeck
from doorcard import DoorCard
import random
from symbols import Symbols


class DoorDeckFactory:
    '''
    Takes care of loading DoorCards from wherever they come from :)
    '''

    def __init__(self):
        import json
        with open('resources/door_cards.json', 'r') as file:
            self.door_cards = json.loads(file.read())

        # Convert symbol names to enums
        for card in self.door_cards:
            card.symbols = map(Symbols.convert, card.symbols)

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

        cards = [self.draw_door_card() for _ in range(0, num_cards)]

        return DoorDeck(cards)
