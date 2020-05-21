from enum import Enum, auto, unique


@unique
class Symbols(Enum):
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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, Symbols):
            return self.name < other.name
