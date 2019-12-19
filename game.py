# game.py: execute commands based on the input

from input import get_input
from enemy import Enemy
from hero import Hero
import cards

# The enemy we're fighting
# TODO Issue #4: Support multiple enemies

enemy = Enemy()
hero = Hero()
# Draws the hero's initial hand
for j in range(0, 5):
    hero.draw_card()

def play_card(card):
    '''
    Play a card against the current enemy
    '''


    # Forces card into a lower case string to prevent capitalization issues with input
    card = card.lower()

    # If card is not valid, don't let it be played
    if not cards.is_valid(card):
        print("That's not an action!\n")
        return

    # Check if the card is available to the hero
    if not hero.has_card(card):
        print("You don't have that card!\n")
        
    # Try to ttack with the card
    if enemy.try_attack(card):
        hero.discard(card)
        print("You hit the enemy with your", card + "!\n")
    else:
        print("The enemy doesn't have that card!")





# Main game loop
while True:

    # Print enemy HP
    # TODO Issue #7: This will be removed and replaced with the print command.
    print(hero)
    print(enemy)

    # Get input
    operation, args = get_input()

    # Decide what operation to do
    if operation == 'play':
        play_card(args[0])
    elif operation == 'discard':
        hero.discard(args[0])
    elif operation == 'draw':
        hero.draw_card()
        print('You drew ' + hero.hero_hand[-1] + '\n')
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
