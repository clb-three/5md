# game.py: execute commands based on the input

import hero_cards
from boss import Boss
from enemy import Enemy
from doordeck_factory import DoorDeckFactory
from hero import Hero
from table import Table
from game import Game
from user_input import get_command
from symbol import Symbol
from script import DoorDeckContext


class GameLoop():
    '''
    Performs the main loop of the game, and references the resources it needs.
    '''

    def __init__(self):
        # Each player will have one Hero.
        self.heroes = {
            'benji': Hero('benji', 'barbarian'),
            'austin': Hero('austin', 'healer'),
        }
        # Draws the hero's initial hand
        for j in range(0, 5):
            for h in self.heroes.values():
                h.draw_card()

        # Deal boss mat and door deck
        self.boss = Boss([Symbol.arrow, Symbol.jump], 20)
        dd_ctx = DoorDeckContext(self.heroes)
        dd_factory = DoorDeckFactory(dd_ctx)
        self.doordeck = dd_factory.deal(
            self.boss.num_door_cards, len(self.heroes) * 2)

        game = Game(self.heroes, self.doordeck, self.boss)
        self.table = Table(game)

    def loop(self, command_getter):
        while not self.table.game_over:
            self.table.display_status()
            command = command_getter()
            self.table.process_command(command)


if __name__ == '__main__':
    gp = GameLoop()
    gp.loop(get_command)
