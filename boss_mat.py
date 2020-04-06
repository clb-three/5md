
class Boss:
    def __init__(self, symbols):
        self.symbols = symbols

    def is_dead(self):
        return len(self.symbols) == 0

    def try_attack(self, card):
        if card in self.symbols:
            self.symbols.remove(card)
            return True
        else:
            return False


class BossMat:
    '''
    A boss mat has a deck of door cards,
    with a powerful boss on the bottom.
    '''

    def __init__(self, factory, num_cards, symbols):
        self.door_deck = factory.create(num_cards)
        self.target = self.door_deck.current_enemy

        self.boss = Boss(symbols)

    def is_dead(self):
        return self.target.is_dead()

    def play(self, card):
        # Try to attack with the card
        # We'll probably move this into the card module
        # so that it's easier to implement other special card effects.
        if self.target.try_attack(card):
            print("You hit the enemy with your", card + "!\n")
        else:
            print("That card has no effect on this enemy!")

        # break out when the enemy is dead
        if self.target.is_dead():
            if self.door_deck.try_draw():
                self.target = self.door_deck.current_enemy
                print('Drew another fearsome enemy. Grr!')
            elif self.boss.is_dead() is not True:
                self.target = self.boss
