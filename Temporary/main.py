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
        os.system('cls')
        for i in range(len(items)):
            if i == current_pos:
                console.print(Panel(items[i]), style="green")
            else:
                console.print(Panel(items[i], border_style="bold purple4"))
        console.print("Press 'q' to quit.", style="grey69")
        key = msvcrt.getch() # getch returns a byte
        if (key == b"w" or key == b"H"): # H  is for PgUp
            if current_pos > 0:
                current_pos -= 1
            elif current_pos == 0:
                current_pos = len(items)-1
            
        elif (key == b"s" or key== b"P"): # P is for PgDn
            if current_pos < len(items) - 1:
                current_pos += 1
            elif current_pos == len(items)-1:
                current_pos = 0
        elif key == b"q":
            sys.exit()
        elif key == b"\r": #this is for Enter
            choice = current_pos
            break
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
    myList = ["[grey70]SIGNUP[/]", "[grey70]LOGIN[/]"]
    choice = choose_by_key(myList)
    if choice == 0:
        signup_page()
    elif choice == 1:
        login_page()
        

def signup_page():

    os.system('cls')
    console = Console()

    console.print("[bold purple4]Enter you email: [/]")
    email = input()
    while  True:
        try:
            if user.email_isvalid(email):
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
            if user.username_isvalid(username):
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
            if user.password_isvalid(password):
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
        
    user.sign_up(email, username, password)

def login_page():
    console = Console()
    os.system('cls')
    console.print("Enter your email: ", style="bold purple4")
    username = input()
    console.print("[bold purple4]Enter your password: [/]")
    password = input()

    while True:
        try:
            if user.login(email, password):
                console.print('Successfully logged in!')
                break
        except Exception as error:
            console.print(str(error))
            console.print("Try again: ")
            console.print("[bold purple4]Enter your email: [/]")
            username = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()

menu()