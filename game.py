# game.py: execute commands based on the input

from input import get_input

enemy = ['sword', 'shield', 'bow']

def matches(card, enemy):
    '''
    Return true if card matches a card in enemy
    Return false if none of the cards match
    '''

    match = None

    # Take a field off the enemy
    # When we play that card
    for enemy_card in enemy:
        if card == enemy_card:
            match = enemy_card # marking card for removal

    if match != None:
        return True
    else:
        return False

def print_enemy_health(enemy):
    '''
    Print out the enemy's cards and get the user's attack
    '''

    print('Enemy HP:')
    # C++/Java/JS:
    # for(int i = 0; i < enemy.size(); i ++)
    # card = enemy[i]
    for card in enemy:
        print(card)

def attack(card, enemy):    
    '''
    Test for a match and remove it from the
    enemy's health if it's a match
    '''

    if matches(card, enemy):
        enemy.remove(card)
    else:
        print('No match')

# Main game loop
while True:
    # Print enemy output
    print_enemy_health(enemy)

    # Get input
    operation, args = get_input()

    if operation == 'play':
        # Attack with the card
        attack(args[0], enemy)
    elif operation == 'quit':
        break
    elif operation == '<3':
        print('3<')
    else:
        print('unrecognized command')

    # If the enemy is dead, then break out of the loop
    if len(enemy) == 0:
        break

print('End of game!')
if len(enemy) == 0:
    print('You won!')
