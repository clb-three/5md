from .private.base import BaseDoorCard, DoorCardTypes


class Boss(BaseDoorCard):
    '''
    This is the big boss (hunk of symbol cards)
    at the bottom of a boss mat.
    '''

    def __init__(self, symbols, num_door_cards):
        # TODO: These should come from store somewhere,
        # and be referenced just by the boss's name.
        super().__init__(symbols, DoorCardTypes.boss)
        self.num_door_cards = num_door_cards
