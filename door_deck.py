# A deck of door cards you must defeat

from enemy import DoorCard

# Place an initial deck of 5 enemies
enemy_deck = [DoorCard() for _ in range(0, 5)]
# The enemy face up on the top of the deck
current_enemy = None
def try_draw():
    global current_enemy
    if len(enemy_deck) > 0:
        current_enemy = enemy_deck.pop()
        return True
    else:
        return None
