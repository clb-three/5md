# All possible moves a hero can have
# TODO Issue #10: Of course, this isn't all the moves that a hero can have.
action_cards = [
    "sword",
    "shield",
    "arrow",
    "jump",
    "scroll"
]


def deck():
    '''
    The deck for a given hero.
    TODO: Make this different depending on the hero.
    '''
    return action_cards


def is_valid(card):
    '''
    Return whether card is valid
    '''
    return card in action_cards
