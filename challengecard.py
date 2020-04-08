# These are cards with a skull on the back, and
# two are mixed into the door deck per player.

from doorcard import DoorCard
from enemy import Enemy

# TODO: Make functionality for Event cards. It'll probably be a class that goes in the door deck.
# When you flip over an Event, your team must immediately do whatever the card says.
# Only the Action Card CANCEL and HOLY HAND GRENADE can prevent your party from doing the Event.


class Event(DoorCard):
    '''
    Event will do something bad to the players!
    '''
    pass


class Miniboss(Enemy):
    '''
    Miniboss is a special case of an Enemy
    '''

    def __init__(self, name, symbols):
        super().__init__(name, symbols, 'miniboss')
