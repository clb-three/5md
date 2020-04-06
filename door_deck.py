# A deck of door cards you must defeat

from door_card import DoorCard

# Place an initial deck of 5 enemies
num_enemies = 5
enemy_deck = [DoorCard() for _ in range(0, num_enemies)]

# The enemy face up on the top of the deck
current_enemy = None


def try_draw():
    global current_enemy
    if len(enemy_deck) > 0:
        current_enemy = enemy_deck.pop()
        return True
    else:
        return False
