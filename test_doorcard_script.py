
from script import DoorDeckContext
from hero import Hero
from event import Event


def mock_heroes(*names):
    '''
    Constructs a mock instance of a map of Heroes from a list of names
    '''
    return {h.name: h for h in [Hero(n) for n in names]}


def test_ado():
    heroes = mock_heroes('benji', 'austin')
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    ctx = DoorDeckContext(heroes)

    ctx.all_heroes_discard_one()

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1


def test_event_ado():
    heroes = mock_heroes('benji', 'austin')
    for h in heroes.values():
        h.draw_card()
    deck_sizes = [len(hero.hand) for hero in heroes.values()]
    ctx = DoorDeckContext(heroes)

    ouch = Event(
        'ouchie', ctx, DoorDeckContext.all_heroes_discard_one.__name__)

    ouch.run_script()

    for i, hero in enumerate(heroes.values()):
        assert len(hero.hand) == deck_sizes[1] - 1
