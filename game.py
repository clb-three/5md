# game.py: execute commands based on the input

from input import get_input
from enemy import Enemy
from hero import Hero

# The enemy we're fighting
# TODO Issue #4: Support multiple enemies

enemy = Enemy()
hero = Hero()

def play_card(card):
    '''
    Play a card against the current enemy
    '''

    # Forces card into lower case string to prevent capitalization issues with input
    card = card.lower()

    # if card is valid, allow play
    if card == "sword" or card == "shield" or card == "arrow" or card == "jump" or card == "scroll":
        # checks if the card is available to the hero
        if hero.has_card(card):
            # Attack with the card
            enemy.attack(card) # TODO Issue #9 Check that the enemy actually can be hit by the card (if enemy doesn't have jump dont remove jump from hero)
            hero.discard(card) #temporary fix until hero class is fully implemented, removes card from heros hand
            print("You hit the enemy with your", card + "!\n")
        else:
            print("You don't have that card!\n")
    else:
        print("That's not an action!\n")






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
