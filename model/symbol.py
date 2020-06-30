from enum import Enum, unique


@unique
class Symbol(str, Enum):
    '''
    Enumerations for all symbols.
    Inherits from str so that it is serializable.
    '''

    sword = 'sword'
    shield = 'shield'
    arrow = 'arrow'
    jump = 'jump'
    scroll = 'scroll'

    @classmethod
    def convert(cls, symbol_name):
        '''
        Convert a symbol name to an enum and return it
        or return None if it didn't work.
        '''
        return next((v for k, v in dict(cls.__members__).items() if k == symbol_name), None)

    def __str__(self):
        return str(self.name)
