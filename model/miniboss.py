
from .enemy import Enemy
from .doorcard import DoorCardTypes


class Miniboss(Enemy):
    '''
    Miniboss is a special case of an Enemy
    '''

    def __init__(self, name, symbols):
        super().__init__(name, symbols, DoorCardTypes.miniboss)
