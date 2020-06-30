import random


def all_heroes_discard_one(ctx):
    '''Make all heroes discard one card'''
    for _, hero in ctx.heroes.items():
        if len(hero.hand) > 0:
            choice = random.choice(hero.hand)
            hero.discard(choice)


script_funcs = [all_heroes_discard_one]
scripts = {f.__name__: f for f in script_funcs}
