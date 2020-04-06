
from door_card import DoorCard


def deal_door_deck(num_cards):
    '''
    Deal out and return a DoorDeck with the given num_cards.
    '''
    symbols = ['sword', 'shield', 'arrow']
    return [DoorCard(symbols) for _ in range(0, num_cards)]
