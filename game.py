# game.py: execute commands based on the input

from input import get_input
from door_card import DoorCard
from door_deck import DoorDeck
from hero import Hero
import hero_cards

door_deck = DoorDeck(5)

# TODO: Add support for multiple Heroes. Each player will have one Hero.
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
    if not hero_cards.is_valid(card):
        print("That's not an action!\n")
        return

    # Check if the card is available to the hero
    if not hero.has_card(card):
        print("You don't have that card!\n")
        return

    # Try to attack with the card
    # We'll probably move this into the card module
    # so that it's easier to implement other special card effects.
    if door_deck.current_enemy.try_attack(card):
        hero.discard(card)
        print("You hit the enemy with your", card + "!\n")
    else:
        print("That card has no effect on this enemy!")
        return

    # Clean up the enemy if they're dead
    if door_deck.current_enemy.is_dead():
        print("You killed the enemy!")
        if door_deck.try_draw():
            print("Drawing the next one")
        else:
            print("All enemies dead")


# Main game loop
while True:

    # Print enemy HP
    # TODO Issue #7: This will be removed and replaced with the print command.
    print(hero)
    print(door_deck.current_enemy)

    # Get input
    operation, args = get_input()

    # Decide what operation to do
    if operation == 'play':
        play_card(args[0])
    elif operation == 'discard':
        hero.discard(args[0])
    elif operation == 'draw':
        hero.draw_card()
        print('You drew a %s.' % hero.hero_hand[-1])
        print('Your deck has %d cards left.' % len(hero.hero_deck))
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
    if door_deck.current_enemy.is_dead():
        if door_deck.try_draw():
            print('Drew another fearsome enemy. Grr!')
        else:
            break

print('End of game!')
if len(door_deck.enemy_deck) == 0:
    print('You won!')
