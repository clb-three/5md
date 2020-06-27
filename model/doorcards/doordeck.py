# A deck of door cards you must defeat


class DoorDeck:
    '''
    A DoorDeck is a closed system of door cards.
    Reveals the top door card to fight the players until we're out of cards.
    '''

    def __init__(self, cards):
        '''
        Create a new DoorDeck with the given cards.
        '''

        super().__init__()
        # Place an initial deck of 5 enemies
        self.deck = cards

    @property
    def current_enemy(self):
        return self.deck[0]

    def try_draw(self):
        '''
        Discard the current top card and draw the next one.
        '''

        if len(self.deck) > 0:
            self.deck.pop(0)
            return True
        else:
            return False

    def put_on_top(self, card):
        '''
        Put the given card on top.
        '''

        self.deck.insert(0, card)

    def __dict__(self):
        selfobj = {
            'deck': [c.__dict__() for c in self.deck],
            'top': self.current_enemy.__dict__()
        }
        return selfobj
