'''All major DoorCard types'''
from enum import Enum, auto, unique


@unique
class DoorCardTypes(Enum):
    '''All major DoorCard types'''
    boss = auto()
    monster = auto()
    event = auto()
    miniboss = auto()
