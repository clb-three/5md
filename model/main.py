if __name__ == '__main__':
    table = table_factory.get_table()
    print(table.gamestate)
    while (command := input('Enter a command $>')) != 'quit':
        message = table.process_command(command)
