
from copy import deepcopy

from .enemy import Enemy
from .types import DoorCardTypes


class Miniboss(Enemy):
    '''
    Miniboss is a special case of an Enemy
    '''

    def __init__(self, name, symbols):
        super().__init__(name, symbols, DoorCardTypes.miniboss)

    def deepcopy(self):
        return Miniboss(deepcopy(self.name), deepcopy(self.symbols))
