# game.py: execute commands based on the input

from input import get_input
from door_card import DoorCard
from boss_mat import BossMat, PlayResult
from door_deck_factory import DoorDeckFactory
from hero import Hero
import hero_cards


class Table:

    def __init__(self, heroes, mat):
        self.heroes = heroes
        self.mat = mat

        self.game_over = False

    def play_card(self, hero, card):
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
            print(f"{hero.name} doesn't have that card!\n")
            return

        result = self.mat.play(card)
        if result == PlayResult.SuccessfulAttack:
            print(f"{hero.name} hit the enemy with your {card}!\n")
        elif result == PlayResult.FailedAttack:
            print("That card has no effect on this enemy!")
        elif result == PlayResult.DefeatedEnemy:
            print(f'{hero.name} defeated a fearsome enemy. Grr!')
        elif result == PlayResult.DefeatedDoorDeck:
            print('Now we\'re fighting the boss. Ahh!')
        elif result == PlayResult.DefeatedBoss:
            print(f'{hero.name} killed the boss!')

        hero.discard(card)

    def play_turn(self):
        # Print enemy HP
        # TODO Issue #7: This will be removed and replaced with the print command.
        print(list(heroes.values()))
        print(mat.target)

        # Get input
        args = get_input()

        # Do input
        if args[0] in heroes:
            hero = heroes[args[0]]

            if args[1] == 'play':
                self.play_card(hero, args[2])
            elif args[1] == 'discard':
                hero.discard(args[2])
            elif args[1] == 'draw':
                card_drawn = hero.draw_card()
                print(f'{hero.name} drew a %s.' % card_drawn)
                print(
                    f'{hero.name}\'s deck has {len(hero.hero_deck)} cards left.')
        elif args[0] == 'print':
            # TODO Issue #7: Print the current enemy's deets. We'll want this to replace the printing
            # the status up in the top of the loop.
            print('Not implemented yet')
        elif args[0] == 'quit':
            # Quit the game
            self.game_over = True
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
            self.game_over = True


door_deck_factory = DoorDeckFactory()
mat = BossMat(door_deck_factory, 1, ['arrow', 'jump'])

# Each player will have one Hero.
heroes = {
    'benji': Hero('benji'),
    'austin': Hero('austin'),
}

# Draws the hero's initial hand
for j in range(0, 5):
    for h in heroes.values():
        h.draw_card()

table = Table(heroes, mat)
while not table.game_over:
    table.play_turn()
