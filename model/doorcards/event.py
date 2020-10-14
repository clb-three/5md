from copy import deepcopy

from .private.base import BaseDoorCard
from .types import DoorCardTypes

# When you flip over an Event, your team must immediately (after opportunity to cancel) do whatever the card says.
# Only the Action Card CANCEL and HOLY HAND GRENADE can prevent your party from doing the Event.


class Event(BaseDoorCard):
    '''
    Event will do something bad to the players!
    '''

    def __init__(self, name, script):
        super().__init__([], DoorCardTypes.event)
        self.name = name
        self.script = script
        self.done = False

    def kill(self):
        self.done = True

    def do_script(self, ctx):
        if not self.done:
            self.script(ctx)
            self.kill()

    def is_dead(self):
        '''
        Always consider this card "dead", since it gets
        burned up and cycled.
        '''

        return self.done

    def deepcopy(self):
        return Event(deepcopy(self.name), self.do_script)
