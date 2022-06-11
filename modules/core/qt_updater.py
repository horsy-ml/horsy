from qt_thread_updater import get_updater


def call(func, *args):
    get_updater().call_latest(func, *args)
