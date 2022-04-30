# Module for PATH actions
import os
import winreg


def get_path() -> str:
    """
    Returns the current PATH variable
    """
    existing_path_value_s = set()
    for i in os.popen('PATH').read()[5:].replace('\n', '').split(';'):
        existing_path_value_s.add(i + ';')
    existing_path_value = str()
    for i in sorted(list(existing_path_value_s)):
        existing_path_value += i

    return existing_path_value


def add_to_path(program_path: str):
    """
    Adds a program to the PATH variable
    """
    existing_path_value = get_path()
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            new_path_value = \
                existing_path_value + \
                f'{";" if existing_path_value[-1] != ";" else ""}' + \
                program_path + ';' + program_path + "\\apps;"  # Create new path value
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value)  # Update the path value


def add_var(horsy_path: str):
    """
    Creates HORSYPATH environment variable
    """
    import winreg
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            winreg.SetValueEx(key, "HORSYPATH", 0, winreg.REG_EXPAND_SZ, horsy_path)  # Update the path value
