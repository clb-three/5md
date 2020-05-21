from doorcard import DoorCard

# TODO: Make functionality for Event cards. It'll probably be a class that goes in the door deck.
# When you flip over an Event, your team must immediately do whatever the card says.
# Only the Action Card CANCEL and HOLY HAND GRENADE can prevent your party from doing the Event.


class Event(DoorCard):
    '''
    Event will do something bad to the players!
    '''

    def __init__(self, name, ctx=None, script_name=None):
        self.name = name
        super().__init__([], 'event')
        if ctx and script_name:
            self.init_script(ctx, script_name)

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
