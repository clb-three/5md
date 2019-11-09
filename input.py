# input.py: takes input and executes commands based on the input
# Currently just takes cards to play

enemy = ['sword', 'shield', 'bow']

while True:
    print('We need to attack the enemy with:')
    # C++/Java/JS:
    # for(int i = 0; i < enemy.size(); i ++)
    # card = enemy[i]
    for card in enemy:
        print(card)

    line = input('Enter a card:')

    match = None

    # Take a field off the enemy
    # When we play that card
    for card in enemy:
        if line == card:
            match = card # marking card for removal

    if match != None:
        enemy.remove(match)
    else:
        print('No match')

    if len(enemy) == 0:
        break

print('You won!')
