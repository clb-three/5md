# All possible moves a hero can have
action_cards = [
    "sword",
    "shield",
    "arrow",
    "jump",
    "scroll"
]

def is_valid(card):
    '''
    Return whether card is valid
    '''
    return card in action_cards
