from enum import Enum, auto


class Symbols(Enum):
    '''
    Enumerations for all symbols
    '''

    sword = auto()
    shield = auto()
    arrow = auto()
    jump = auto()
    scroll = auto()

    def convert(self, symbol_name):
        '''
        Convert a symbol name to an enum and return it
        or return None if it didn't work.
        '''
        return next(v for k, v in self.__members__ if k == symbol_name, None)
