from model.serialization.stringable import Stringable


class Message(Stringable):
    def __init__(self, verb, obj=None):
        self.code = verb
        self.obj = None
