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

# Each player will have one Hero.
heroes = {
    'benji': Hero('benji'),
    'austin': Hero('austin'),
}

# Draws the hero's initial hand
for j in range(0, 5):
    for h in heroes.values():
        h.draw_card()

# Deal boss mat and door deck
boss = Boss([Symbols.arrow, Symbols.jump], 20)
door_deck_factory = DoorDeckFactory()
door_deck = door_deck_factory.deal(boss.num_door_cards, len(heroes) * 2)

game = Game(heroes, door_deck, boss)
table = Table(game)
while not table.game_over:
    table.display_status()
    command = get_command()
    table.process_command(command)
