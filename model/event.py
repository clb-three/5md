from .doorcard import DoorCard, DoorCardTypes
from .doorcard_scripts import scripts

# TODO: Make functionality for Event cards. It'll probably be a class that goes in the door deck.
# When you flip over an Event, your team must immediately do whatever the card says.
# Only the Action Card CANCEL and HOLY HAND GRENADE can prevent your party from doing the Event.


class Event(DoorCard):
    '''
    Event will do something bad to the players!
    '''

    def __init__(self, name, script_name=None):
        self.name = name
        super().__init__([], DoorCardTypes.event)
        if script_name not in scripts:
            raise Exception(f'Script "{script_name}" not found.')
        self.run_script = scripts[script_name]

    def is_dead(self):
        '''
        Always consider this card "dead", since it gets
        burned up and cycled.
        '''

        return True

    def is_dead(self):
        '''
        Always consider this card "dead", since it gets
        burned up and cycled.
        '''

        return True

    def __str__(self):
        return f'Event: {self.name}'
