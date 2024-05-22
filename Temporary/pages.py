import os, msvcrt, sys, json, GlobalFunctions as GF
from rich.console import Console
from rich.panel import Panel
import user as userlib
import projects as pr
from rich.prompt import Prompt, Confirm

def menu():
    introduction = "\n[bold italic]TRELLOMIZE[/]\n[grey70]Transform your project management experience with our innovative platform,\noffering streamlined coordination, real-time updates, and effective task management.[/]\n"
    choice = GF.choose_by_key(SIGNUP = "[grey70]for free![/]", LOGIN = "[grey70]if you already have an account[/]")
    if choice == 0:
        signup_page()
    elif choice == 1:
        login_page()
        

def signup_page():

    os.system('cls')
    console = Console()
    signup_sys = userlib.SignUp()
    console.print("[bold purple4]Enter you email: [/]")
    email = input()
    while  True:
        try:
            if signup_sys.email_isvalid(email):
                break
        except ValueError as error:
            os.system('cls')
            console.print(error, style="red")
            console.print("[bold purple4]Enter you email: [/]")
            email = input()

    console.print("[bold purple4]Enter you username: [/]")
    username = input()
    while True:
        try:
            if signup_sys.username_isvalid(username):
                break
        except ValueError as error:
            os.system('cls')
            console.print(error, style="red")
            console.print("[bold purple4]Enter you email: [/]")
            console.print(email)
            console.print("[bold purple4]Enter you username: [/]")
            username = input()
            
    console.print("[bold purple4]Enter you password: [/]")
    password = input()
    while  True:
        try:
            if signup_sys.password_isvalid(password):
                break      
        except ValueError as error:
            os.system('cls')
            console.print(error, style="red")
            console.print("[bold purple4]Enter you email: [/]")
            console.print(email)
            console.print("[bold purple4]Enter you username: [/]")
            console.print(username)
            console.print("[bold purple4]Enter you password: [/]")
            password = input()
        
    signup_sys.sign_up(email, username, password)

def login_page():
    console = Console()
    login_sys = userlib.Login()
    os.system('cls')
    console.print("Enter your email: ", style="bold purple4")
    email = input()
    console.print("[bold purple4]Enter your password: [/]")
    password = input()

    while True:
        try:
            if login_sys.load(email, password):
                console.print('Successfully logged in!')
                filename = os.path.join("AllFiles\\Users", f"{email}.json")
                with open(filename, 'r') as file:
                    data = json.load(file)
                    username = data.get("username")
                    user = userlib.User(email , username , password)
                    your_account_page(user)
                break
        except ValueError as error:
            console.print(str(error))
            console.print("Try again: ")
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()

def your_account_page(user):
    os.system('cls')
    console = Console()
    choice = GF.choose_by_key("[bold italic white]I want to ...", "[grey70]create a new project.", "[grey70]see my projects.", "[grey70]edit my profile.", "[grey70]back", "[grey70]logout")
    if choice == 0:
        new_project_page(user)
    elif choice == 1:
        load_projects_page()
    elif choice == 2:
        edit_info_page()
    elif choice == 3:
        pass
    elif choice == 4:
        logout_page()
        
def new_project_page(user):
    console = Console()
    console.print("[grey70]Enter a title for your project: ", justify="center")
    title = input()
    my_project = pr.Project(title, user)
    pr.create_new_project(my_project, user)
    choice = GF.choose_by_key(title, BACKLOG='', TODO='', DOING='', DONE='', ARCHIVED='')
    task_page_by_status(my_project, choice+1)

def load_projects_page(): #
    pass

def edit_info_page():
    pass

def logout_page(): #
    pass

def task_page_by_status(project, status=pr.Status.BACKLOG.value):
    os.system('cls')
    console = Console()
    console.print(pr.Status(status), style="bold itatlic white", justify="center")
    choice = GF.choose_by_key(Create = f"[grey70]Add a task in {pr.Status(status)}s")
    if choice == 0:
        os.system('cls')
        title = Prompt.ask('Enter a title for you task')
        priority = Prompt.ask('How important in this task?', choices=['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'])
        want_to_add_assignee = Confirm.ask('Wanna add any assignee?')
        task = pr.Task(title, status, priority)
        if want_to_add_assignee:
            assignee = Prompt.ask('Choose the assignees: ')
            choice = GF.normal_choose(project.getCollaborators())