# input.py: take input from the user


def get_input():
    '''
    Split command into '<playername> <operation> <args[0]> <args[1]> ... <args[n]>'
    '''
    command = input('Enter a command: ')

    return command.split(' ')
