from rich.console import Console
from rich.panel  import Panel
from rich.layout import Layout
from rich.text import Text
import projects as pr
import os, sys, msvcrt, json, logging

def prompt():
    print('\nPress any key to continue.')
    key = msvcrt.getch()

def log_actions(user):

    directory = "AllFiles\\Logs"
    if not os.path.exists(directory):
        os.makedirs(directory)

    logging.basicConfig(
        filename = os.path.join(directory, f"{user.getEmail()}.log"),
        level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )
    log = logging.getLogger(user.getEmail())
    return log

def choose_by_key_with_kwargs(description="", **kwargs):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
        console.print(description, justify="center")
        for index, (first, second) in enumerate(kwargs.items()):
            if index == current_pos:
                console.print(Panel(second, title=first, expand=False), style="purple", justify="center")
            else:
                console.print(Panel(second, title=first, expand=False, border_style="bold purple4"), justify="center")
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if key == b"H": # H  is for PgUp
            current_pos = (current_pos - 1) % len(kwargs)
            
        elif key== b"P": # P is for PgDn
            current_pos = (current_pos + 1) % len(kwargs)
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
        console.print(description, justify="center")
        for i in range(len(args)):
            if i == current_pos:
                console.print(Panel(args[i], expand=False), style="purple", justify="center")
            else:
                console.print(Panel(args[i], expand=False, border_style="bold purple4"), justify="center")
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if key == b"H": # H  is for PgUp
            current_pos = (current_pos - 1) % len(args)
            
        elif key== b"P": # P is for PgDn
            current_pos = (current_pos + 1) % len(args)
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice

def normal_choose(description="", *args):   # Overloaded Function
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
        console.print(description)
        for i in range(len(args)):
            if i == current_pos:
                console.print(f"{i+1}. {args[i]}\n", style="purple")
            else:
                console.print(f"{i+1}. {args[i]}\n")
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if key == b"H": # H  is for PgUp
            current_pos = (current_pos - 1) % len(args)
            
        elif key== b"P": # P is for PgDn
            current_pos = (current_pos + 1) % len(args)
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

def write_to_the_file(data):
    filename = os.path.join("AllFiles\\Users", f"{data["email"]}.json")
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_the_collaborators_data(*args): # Returns all the collaborators' data in a list. Args are emails of the collaborators
    directory = "AllFiles\\Users"
    data = []
    for email in args:
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, f"{email}.json")
        with open(filename, "r") as f:
            data.append(json.load(f))
    return data

            
def switch_panels(project: pr.Project):
    console = Console()
    tasks = project.getTasks()
    
    panels = {"BACKLOG": "", "TODO": "", "DOING": "", "DONE": "", "ARCHIVED": ""}
    
    for i,task in enumerate(tasks):
        if task.getStatus() == 1:
            panels["BACKLOG"] += f"#{i+1}: {task.getTitle()}\n"
        elif task.getStatus() == 2:
            panels["TODO"] += f"{i+1}. {task.getTitle()}\n"
        elif task.getStatus() == 3:
            panels["DOING"] += f"{i+1}. {task.getTitle()}\n"
        elif task.getStatus() == 4:
            panels["DONE"] += f"{i+1}. {task.getTitle()}\n"
        elif task.getStatus() == 5:
            panels["ARCHIVED"] += f"{i+1}. {task.getTitle()}\n"

    layout = Layout()
    layout.split(
        Layout(name="space", ratio=2),
        Layout(name='title', ratio=1),
        Layout(name='first', ratio=12),
        Layout(name='last', ratio=1)
    )
    layout["space"].update(Text(" "))
    layout["title"].split(
        Layout(renderable=Text(project.getTitle(), justify="center", style="bold magenta"))
    )
    
    layout["first"].split(
        Layout(renderable=Text(" ")),
        *[Layout(renderable=Panel(panels[name], title=name), name=name) for name in panels],
        Layout(renderable=Text(" ")),
        splitter="row"
    )
    layout["last"].split(
        Layout(renderable=Text(" ")),
        Layout(renderable=Panel(Text("Back", justify="center")), name="Back"),
        Layout(renderable=Text(" ")),
        splitter="row"
    )

    current_pos = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, name in enumerate(list(panels.keys()) + ["Back"]):
            if i == current_pos:
                if i != 5:
                    layout[name].update(renderable=Panel(panels.get(name, "Back"), title=name, style="purple bold"))
                else:
                    layout[name].update(renderable=Panel(Text(panels.get(name, "Back"), justify="center"), title="", style="purple bold"))
            else:
                if i != 5:
                    layout[name].update(renderable=Panel(panels.get(name, "Back"), title=name))
                else:
                    layout[name].update(renderable=Panel(Text(panels.get(name, "Back"), justify="center"), title=""))
        console.print(layout)
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch()
        if key == b'q':
            sys.exit()
        elif key == b'K':  # Left arrow
            current_pos = (current_pos - 1) % (len(panels) + 1)
        elif key == b'M':  # Right arrow
            current_pos = (current_pos + 1) % (len(panels) + 1)
        elif key == b'\r':  # Enter
            choice = current_pos
            break

    return choice