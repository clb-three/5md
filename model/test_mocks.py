import random

from coolname import generate_slug

from .doorcards.enemy import Enemy
from .heroes import factory as hero_factory


def hero(classname):
    """Create a Hero with a random name and the given class."""
    return hero_factory.hero(generate_slug(), classname)


def gen_mock_heroes(howmany):
    """Create many heroes with random names and classes."""
    classes = ['ranger', 'barbarian', 'mage']
    return [hero(random.choice(classes)) for _ in range(howmany)]


def enemy(*symbols):
    """Create an Enemy with a random name and the given symbols."""
    return Enemy(generate_slug(), list(symbols))
