from . import test_mocks as mock
from .doorcards.event import Event
from .doorcards.scripts import all_heroes_discard_one
from .gamestate import GameState


def test_all_heroes_discard_one():
    heroes = mock.gen_mock_heroes(10)
    for hero in heroes:
        hero.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes]
    game = GameState(heroes=heroes)

    all_heroes_discard_one(game)

    for _, hero in enumerate(heroes):
        assert len(hero.hand) == deck_sizes[1] - 1


def test_event_all_heroes_discard_one():
    heroes = mock.gen_mock_heroes(10)
    for hero in heroes:
        hero.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes]

    ouch = Event('ouchie', all_heroes_discard_one)

    ctx = GameState(heroes=heroes)

    ouch.do_script(ctx)

    for _, hero in enumerate(heroes):
        assert len(hero.hand) == deck_sizes[1] - 1
