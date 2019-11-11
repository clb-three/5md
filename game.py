# game.py: execute commands based on the input

from input import get_input
from enemy import Enemy

# The enemy we're fighting
# TODO Issue #4: Support multiple enemies
enemy = Enemy()

def play_card(card):
    '''
    Play a card against the current enemy
    '''

    # TODO: Check that the attack is a valid card

    # TODO Issue #5: Check that the attack is one of the cards in our hand

    # Attack with the card
    enemy.attack(card)

# Main game loop
while True:

    # Print enemy HP
    # TODO Issue #7: This will be removed and replaced with the print command.
    print(enemy)

    # Get input
    operation, args = get_input()

    # Decide what operation to do
    if operation == 'play':
        play_card(args[0])
    elif operation == 'print':
        # TODO Issue #7: Print the current enemy's deets. We'll want this to replace the printing
        # the status up in the top of the loop.
        print('Not implemented yet')
    elif operation == 'quit':
        # Quit the game
        break
    elif operation == '<3':
        # Love on u
        print('3<')
    else:
        # Catch any command that we don't know
        # and let the user know about it
        print('Unrecognized command')

    # break out when the enemy is dead
    if enemy.is_dead():
        break

print('End of game!')
if enemy.is_dead():
    print('You won!')
