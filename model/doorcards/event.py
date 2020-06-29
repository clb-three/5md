from copy import deepcopy

from .private.base import BaseDoorCard
from .types import DoorCardTypes

# TODO: Make functionality for Event cards. It'll probably be a class that goes in the door deck.
# When you flip over an Event, your team must immediately do whatever the card says.
# Only the Action Card CANCEL and HOLY HAND GRENADE can prevent your party from doing the Event.


class Event(BaseDoorCard):
    '''
    Event will do something bad to the players!
    '''

    def __init__(self, name, script):
        super().__init__([], DoorCardTypes.event)
        self.name = name
        self.do_script = script

    def is_dead(self):
        '''
        Always consider this card "dead", since it gets
        burned up and cycled.
        '''

        return True

    def __dict__(self):
        selfobj = super().__dict__()
        selfobj['name'] = self.name

        return selfobj

    def deepcopy(self):
        return Event(deepcopy(self.name), self.do_script)
