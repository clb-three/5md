

from attackable import Attackable


class Boss(Attackable):
    def __init__(self, symbols, num_door_cards):
        # TODO: These should come from store somewhere,
        # and be referenced just by the boss's name.
        super().__init__(symbols)
        self.num_door_cards = num_door_cards
