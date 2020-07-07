
from model.message import Message

from .heroes import factory as hero_factory
from .heroes.complaint import Complaint


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
                card = args[1].lower()
                return self.gamestate.play_card(hero, card)
            elif args[0] == 'discard':
                card = args[1].lower()
                hero.discard(card)

                return Message('discard', [hero.name, card])
            elif args[0] == 'draw':
                card_drawn = hero.draw_card()

                return [Message('drawcard', [hero.name, card_drawn]), Message('cardsleft', len(hero.deck))]
        except Complaint as complaint:
            return complaint.msg

    def do_command(self, command):

        # Get input
        args = command.split(' ')

        # save the last command we've done
        if command != '':
            self.last_command = command

        # Do input
        if args[0] in self.gamestate.heroes:
            hero = self.gamestate.heroes[args[0]]
            return self.process_hero_command(hero, args[1:])
        elif args[0] == 'quit':
            # Quit the game
            self.game_over = True
            return Message('quit')
        elif args[0] == 'nuke':
            # Kill the current enemy
            self.gamestate.target.kill()
            return self.gamestate.update_target()
        elif args[0] == '':
            # Repeat the last command
            if not self.last_command:
                return Message('log', 'no previous command')
            else:
                msg = self.process_command(self.last_command)
                return [
                    Message('log', f'redoing "{self.last_command}"'), msg]
        elif args[0] == '<3':
            # Love on u
            return Message('<3')
        elif args[0] == 'getstate':
            return Message('state', self.gamestate)
        else:
            # Catch any command that we don't know
            # and let the user know about it
            return Message('error', 'invalidcommand')

    def process_command(self, command):
        '''
        Process a command from the user.
        '''

        message = self.do_command(command)

        # break out when all enemies isded
        if self.gamestate.is_defeated():
            self.game_over = True
            return [message, Message('state', 'won')]

        if not isinstance(message, list):
            message = [message]

        return message
