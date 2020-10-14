import json

from .dictable import Dictable


class ComplexEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Dictable):
            return dict(o)
        else:
            return self.default(o)
