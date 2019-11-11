# input.py: take input from the user

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
