from rich.console import Console
from rich.panel import Panel
import os
import msvcrt
import user
import sys

def press_esc():
    console = Console()
    current_pos = 0
    choice = 0
    mylist = ['Resume', 'Exit']
    while True:
        key = msvcrt.getch()
        if (key == b"w" or key == b"H"): # H  is for PgUp
            choice = (choice - 1 + len(mylist)) % len(mylist)
        elif (key == b"s" or key== b"P"): # P is for PgDn
            choice = (choice + 1) % len(mylist)
        return choice
def choose_by_key(*args):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        os.system('cls')
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
        elif key == b"esc":
            os.system('cls')
            console.print(Panel("Resume", border_style="bold purple4"))
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
    return choice

def introduction():
    os.system('cls')
    console = Console()
    introduction = "\n[bold italic]TRELLOMIZE[/]\n[grey70]Transform your project management experience with our innovative platform,\noffering streamlined coordination, real-time updates, and effective task management.[/]\n"
    console.print(introduction, justify="center")
    console.print(Panel("[grey70]for free![/]", title="SIGNUP", border_style="bold purple4"), justify="center")
    console.print("or\n", justify="center")
    console.print(Panel("[grey70]if you already have an account[/]", title="LOGIN", border_style="bold purple4"), justify="center")
    console.print("Press any key to continue.\n", justify="center", style="grey69")
    key = msvcrt.getch()

def menu():
    introduction()
    choice = choose_by_key("[grey70]SIGNUP[/]", "[grey70]LOGIN[/]")
    if choice == 0:
        signup_page()
    elif choice == 1:
        login_page()
        

def signup_page():

    os.system('cls')
    console = Console()
    signup_sys = user.SignUp()
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
    login_sys = user.Login()
    os.system('cls')
    console.print("Enter your email: ", style="bold purple4")
    email = input()
    console.print("[bold purple4]Enter your password: [/]")
    password = input()

    while True:
        try:
            if login_sys.load(email, password):
                console.print('Successfully logged in!')
                your_account_page()
                break
        except Exception as error:
            console.print(str(error))
            console.print("Try again: ")
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()

def your_account_page():
    os.system('cls')
    console = Console()
    console.print("I want to ...")
    choice = choose_by_key("[grey70]create a new project.", "[grey70]see my projects.", "[grey70]edit my profile.", "[grey70]back", "[grey70]logout.")
    if choice == 0:
        new_project_page()
    elif choice == 1:
        load_projects()
    elif choice == 2:
        edit_info()
    elif choice == 3:
        pass
    elif choice == 4:
        logout()
        
def new_project_page():
    console = Console()
    console.print("[grey70]Enter a title for your project: ")
    title = input()


def load_projects():
    pass

def edit_info():
    pass

def logout():
    pass

menu()