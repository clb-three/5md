# game.py: execute commands based on the input

from input import get_input
from enemy import Enemy

# The enemy we're fighting
# TODO: Support multiple enemies
enemy = Enemy()

# Main game loop
while True:

    # Print enemy HP
    print(enemy)

    # Get input
    operation, args = get_input()

    # Decide what operation to do
    if operation == 'play':
        # Rename args[0] to attack for simplicity
        attack = args[0]

        # TODO: Check that:
        # 1. the attack is a valid card
        # 2. the attack is one of the cards in our hand

        # Attack with the card
        enemy.attack(attack)
    elif operation == 'quit':
        # Quit the game
        break
    elif operation == '<3':
        # Love on u
        print('3<')
    else:
        # Catch any command that we don't know
        # and let the user know about it
        print('unrecognized command')

    # break out when the enemy is dead
    if enemy.is_dead():
        break

print('End of game!')
if enemy.is_dead():
    print('You won!')
