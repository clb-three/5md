import json

from .complex_encoder import ComplexEncoder
from .dictable import Dictable


class Stringable(Dictable):

    def __str__(self):
        '''
            Return a list of the enemy's symbols
            '''

        return json.dumps(dict(self), indent=4, cls=ComplexEncoder, separators=(',', ':'))

    def __repr__(self):
        return str(self)
