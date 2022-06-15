import os
import modules.core.vars as horsy_vars


def check_files():
    if not os.path.exists(horsy_vars.horsypath + 'apps'):
        os.makedirs(horsy_vars.horsypath + 'apps')

    if not os.path.isfile(horsy_vars.horsypath + 'config.cfg'):
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            f.write('{}')

    if not os.path.isfile(horsy_vars.horsypath + 'apps/versions.json'):
        with open(horsy_vars.horsypath + 'apps/versions.json', 'w+') as f:
            f.write('{}')

    if os.path.isfile(horsy_vars.horsypath + 'horsygui.old'):
        os.remove(horsy_vars.horsypath + 'horsygui.old')
