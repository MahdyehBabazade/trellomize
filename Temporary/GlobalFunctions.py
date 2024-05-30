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
        console.print(description)
        for index, (first, second) in enumerate(kwargs.items()):
            if index == current_pos:
                console.print(Panel(second, title=first), style="purple")
            else:
                console.print(Panel(second, title=first, border_style="bold purple4"))
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if (key == b"w" or key == b"H"): # H  is for PgUp
            current_pos = (current_pos - 1) % len(kwargs)
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
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
        console.print(description)
        for i in range(len(args)):
            if i == current_pos:
                console.print(Panel(args[i]), style="purple")
            else:
                console.print(Panel(args[i], border_style="bold purple4"))
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if (key == b"w" or key == b"H"): # H  is for PgUp
            current_pos = (current_pos - 1) % len(args)
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
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
        if (key == b"w" or key == b"H"): # H  is for PgUp
            current_pos = (current_pos - 1) % len(args)
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
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

def switch_panels(layout, panel_names : list, panel_texts):
    console = Console()
    current_pos = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # 'nt' is for windows, I could use it in other cplaces but didn't remember :(
        for i, name in enumerate(panel_names):
            if i == current_pos:
                layout[name].update(renderable=Panel(panel_texts[i], title=name, style="purple bold"))
            else:
                layout[name].update(renderable=Panel(panel_texts[i], title=name))
        console.print(layout)
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch()
        if key == b"q":
            sys.exit()
        if key == b"w":  # Left arrow
            current_pos = (current_pos - 1) % len(panel_names)
        elif key == b"s":  # Right arrow
            current_pos = (current_pos + 1) % len(panel_names)
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice
            
def create_layout(project : pr.Project):
    console = Console()
    tasks = project.getTasks()
    backlogs = ""
    for task in tasks:
        if task.getStatus() == 1:
            backlogs += f"{task.getTitle()}\n"
    todos = ""
    for task in tasks:
        if task.getStatus() == 2:
            todos += f"{task.getTitle()}\n"
    doings = ""
    for task in tasks:
        if task.getStatus() == 3:
            doings += f"{task.getTitle()}\n"
    dones = ""
    for task in tasks:
        if task.getStatus() == 4:
            dones += f"{task.getTitle()}\n"
    archiveds = ""
    for task in tasks:
        if task.getStatus() == 5:
            archiveds += f"{task.getTitle()}\n"

    layout = Layout()
    layout.split(
        Layout(name='title', ratio=1),  
        Layout(name='first', ratio=12),  
        Layout(name='second', ratio=16),
    )
    layout["title"].update(Text(project.getTitle(), justify="center", style="bold magenta"))
    
    layout["first"].split(
    Layout(renderable=Panel(backlogs, title="BACKLOG"), name="BACKLOG"),
    Layout(renderable=Panel(todos, title="TODO"), name="TODO"),
    splitter="row"
    )

    layout["second"].split(
        Layout(renderable=Panel(doings, title="DOING"), name="DOING"),
        Layout(renderable=Panel(dones, title="DONE"), name="DONE"),
        Layout(renderable=Panel(archiveds, title="ARCHIVED"), name="ARCHIVED"),
        splitter="row"
    )
    return layout