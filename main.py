# game.py: execute commands based on the input

import hero_cards
from boss import Boss
from enemy import Enemy
from doordeck_factory import DoorDeckFactory
from hero import Hero
from table import Table
from game import Game
from user_input import get_command
from symbols import Symbols
from script import DoorDeckContext

# Each player will have one Hero.
heroes = {
    'benji': Hero('benji', 'barbarian'),
    'austin': Hero('austin', 'healer'),
}

# Draws the hero's initial hand
for j in range(0, 5):
    for h in heroes.values():
        h.draw_card()

# Deal boss mat and door deck
boss = Boss([Symbols.arrow, Symbols.jump], 20)
dd_ctx = DoorDeckContext(heroes)
dd_factory = DoorDeckFactory(dd_ctx)
dd = dd_factory.deal(boss.num_door_cards, len(heroes) * 2)

game = Game(heroes, dd, boss)
table = Table(game)
while not table.game_over:
    table.display_status()
    command = get_command()
    table.process_command(command)
