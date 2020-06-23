
from .hero import Hero
from .doorcards.event import Event
from .test_utils import gen_mock_heroes
from .doorcards.scripts import all_heroes_discard_one
from .game import Game


def test_all_heroes_discard_one():
    heroes = gen_mock_heroes(10)
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    game = Game(heroes=heroes)

    all_heroes_discard_one(game)

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1


def test_event_all_heroes_discard_one():
    heroes = gen_mock_heroes(10)
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]

    ouch = Event('ouchie', all_heroes_discard_one.__name__)

    c = Game(heroes=heroes)

    ouch.do_script(c)

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1
