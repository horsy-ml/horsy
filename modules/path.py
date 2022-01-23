# Module for PATH actions
import os


def add_to_path(program_path: str):
    import winreg

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            existing_path_value = os.popen('echo %PATH%').read()  # Get the existing path value
            print(existing_path_value)
            new_path_value = existing_path_value + ";" + program_path  # Connect the new path to the existing path
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value)  # Update the path value


def delete_from_path(program_path: str):
    import winreg

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            existing_path_value = os.popen('echo %PATH%').read()  # Get the existing path value
            new_path_value = existing_path_value.replace(program_path + ";", "")  # Remove the program path from path
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value)  # Update the path value


def add_var(horsy_path: str):
    import winreg

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            winreg.SetValueEx(key, "HORSYPATH", 0, winreg.REG_EXPAND_SZ, horsy_path)  # Update the path value
