from enum import Enum, auto, unique


@unique
class Symbol(Enum):
    '''
    Enumerations for all symbols
    '''

    sword = auto()
    shield = auto()
    arrow = auto()
    jump = auto()
    scroll = auto()

    @classmethod
    def convert(cls, symbol_name):
        '''
        Convert a symbol name to an enum and return it
        or return None if it didn't work.
        '''
        return next((v for k, v in cls.__members__.items() if k == symbol_name), None)

    def __str__(self):
        return str(self.name)
