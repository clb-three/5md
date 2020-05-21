
from script import DoorDeckContext
from enum import Enum, unique, auto
from hero_card_types import HeroCardTypes


@unique
class DoorCardTypes(Enum):
    boss = auto()
    monster = auto()
    event = auto()
    miniboss = auto()


class DoorCard:
    def __init__(self, symbols, card_type):
        self.symbols = symbols
        self.type = card_type
        self.run_script = None

    def init_script(self, ctx, script_name):
        '''
        Initialize script member with the given context
        '''
        self.run_script = getattr(ctx, script_name)

    def is_dead(self):
        '''
        Return True if the Enemy is dead
        '''

        return len(self.symbols) == 0

    def attack(self, card):
        '''
        Attack this enemy with the given card and return True if it's a success,
        else return False
        '''

        if card.card_type == HeroCardTypes.symbol:
            symbol = card
            if symbol in self.symbols:
                self.symbols.remove(symbol)
                return True

        return False

    def kill(self):
        '''
        kys
        '''

        del self.symbols[:]

    def __str__(self):
        '''
        Return a list of the enemy's symbols
        '''

        return f'type: {str(self.type)} HP: {str(self.symbols)}'
