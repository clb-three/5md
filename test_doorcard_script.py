
from script import DoorDeckContext
from hero import Hero
from event import Event


def test_all_discard_one():
    benji = Hero('benji')
    austin = Hero('austin')
    heroes = {
        'benji': benji,
        'austin': austin
    }
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    ctx = DoorDeckContext(heroes)

    ctx.all_heroes_discard_one()

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1


def test_event_all_discard_one():
    benji = Hero('benji')
    austin = Hero('austin')
    heroes = {
        'benji': benji,
        'austin': austin
    }
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    ctx = DoorDeckContext(heroes)

    ouch = Event('ouchie', ctx, 'all_heroes_discard_one')

    ouch.run_script()

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1
