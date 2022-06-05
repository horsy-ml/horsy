def menu(options: list) -> int:
    for i in range(len(options)):
        print(str(i) + '  -  ' + options[i])
    user_input = None
    while user_input is None:
        try:
            user_input = int(input('\n> '))
            if user_input < 0 or user_input >= len(options):
                user_input = None
                print('Choose number between 0 and ' + str(len(options) - 1))
        except ValueError:
            print('Choose number option')

    return user_input


def get(description: str) -> str:
    print(description)
    return input('> ')
