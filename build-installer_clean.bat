pip install -r requirements.txt
rmdir /s /q build
pyinstaller --noconfirm --icon "img/icon.ico" --windowed --onefile "horsy_installer.py"
rmdir /s /q __pycache__
del horsy_installer.spec
rmdir /s /q build