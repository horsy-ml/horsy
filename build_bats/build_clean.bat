cd ..
pip install -r requirements.txt
rmdir /s /q build
pyinstaller --noconfirm --icon "img/icon.ico" --console --onefile "horsy.py"
rmdir /s /q __pycache__
del horsy.spec
rmdir /s /q build