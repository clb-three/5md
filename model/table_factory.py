import mylog
from model.doorcards import factory as doorcard_factory
from model.gamestate import GameState
from model.heroes import factory as hero_factory
from model.table import Table


def get_table(emitter=print):
    """Get an instance of Table"""
    heroes = [
        hero_factory.hero('benji', 'barbarian'),
        hero_factory.hero('austin', 'healer'),
    ]
    # Draws the hero's initial hand
    for _ in range(0, 5):
        for hero in heroes:
            hero.draw_card()

    # Deal boss mat and door deck
    boss = doorcard_factory.create_boss()
    doordeck = doorcard_factory.deal_deck(boss.num_door_cards, len(heroes), boss)

    game = GameState(doordeck, heroes, logging=mylog)
    return Table(game, emitter, mylog)
