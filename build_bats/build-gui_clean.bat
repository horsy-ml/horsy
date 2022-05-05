cd ..
pip install -r requirements.txt
rmdir /s /q build
pyinstaller --noconfirm --icon "img/icon.ico" --console --onefile "horsygui.py"
rmdir /s /q __pycache__
del horsygui.spec
rmdir /s /q build
cd build_bats