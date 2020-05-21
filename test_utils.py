from coolname import generate_slug
from hero import Hero


def mock_hero():
    return Hero(generate_slug(), 'ranger')


def gen_mock_heroes(howmany):
    heroes = [mock_hero() for _ in range(howmany)]
    return {h.name: h for h in heroes}
