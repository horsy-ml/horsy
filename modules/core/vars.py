import os


protocol = "https://"
server_url = 'horsy.ml'
horsypath = os.popen('echo %HORSYPATH%').read().replace('\n', '') + '\\'
