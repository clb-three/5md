import hero_cards


class Table:
    '''
    A Table takes care of the logic for high-level interaction
    between parts of the game.
    '''

    def __init__(self, game):
        self.game_over = False
        self.last_command = ''
        self.game = game

    def display_status(self):
        print(self.game)

    def process_hero_command(self, hero, args):
        '''
        Process a command specific to a hero.
        '''

        if args[0] == 'play':
            # Forces card into a lower case string to prevent capitalization issues with input
            card_name = args[1].lower()

            card = hero_cards.get(card_name)

            # If card is not valid, don't let it be played
            if not card:
                print("That's not a valid card name!\n")
                return

            self.game.play_card(hero, card)
        elif args[0] == 'discard':
            hero.discard(args[1])
        elif args[0] == 'draw':
            card_drawn = hero.draw_card()
            print(f'{hero.name} drew a %s.' % card_drawn)
            print(f'{hero.name}\'s deck has {len(hero.deck)} cards left.')

    def process_command(self, command):
        '''
        Process a command from the user.
        '''

        # Get input
        args = command.split(' ')

        # save the last command we've done
        if command != '':
            self.last_command = command

        # Do input
        if args[0] in self.game.heroes:
            hero = self.game.heroes[args[0]]
            self.process_hero_command(hero, args[1:])
        elif args[0] == 'print':
            # TODO Issue #7: Print the current enemy's deets. We'll want this to replace the printing
            # the status up in the top of the loop.
            print('Not implemented yet')
        elif args[0] == 'quit':
            # Quit the game
            self.game_over = True
        elif args[0] == 'nuke':
            # Kill the current enemy
            self.game.target.kill()
        elif args[0] == '':
            # Repeat the last command
            if self.last_command == '':
                print('No previous command.')
            else:
                print(f'Redo "{command}"')
                self.process_command(self.last_command)
        elif args[0] == '<3':
            # Love on u
            print('3<')
        else:
            # Catch any command that we don't know
            # and let the user know about it
            print('Unrecognized command')

        # Switch out target when they're dead
        self.game.bring_out_yer_dead()

        # Trigger "on draw" effect
        self.game.do_target_script()

        # break out when all enemies isded
        if self.game.is_defeated():
            print('You won!')
            self.game_over = True
