from rich.console import Console
from rich.panel  import Panel
import os, sys, msvcrt, json

def prompt():
    print('\nPress any key to continue.')
    key = msvcrt.getch()

def choose_by_key_with_kwargs(description="", **kwargs):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
        console.print(description)
        for index, (first, second) in enumerate(kwargs.items()):
            if index == current_pos:
                console.print(Panel(second, title=first), style="purple")
            else:
                console.print(Panel(second, title=first, border_style="bold purple4"))
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if (key == b"w" or key == b"H"): # H  is for PgUp
            if current_pos > 0:
                current_pos -= 1
            elif current_pos == 0:
                current_pos = len(kwargs)-1
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
            if current_pos < len(kwargs) - 1:
                current_pos += 1
            elif current_pos == len(kwargs)-1:
                current_pos = 0
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice

def choose_by_key(description="", *args):   # Overloaded Function
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
        console.print(description)
        for i in range(len(args)):
            if i == current_pos:
                console.print(Panel(args[i]), style="purple")
            else:
                console.print(Panel(args[i], border_style="bold purple4"))
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if (key == b"w" or key == b"H"): # H  is for PgUp
            if current_pos > 0:
                current_pos -= 1
            elif current_pos == 0:
                current_pos = len(args)-1
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
            if current_pos < len(args) - 1:
                current_pos += 1
            elif current_pos == len(args)-1:
                current_pos = 0
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice

def load_the_data(email):
    directory = "AllFiles/Users"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{email}.json")
    with open(filename, "r") as f:
        data = json.load(f)
    return data