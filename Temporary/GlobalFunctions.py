from rich.console import Console
from rich.panel  import Panel
import os, sys, msvcrt

def prompt():
    print('Press any key to continue.')
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

def choose_by_key(description="", **kwargs):
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

def choose_by_key(description="" , *args):   # Overloaded Function
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
        console.print(description, justify="center")
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

def normal_choose(*args):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        clear_text(*args)
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

def clear_text(text_to_clear):
    lines = sys.stdout.getvalue().split('\n')
    new_lines = [line for line in lines if text_to_clear not in line]
    new_content = '\n'.join(new_lines)
    sys.stdout.write("\033[H\033[J")  # Clear the terminal
    sys.stdout.write(new_content)
    sys.stdout.flush()