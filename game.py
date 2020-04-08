# game.py: execute commands based on the input

import hero_cards
from boss import Boss
from enemy import Enemy
from doordeck_factory import DoorDeckFactory
from hero import Hero
from table import Table
from user_input import get_command
from symbols import Symbols

boss = Boss([Symbols.arrow, Symbols.jump], 1)
door_deck_factory = DoorDeckFactory()
door_deck = door_deck_factory.create(boss.num_door_cards)

# Each player will have one Hero.
heroes = {
    'benji': Hero('benji'),
    'austin': Hero('austin'),
}

# Draws the hero's initial hand
for j in range(0, 5):
    for h in heroes.values():
        h.draw_card()

table = Table(heroes, door_deck, boss)
while not table.game_over:
    table.display_status()
    command = get_command()
    table.process_command(command)
