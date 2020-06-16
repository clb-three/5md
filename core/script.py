import random


class DoorDeckContext():
    '''
    A Context is a set of references to game objects for a script to interact with.
    '''

    def __init__(self, heroes):
        self.heroes = heroes

    def all_heroes_discard_one(self):
        for hero_name in self.heroes:
            self.heroes[hero_name].hand.remove(
                random.choice(self.heroes[hero_name].hand))
