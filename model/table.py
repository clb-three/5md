from .heroes.complaint import Complaint
from .heroes import factory as hero_factory


class Table:
    '''
    A Table takes care of the logic for high-level interaction
    between parts of the game.
    '''

    def __init__(self, game):
        self.game_over = False
        self.last_command = None
        self.gamestate = game

    def process_hero_command(self, hero, args):
        '''
        Process a command specific to a hero.
        '''

        try:
            if args[0] == 'play':
                # Forces card into a lower case string to prevent capitalization issues with input
                card_name = args[1].lower()
                card = hero_factory.get_card(card_name)
                self.gamestate.play_card(hero, card)
            elif args[0] == 'discard':

                hero.discard(args[1])
            elif args[0] == 'draw':
                card_drawn = hero.draw_card()

                self.gamestate.notifier.info(
                    f'drawcard {hero.name} {card_drawn}')
                self.gamestate.notifier.info(
                    f'cardsleft {hero.name} {len(hero.deck)}')
        except Complaint as c:
            self.gamestate.notifier.error(str(c))
            return

    def process_command(self, command):
        '''
        Process a command from the user.
        '''

        # Get input
        args = command.split(' ')

        # Do input
        if args[0] in self.gamestate.heroes:
            hero = self.gamestate.heroes[args[0]]
            self.process_hero_command(hero, args[1:])
        elif args[0] == 'quit':
            # Quit the game
            self.game_over = True
        elif args[0] == 'nuke':
            # Kill the current enemy
            self.gamestate.target.kill()
        elif args[0] == '':
            # Repeat the last command
            if not self.last_command:
                self.gamestate.notifier.log('Error: no previous command.')
            else:
                self.gamestate.notifier.log(f'Redoing "{self.last_command}"')
                self.process_command(self.last_command)
                return
        elif args[0] == '<3':
            # Love on u
            self.gamestate.notifier.send('3<')
        elif args[0] == 'getstate':
            self.gamestate.notifier.info(self.gamestate)
        else:
            # Catch any command that we don't know
            # and let the user know about it
            self.gamestate.notifier.error('invalidcommand')

        # save the last command we've done
        if command != '':
            self.last_command = command

        # Trigger "on draw" effect
        # self.gamestate.do_target_script()

        # Switch out target when they're dead
        self.gamestate.bring_out_yer_dead()

        # break out when all enemies isded
        if self.gamestate.is_defeated():
            self.gamestate.notifier.info('won')
            self.game_over = True
