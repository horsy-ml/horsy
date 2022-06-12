from rich import print
from traceback import format_exception


def hook(type_, value: None, traceback: None):
    print("[red][!] Error happened[/]")
    print("Error type: ", type_.__name__)
    print("Error value: ", value)
    print("Error traceback: ", format_exception(type_, value, traceback)[2])
