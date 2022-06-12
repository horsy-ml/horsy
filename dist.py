import os


v = 'venv\\Scripts\\activate & '

if not os.path.exists('bin'):
    os.makedirs('bin')

choice = int(input('''\
1 - Build
2 - Release

> \
'''))

if choice == 1:
    print()
    build_this = input('''\
0 - Build all
1 - Build horsy
2 - Build horsy-gui

> \
''')
    build_this = build_this if build_this != '0' else '123456789'

    if '1' in build_this:
        os.system(
            v + 'pyinstaller --onefile --exclude-module PyQt5 --icon ui\img\icon.ico --noconfirm --console "horsy.py"'
        )
    if '2' in build_this:
        os.system(
            v + 'pyinstaller --onefile --icon ui\img\icon.ico --noconfirm --console "horsygui.py"'
        )

elif choice == 2:
    os.system("xcopy /s /Y dist\horsy.exe bin\horsy.exe*")
    os.system("xcopy /s /Y dist\horsygui.exe bin\horsygui.exe*")

    with open("web_vars/version", "r") as f_r:
        version = f_r.readline()

    with open("web_vars/version", "w") as f_w:
        f_w.write(str(int(version) + 1))

    print(f"Version {int(version) + 1} released")

input('Press enter to exit...')
