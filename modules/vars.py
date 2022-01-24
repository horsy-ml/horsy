import os


protocol = "http://"
server_url = 'localhost:60666'
horsypath = os.popen('echo %HORSYPATH%').read().replace('\n', '') + '/'
