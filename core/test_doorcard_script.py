
from script import DoorDeckContext
from hero import Hero
from event import Event
from test_utils import gen_mock_heroes


def test_ado():
    heroes = gen_mock_heroes(10)
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    ctx = DoorDeckContext(heroes)

    ctx.all_heroes_discard_one()

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1


def test_event_ado():
    heroes = gen_mock_heroes(10)
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    ctx = DoorDeckContext(heroes)

    ouch = Event(
        'ouchie', ctx, DoorDeckContext.all_heroes_discard_one.__name__)

    ouch.run_script()

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1
