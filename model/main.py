
from .doorcards import factory as doorcard_factory
from .gamestate import GameState
from .heroes import factory as hero_factory
from .table import Table

if __name__ == '__main__':

    heroes = {
        'benji': hero_factory.hero('benji', 'barbarian'),
        'austin': hero_factory.hero('austin', 'healer'),
    }
    # Draws the hero's initial hand
    for _ in range(0, 5):
        for hero in heroes.values():
            hero.draw_card()

    # Deal boss mat and door deck
    boss = doorcard_factory.create_boss()
    doordeck = doorcard_factory.deal_deck(
        boss.num_door_cards, len(heroes))

    game = GameState(heroes, doordeck,
                     doordeck.current_enemy, boss)
    table = Table(game)

    while not table.game_over:
        command = input('Enter a command $>')
        message = table.process_command(command)
        print(str(message))
