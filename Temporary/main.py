from rich.console import Console
from rich.panel import Panel
import os
import msvcrt
import user
import sys

def choose_by_key(items):
    console = Console()
    current_pos = 0
    choice = 0
    while True:
        key = msvcrt.getch() #it returns a byte
        if key == b"w" and current_pos > 0:
            current_pos -= 1
        elif key == b"s" and current_pos < len(items) - 1:
            current_pos += 1
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
        os.system('cls')
        for i in range(len(items)):
            if i == current_pos:
                console.print(Panel(items[i]), style="green")
            else:
                console.print(Panel(items[i], border_style="bold purple4"))
        console.print("Press 'q' to quit.", style="grey69")
    return choice

def introduction():
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
    myList = ["[grey70]SIGNUP[/]","[grey70]LOGIN[/]"]
    if choose_by_key(myList) == 0:
        signup_page()
    elif choose_by_key(myList) == 1:
        login_page()
        

def signup_page():
    os.system('cls')
    console = Console()
    console.print("[bold purple4]Enter you email: [/]\n")
    email = input()
    while not user.email_isvalid(email):
        os.system('cls')
        console.print("Invalid Email!\n", style="red")
        console.print("[bold purple4]Enter you email: [/]\n")
        email = input()

    console.print("[bold purple4]Enter you username: [/]\n")
    username = input()
    while not user.username_isvalid(username):
        os.system('cls')
        console.print("[bold purple4]Enter you email: [/]\n")
        console.print(email)
        console.print("\nInvalid Username!", style="red")
        console.print("[bold purple4]Enter you username: [/]\n")
        username = input()

    console.print("[bold purple4]Enter you password: [/]\n")
    password = input()
    while not user.password_isvalid(password):
        os.system('cls')
        console.print("[bold purple4]Enter you email: [/]\n")
        console.print(email)
        console.print("\n[bold purple4]Enter your username: [/]\n")
        console.print(username)
        console.print("\nPassword must be 8 or more characters!", style="red")
        console.print("[bold purple4]Enter you password: [/]\n")
        password = input()

    user.sign_up(email, username, password)
def login_page():
    console = Console()
    os.system('cls')
    console.print("Enter your email or username: ", style="bold purple4")
    username = input()
    user.login()


menu()