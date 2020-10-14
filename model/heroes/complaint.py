
from model.serialization.stringable import Stringable


class Complaint(Exception, Stringable):
    '''
    A Complaint should be raised when we try to invalidate the game state.
    '''

    def __init__(self, msg):
        super().__init__(str(msg))
        self.msg = msg
