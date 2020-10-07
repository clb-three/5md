import random


def all_heroes_discard_one(ctx):
    """Make all heroes discard one card"""
    for hero in ctx.heroes:
        if len(hero.hand) > 0:
            choice = random.choice(hero.hand)
            hero.discard(choice)


def all_heroes_discard_n(ctx, n):
    """Make all heroes discard n cards"""
    for _ in range(n):
        all_heroes_discard_one(ctx)


def all_heroes_discard_all(ctx):
    """Make all heroes discard all cards"""
    while any(len(hero.hand) > 0 for hero in ctx.heroes):
        all_heroes_discard_one(ctx)


script_funcs = [all_heroes_discard_one]
scripts = {f.__name__: f for f in script_funcs}
