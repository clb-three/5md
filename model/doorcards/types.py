from enum import Enum, unique, auto


@unique
class DoorCardTypes(Enum):
    boss = auto()
    monster = auto()
    event = auto()
    miniboss = auto()
