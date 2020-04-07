# game.py: execute commands based on the input

from input import get_input
from door_card import DoorCard
from boss_mat import BossMat, PlayResult
from door_deck_factory import DoorDeckFactory
from hero import Hero
import hero_cards


def play_card(hero, card, mat):
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

    result = mat.play(card)
    if result == PlayResult.SuccessfulAttack:
        print("You hit the enemy with your", card + "!\n")
    elif result == PlayResult.FailedAttack:
        print("That card has no effect on this enemy!")
    elif result == PlayResult.DefeatedEnemy:
        print('Defeated a fearsome enemy. Grr!')
    elif result == PlayResult.DefeatedDoorDeck:
        print('Now we\'re fighting the boss. Ahh!')
    elif result == PlayResult.DefeatedBoss:
        print('You killed the boss!')

    hero.discard(card)


def main_loop(heroes, mat):
    while True:
        # Print enemy HP
        # TODO Issue #7: This will be removed and replaced with the print command.
        print(heroes)
        print(mat.target)

        # Get input
        args = get_input()

        # Do input
        if args[0] in heroes:
            hero = heroes[args[0]]

            if args[1] == 'play':
                play_card(hero, args[2], mat)
            elif args[1] == 'discard':
                hero.discard(args[2])
            elif args[1] == 'draw':
                card_drawn = hero.draw_card()
                print('You drew a %s.' % card_drawn)
                print('Your deck has %d cards left.' % len(hero.hero_deck))
        elif args[0] == 'print':
            # TODO Issue #7: Print the current enemy's deets. We'll want this to replace the printing
            # the status up in the top of the loop.
            print('Not implemented yet')
        elif args[0] == 'quit':
            # Quit the game
            break
        elif args[0] == '<3':
            # Love on u
            print('3<')
        else:
            # Catch any command that we don't know
            # and let the user know about it
            print('Unrecognized command')

        # break out when all enemies isded
        if mat.is_defeated():
            print('You won!')
            break


door_deck_factory = DoorDeckFactory()
mat = BossMat(door_deck_factory, 1, ['arrow', 'jump'])

# Each player will have one Hero.
heroes = {
    "benji": Hero(),
    "austin": Hero(),
}

# Draws the hero's initial hand
for j in range(0, 5):
    for h in heroes.values():
        h.draw_card()

main_loop(heroes, mat)
