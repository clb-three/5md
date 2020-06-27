import random


def all_heroes_discard_one(ctx):
    '''Make all heroes discard one card'''
    for hero_name in ctx.heroes:
        ctx.heroes[hero_name].hand.remove(
            random.choice(ctx.heroes[hero_name].hand))


script_funcs = [all_heroes_discard_one]
scripts = {f.__name__: f for f in script_funcs}
