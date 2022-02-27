import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def softcls():
    print('\n' * os.get_terminal_size().lines)
