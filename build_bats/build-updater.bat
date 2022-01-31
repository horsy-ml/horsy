cd ..
pip install -r requirements.txt
pyinstaller --noconfirm --icon "img/icon.ico" --onefile --console "horsy_updater.py"
rmdir /s /q __pycache__
del horsy_updater.spec