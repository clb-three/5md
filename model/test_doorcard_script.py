
from . import test_mocks as mock
from .console_notifier import ConsoleNotifier
from .doorcards.event import Event
from .doorcards.scripts import all_heroes_discard_one
from .gamestate import GameState


def test_all_heroes_discard_one():
    heroes = mock.gen_mock_heroes(10)
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    game = GameState(ConsoleNotifier(), heroes=heroes)

    all_heroes_discard_one(game)

    for _, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1


def test_event_all_heroes_discard_one():
    heroes = mock.gen_mock_heroes(10)
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]

    ouch = Event('ouchie', all_heroes_discard_one.__name__)

    ctx = GameState(ConsoleNotifier(), heroes=heroes)

    ouch.do_script(ctx)

    for _, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1
