from .private.base import BaseDoorCard
from .private.types import DoorCardTypes
from copy import deepcopy


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

    def __dict__(self):
        selfobj = super().__dict__()
        selfobj['num_door_cards'] = self.num_door_cards

        return selfobj

    def deepcopy(self):
        return Boss(deepcopy(self.symbols), deepcopy(self.num_door_cards))
