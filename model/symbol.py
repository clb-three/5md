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

    def play(self, ctx):
        '''
        Play this symbol against the target
        '''
        if self in ctx.target.symbols:
            ctx.target.symbols.remove(self)
        else:
            raise Exception(f'{self} not in ctx.target.symbols')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, Symbol):
            return self.name < other.name
