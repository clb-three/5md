
enemy = ['sword', 'shield', 'bow']

while True:
    print('We need to attack the enemy with:')
    # C++/Java/JS:
    # for(int i = 0; i < enemy.size(); i ++)
    # card = enemy[i]
    for card in enemy:
        print(card)

    line = input('Enter a card:')

    # Take a field off the enemy
    # When we play that card
    for card in enemy:
        if line == card:
            enemy.remove(card)

    if len(enemy) == 0:
        break

print('You won!')
