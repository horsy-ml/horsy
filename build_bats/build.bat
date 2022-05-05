cd ..
pip install -r requirements.txt
pyinstaller --noconfirm --icon "img/icon.ico" --console --onefile "horsy.py"
rmdir /s /q __pycache__
del horsy.spec
cd build_bats