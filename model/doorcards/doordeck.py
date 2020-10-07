# A deck of door cards you must defeat
from model.serialization.stringable import Stringable


class DoorDeck(Stringable):
    """
    A DoorDeck is a closed system of door cards.
    Reveals the top door card to fight the players until we're out of cards.
    """

    def __init__(self, cards):
        """
        Create a new DoorDeck with the given cards.
        """

        super().__init__()
        # Place an initial deck of 5 enemies
        self.deck = cards

    @property
    def top(self):
        if len(self.deck):
            return self.deck[0]

    def try_draw(self):
        """
        Discard the current top card and draw the next one.
        """

        if len(self.deck) > 0:
            self.deck.pop(0)
            return True
        else:
            return False

    def put_on_top(self, card):
        """
        Put the given card on top.
        """

        self.deck.insert(0, card)
