'''All major DoorCard types'''
from enum import Enum, unique


@unique
class DoorCardTypes(str, Enum):
    '''
    All major DoorCard types.
    Inherits from str so that it is serializable.
    '''
    boss = 'boss'
    monster = 'monster'
    event = 'event'
    miniboss = 'miniboss'

    def __str__(self):
        return str(self.name)
