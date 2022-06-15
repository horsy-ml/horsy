from rich import print
from traceback import format_exception


def hook(type_, value, traceback):
    print("[red][!] Error happened[/]")
    print("Error type: ", type_.__name__)
    print("Error value: ", value)
    print("Error traceback: ", format_exception(type_, value, traceback)[2])


def thread_hook(exception):
    print(f"[red][!] Error happened in {exception.thread}[/]")
    print("Error type: ", exception.exc_type.__name__)
    print("Error value: ", exception.exc_value)
    print("Error traceback: ", format_exception(exception.exc_type, exception.exc_value, exception.exc_traceback)[2])
