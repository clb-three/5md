# game.py: execute commands based on the input

from input import get_input
from enemy import Enemy

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
