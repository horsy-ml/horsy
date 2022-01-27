pip install -r requirements.txt
pyinstaller --noconfirm --icon "img/icon.ico" --console --onefile "horsygui.py"
rmdir /s /q __pycache__
del horsygui.spec