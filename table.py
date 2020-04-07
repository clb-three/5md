

class Table:
    '''
    A Table takes care of the logic for high-level interaction
    between parts of the game.
    '''

    def __init__(self, heroes, door_deck, boss):
        self.heroes = heroes

        self.game_over = False

        self.door_deck = door_deck
        self.boss = boss
        self.target = self.door_deck.current_enemy

    def display_status(self):
        # Print enemy HP
        # TODO Issue #7: This will be removed and replaced with the print command.
        print(list(self.heroes.values()))
        print(self.target)

    def play_card(self, hero, card):
        '''
        Play a card against the current enemy
        '''

        # Check if the card is available to the hero
        if not hero.has_card(card):
            print(f"{hero.name} doesn't have that card!\n")
            return

        hero.discard(card)

        self.target.attack(card)
        print(f"{hero.name} played {card}!\n")

        # switch to next enemy or boss when all enemies are dead
        if self.target.is_dead():
            if self.target == self.boss:
                print(f'{hero.name} killed the boss!')
                return

            if self.door_deck.try_draw():
                print(f'{hero.name} defeated a fearsome enemy. Grr!')
                self.target = self.door_deck.current_enemy
                return
            else:
                print('Now we\'re fighting the boss. Ahh!')
                self.target = self.boss
                return

    def process_hero_command(self, hero, args):
        '''
        Process a command specific to a hero.
        '''

        if args[0] == 'play':
            # Forces card into a lower case string to prevent capitalization issues with input
            card = args[1].lower()

            # If card is not valid, don't let it be played
            if not hero_cards.is_valid(card):
                print("That's not an action!\n")
                return

            self.play_card(hero, card)
        elif args[0] == 'discard':
            hero.discard(args[1])
        elif args[0] == 'draw':
            card_drawn = hero.draw_card()
            print(f'{hero.name} drew a %s.' % card_drawn)
            print(f'{hero.name}\'s deck has {len(hero.hero_deck)} cards left.')

    def process_command(self, command):
        '''
        Process a command from the user.
        '''

        # Get input
        args = command.split(' ')

        # Do input
        if args[0] in heroes:
            hero = heroes[args[0]]
            self.process_hero_command(hero, args[1:])
        elif args[0] == 'print':
            # TODO Issue #7: Print the current enemy's deets. We'll want this to replace the printing
            # the status up in the top of the loop.
            print('Not implemented yet')
        elif args[0] == 'quit':
            # Quit the game
            self.game_over = True
        elif args[0] == '<3':
            # Love on u
            print('3<')
        else:
            # Catch any command that we don't know
            # and let the user know about it
            print('Unrecognized command')

        # break out when all enemies isded
        if self.target == self.boss and self.boss.is_dead():
            print('You won!')
            self.game_over = True
