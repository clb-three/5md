
from attackable import Attackable


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
                print('You killed the boss!')
            elif self.door_deck.try_draw():
                print('Drew another fearsome enemy. Grr!')
                self.target = self.door_deck.current_enemy
            else:
                print('Now we\'re fighting the boss. Ahh!')
                self.target = self.boss
                self.fighting_boss = True

        return success
