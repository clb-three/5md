
class Game:
    '''
    A Game is a boss mat, door deck, and a set of heroes
    '''

    def __init__(self, heroes, door_deck, boss):
        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss

        self.heroes = heroes
        self.door_deck = door_deck
        self.boss = boss
        self.target = self.door_deck.current_enemy

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
        Play a card against the current enemy
        '''

        # Check if the card is available to the hero
        if not hero.has_card(card):
            print(f"{hero.name} doesn't have that card!\n")
            return

        hero.discard(card)

        self.target.attack(card)
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

        if not self.target.script:
            return

        # Else run the script

    def is_defeated(self):
        return self.target == self.boss and self.boss.is_dead()
