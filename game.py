# game.py: execute commands based on the input

from input import get_input

class Enemy:
    def __init__(self):
        '''
        Constructor
        '''
        self.cards = ['sword', 'shield', 'bow']
    
    def matches(self, card: str):
        '''
        Return true if card matches one of my cards
        Return false if none of the cards match
        '''

        match = None

        # Take a field off the enemy
        # When we play that card
        for enemy_card in self.cards:
            if card == enemy_card:
                match = enemy_card # marking card for removal

        if match != None:
            return True
        else:
            return False

    def attack(self, card):    
        '''
        Test for a match and remove it from the
        enemy's health if it's a match
        '''

        if self.matches(card):
            self.cards.remove(card)
        else:
            print('No match')
            
    def __str__(self):
        '''
        Return a list of the enemy's cards
        '''

        return 'Enemy HP:' + str(self.cards)

    def is_dead(self):
        '''
        Return true if the Enemy is dead
        '''
        return len(self.cards) == 0

enemy = Enemy()

# Main game loop
while True:

    # Print enemy HP
    print(enemy)

    # Get input
    operation, args = get_input()

    if operation == 'play':
        # Attack with the card
        enemy.attack(args[0])
    elif operation == 'quit':
        break
    elif operation == '<3':
        print('3<')
    else:
        print('unrecognized command')

    # break out when the enemy is dead
    if enemy.is_dead():
        break

print('End of game!')
if enemy.is_dead():
    print('You won!')
