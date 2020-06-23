

class GameState:
    '''
    A set of boss mat, door deck, target, and a set of heroes
    '''

    def __init__(self, heroes=None, door_deck=None, target=None, boss=None):
        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss

        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss
        self.target = target

    def __str__(self):
        '''
        Print current target's HP
        '''

        return f'''
    {self.heroes.values()}
    {self.target}
'''

    def play_card(self, hero, card):
        '''
        Play the given card against the current enemy
        '''

        # If card is not valid, don't let it be played
        if not card:
            print("That's not a valid card name!\n")
            return

        # Check if the card is available to the hero
        if not hero.has_card(card):
            print(f"{hero.name} doesn't have that card!\n")
            return

        # Play the card
        hero.discard(card)
        card.play(self)
        print(f"{hero.name} played {card}!\n")

    def bring_out_yer_dead(self):
        '''
        Switch to next enemy or boss when all enemies are dead
        '''

        if self.target.is_dead():
            if self.target == self.boss:
                print(f'Killed the boss!')
                return

            if self.door_deck.try_draw():
                print(f'Defeated a fearsome enemy. Grr!')
                self.target = self.door_deck.current_enemy
            else:
                print('Now we\'re fighting the boss. Ahh!')
                self.target = self.boss
                return

    def do_target_script(self):
        '''
        Run this card's script on the model.
        '''

        if not self.target.do_script:
            return

        # Else run the script
        print('Running target script')
        self.target.do_script(self)

    def is_defeated(self):
        return self.target == self.boss and self.boss.is_dead()

    def __str__(self):
        return f'''Heroes: {', '.join([str(h) for h in self.heroes.values()])}
Target: {{{self.target}}}
Boss: {self.boss}
Cards left: {len(self.door_deck.deck)}'''
