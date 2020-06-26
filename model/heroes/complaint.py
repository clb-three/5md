

class Complaint(Exception):
    '''
    A Complaint should be raised when we try to invalidate the game state.
    '''

    def __init__(self, msg):
        super().__init__(msg)
