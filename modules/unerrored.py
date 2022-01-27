import threading
import subprocess
import time


def run(func, *args):
    try:
        subprocess.Popen(func, *args, shell=True)
    except:
        time.sleep(5)


def run_threaded(func, *args):
    try:
        threading.Thread(target=func, args=args).start()
    except:
        time.sleep(5)


def run_old(func, *args):
    try:
        func(args)
    except:
        pass
