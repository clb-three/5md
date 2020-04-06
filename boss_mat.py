

import enum
from attackable import Attackable


class PlayResult(enum.Enum):
    SuccessfulAttack = 1
    FailedAttack = 2
    DefeatedDoorDeck = 3
    DefeatedEnemy = 4
    DefeatedBoss = 5


class Boss(Attackable):
    pass


class BossMat:
    '''
    A boss mat has a deck of door cards,
    with a powerful boss on the bottom.
    '''

    def __init__(self, factory, num_cards, symbols):
        self.door_deck = factory.create(num_cards)
        self.target = self.door_deck.current_enemy

        self.boss = Boss(symbols)

    def is_defeated(self):
        return self.target == self.boss and self.target.is_dead()

    def play(self, symbol):
        success = self.target.try_attack(symbol)

        # switch to next enemy or boss when all enemies are dead
        if self.target.is_dead():
            if self.target == self.boss:
                return PlayResult.DefeatedBoss

            if self.door_deck.try_draw():
                self.target = self.door_deck.current_enemy
                return PlayResult.DefeatedEnemy

            self.target = self.boss
            return PlayResult.DefeatedDoorDeck

        return PlayResult.SuccessfulAttack if success else PlayResult.FailedAttack
