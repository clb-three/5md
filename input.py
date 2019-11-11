# input.py: takes input and executes commands based on the input

enemy = ['sword', 'shield', 'bow']

def matches(card, enemy):
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

# Main game loop
while True:
    print('We need to attack the enemy with:')
    # C++/Java/JS:
    # for(int i = 0; i < enemy.size(); i ++)
    # card = enemy[i]
    for card in enemy:
        print(card)

    card = input('Enter a card:')

    if matches(card, enemy):
        enemy.remove(card)
    else:
        print('No match')

    if len(enemy) == 0:
        break

print('You won!')
