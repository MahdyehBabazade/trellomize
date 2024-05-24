from rich.console import Console
from rich.panel  import Panel
import os, sys, msvcrt

def prompt():
    print('\nPress any key to continue.')
    key = msvcrt.getch()

def press_esc():
    console = Console()
    current_pos = 0
    choice = 0
    mylist = ['Resume', 'Exit']
    while True:
        key = msvcrt.getch()
        if (key == b"w" or key == b"H"): # H  is for PgUp
            if current_pos > 0:
                current_pos -= 1
            elif current_pos == 0:
                current_pos = len(mylist)-1
        elif (key == b"s" or key== b"P"): # P is for PgDn
            if current_pos < len(mylist) - 1:
                current_pos += 1
            elif current_pos == len(mylist)-1:
                current_pos = 0
        elif key ==b"\r":
            choice = current_pos
            break
    return choice

def choose_by_key_with_kwargs(description="", **kwargs):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
        console.print(description, justify="center")
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
        elif key == b"\x1b":
            os.system('cls')
            esc_choice = press_esc()
            if esc_choice == 0:
                continue
            elif esc_choice == 1:
                sys.exit()
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
        console.print("Press 'ESC' to pause.", style="grey69")
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
        elif key == b"\x1b":
            os.system('cls')
            esc_choice = press_esc()
            if esc_choice == 0:
                continue
            elif esc_choice == 1:
                sys.exit()
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice

def normal_choose(mylist):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        for i in range(len(mylist)):
            if i == current_pos:
                console.print(Panel(mylist[i]), style="purple")
            else:
                console.print(Panel(mylist[i], border_style="bold purple4"))
        console.print("Press 'ESC' to pause.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if (key == b"w" or key == b"H"): # H  is for PgUp
            if current_pos > 0:
                current_pos -= 1
            elif current_pos == 0:
                current_pos = len(mylist)-1
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
            if current_pos < len(mylist) - 1:
                current_pos += 1
            elif current_pos == len(mylist)-1:
                current_pos = 0
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice