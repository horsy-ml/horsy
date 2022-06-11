import os
import sys


protocol = "https://"
server_url = 'horsy.ml'
horsypath = (os.path.dirname(sys.executable) + '\\') \
    if "python.exe" not in sys.executable \
    else os.path.expanduser("~") + '\\horsy\\' if os.path.exists(os.path.expanduser("~") + '\\horsy') \
    else (lambda: (os.mkdir(os.path.expanduser("~") + '\\horsy'), os.path.expanduser("~") + '\\horsy\\'))()[1]
