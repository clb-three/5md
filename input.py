# input.py: takes input and executes commands based on the input

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

def get_input():
    '''
    Split command into '<operation> <args[0]> <args[1]> ... <args[n]>'
    '''
    command = input('Enter a command:')
    
    operation = None
    args = []
    try:
        # Assign operation and args
        operation, args = command.split(' ', maxsplit=1)
    except ValueError:
        # There was only one word typed
        operation = command

    # Convert args to a list if it's auto-resolved to a string
    if not isinstance(args, list):
        args = [args]

    return operation, args

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
