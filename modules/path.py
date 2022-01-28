# Module for PATH actions
import os
os.popen('cls')
existing_path_value_l = os.popen('PATH').read()[5:].replace('\n', '')  # Get the existing path value
existing_path_value_s = set()
for i in existing_path_value_l.split(';'):
    existing_path_value_s.add(i + ';')
existing_path_value_s = list(existing_path_value_s)
existing_path_value_s.sort()
existing_path_value = str()
for i in existing_path_value_s:
    existing_path_value += i

print('Existing path value: ' + existing_path_value)


def add_to_path(program_path: str):
    import winreg
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            new_path_value = existing_path_value + f'{";" if existing_path_value[-1] != ";" else ""}' + \
                             program_path + ';' + program_path + "\\apps;"  # Create new
            print(new_path_value)
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value)  # Update the path value


def add_var(horsy_path: str):
    import winreg

    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as root:  # Get the current user's registry
        with winreg.OpenKey(root, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:  # Open the environment key
            winreg.SetValueEx(key, "HORSYPATH", 0, winreg.REG_EXPAND_SZ, horsy_path)  # Update the path value
