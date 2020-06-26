# gameloop.py: execute commands based on the input

from .doorcards import factory as doorcard_factory
from .heroes import factory as hero_factory
from .table import Table
from .gamestate import GameState
from .user_input import get_command
from .console_notifier import ConsoleNotifier


class GameLoop():
    '''
    Performs the main loop of the game, and references the resources it needs.
    '''

    def __init__(self, notifier):
        # Each player will have one Hero.
        self.heroes = {
            'benji': hero_factory.hero('benji', 'barbarian'),
            'austin': hero_factory.hero('austin', 'healer'),
        }
        # Draws the hero's initial hand
        for j in range(0, 5):
            for h in self.heroes.values():
                h.draw_card()

        # Deal boss mat and door deck
        self.boss = doorcard_factory.create_boss()
        self.doordeck = doorcard_factory.deal_deck(
            self.boss.num_door_cards, len(self.heroes))

        game = GameState(notifier, self.heroes, self.doordeck,
                         self.doordeck.current_enemy, self.boss)
        game.bring_out_yer_dead()
        self.table = Table(game)

    def loop(self, command_getter):
        while not self.table.game_over:
            command = command_getter()
            self.table.process_command(command)


if __name__ == '__main__':
    console_notifier = ConsoleNotifier()

    gp = GameLoop(console_notifier)
    gp.loop(get_command)
