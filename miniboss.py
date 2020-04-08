
from enemy import Enemy


class Miniboss(Enemy):
    '''
    Miniboss is a special case of an Enemy
    '''

    def __init__(self, name, symbols):
        super().__init__(name, symbols, 'miniboss')
