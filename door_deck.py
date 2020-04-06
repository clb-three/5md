# A deck of door cards you must defeat

from door_card import DoorCard


class DoorDeck:
    '''
    A DoorDeck is a closed system of door cards.
    Reveals the top door card to fight the players until we're out of cards.
    '''

    def __init__(self, num_cards):
        '''
        Create a new DoorDeck with the given num_cards.
        '''

        super().__init__()
        # Place an initial deck of 5 enemies
        self.enemy_deck = [DoorCard() for _ in range(0, num_cards)]

        # The enemy face up on the top of the deck
        self.current_enemy = None

        self.try_draw()

    def try_draw(self):
        '''
        Discard the current top card and draw the next one.
        '''

        if len(self.enemy_deck) > 0:
            self.current_enemy = self.enemy_deck.pop()
            return True
        else:
            return False
