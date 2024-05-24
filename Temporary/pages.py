import os, json, GlobalFunctions as GF
from rich.console import Console
import user as userlib
import projects as pr
from rich.prompt import Prompt, Confirm
import os, uuid

def menu():
    introduction = "\n[bold italic]TRELLOMIZE[/]\n[grey70]Transform your project management experience with our innovative platform,\noffering streamlined coordination, real-time updates, and effective task management.[/]\n"
    choice = GF.choose_by_key_with_kwargs(introduction, SIGNUP = "[grey70]for free![/]", LOGIN = "[grey70]if you already have an account[/]")
    if choice == 0:
        signup_page()
    elif choice == 1:
        login_page()
    
        

def signup_page():
    os.system('cls')
    console = Console()
    signup_sys = userlib.SignUp()
    console.print('[bold italic white]SIGNUP[/]\nfor free\n', justify="center")
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
        except FileExistsError as error:
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
    user = userlib.User(email, username, password)
    your_account_page(user)

def login_page():
    os.system('cls')
    console = Console()
    login_sys = userlib.Login()
    console.print('[bold italic white]LOGIN[/]\nif you already have an account', justify="center")
    console.print("Enter your email: ", style="bold purple4")
    email = input()
    console.print("[bold purple4]Enter your password: [/]")
    password = input()

    while True: #this one do not work if email is not vallid
        try:
            if login_sys.load(email, password):
                console.print('Successfully logged in!')
                filename = os.path.join("AllFiles/Users", f"{email}.json") #change \\ to /
                with open(filename, 'r') as file:
                    data = json.load(file)
                    username = data.get("username")
                    user = userlib.User(email , username , password)
                    your_account_page(user)
                break
        except ValueError as error:
            os.system('cls')
            console.print(str(error)+"\n", style="bold red")
            console.print("Try again: ")
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()
        except FileNotFoundError as error:
            os.system('cls')
            console.print(str(error)+"\n", style="bold red")
            console.print("Try again: ")
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()
        except KeyError as error:
            os.system('cls')
            console.print(str(error)+"\n", style="bold red")
            console.print("Try again: ")
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()
            

def your_account_page(user):
    os.system('cls')
    console = Console()
    choice = GF.choose_by_key("[bold italic white]\nI want to ...\n", "[grey70]create a new project.", "[grey70]see my projects.", "[grey70]edit my profile.", "[grey70]back", "[grey70]logout")
    if choice == 0:
        new_project_page(user)
    elif choice == 1:
        load_projects_page()
    elif choice == 2:
        setting(user)
        #edit_info_page()
    elif choice == 3:
        pass
    elif choice == 4:
        logout_page(user)
        
def new_project_page(user):
    os.system('cls')
    console = Console()
    console.print("[grey70]Enter a title for your project: ", justify="center")
    title = input()
    myprojectid = str(uuid.uuid1())
    my_project = pr.Project(title, myprojectid, user)
    my_project.save_to_file(user)
    choice = GF.choose_by_key_with_kwargs(title, BACKLOG='', TODO='', DOING='', DONE='', ARCHIVED='')
    task_page_by_status(my_project, choice+1)

def load_projects_page(): #
    pass

def setting(user):
    choice = GF.choose_by_key("What do you want to do?" , "Edit my profile" , "delete acount")
    if choice == 0:
        os.system('cls')
        console = Console()
        console.print("[bold purple4]We want to be sure it's your acount, please enter your password.")
        password = input()
        while True:
            try:
                if user.getPassword() == userlib.hashing(password):
                    break
            except ValueError as error:
                os.system('cls')
                console.print(str(error)+"\n", style="bold red")
                console.print("Try again: ")
                console.print("[bold purple4]Enter your password: [/]")
                password = input()
            except KeyError as error:
                os.system('cls')
                console.print(str(error)+"\n", style="bold red")
                console.print("Try again: ")
                console.print("[bold purple4]Enter your password: [/]")
                password = input()
        choice = GF.choose_by_key('What do you want to change?' , 'My username' , 'My password')
        if choice == 0:
            os.system('cls')
            console.print("[bold purple4]Enter your new username.")
            new_username = input()
            filename = os.path.join("AllFiles\\Users", f"{user.getEmail()}.json")
            with open(filename , 'r') as file:
                data = json.load(file) 
                data['username'] = new_username #update username
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            consol.print("Your username has been changed successfully!") 
        elif choice == 1:
            os.system('cls')
            console.print("[bold purple4]Enter your new password.")
            new_password = userlib.hashing(input())
            filename = os.path.join("AllFiles\\Users", f"{user.getEmail()}.json")
            with open(filename , 'r') as file:
                data = json.load(file) 
                data['password'] = new_password #update password
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4) 
            os.system('cls')
            consol.print("Your password has been changed successfully!")            
    elif choice == 1:
        os.system('cls')
        console = Console()
        choice = GF.choose_by_key('Are you sure?' , 'Yes' , 'No')
        if choice == 0:
            os.system('cls')
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            console.print("[bold purple4]Enter your password: [/]")
            password = input()
            while True:
                try:
                    if userlib.hashing(password) == user.getPassword():
                        break
                except ValueError as error:
                    os.system('cls')
                    console.print(str(error)+"\n", style="bold red")
                    console.print("Try again: ")
                    console.print("[bold purple4]Enter your email: [/]")
                    email = input()
                    console.print("[bold purple4]Enter your password: [/]")
                    password = input()
                except KeyError as error:
                    os.system('cls')
                    console.print(str(error)+"\n", style="bold red")
                    console.print("Try again: ")
                    console.print("[bold purple4]Enter your email: [/]")
                    email = input()
                    console.print("[bold purple4]Enter your password: [/]")
                    password = input()
            user.delete_account()
            console.print("you delete account successfully!")
        elif choice == 1:
            setting(user)


def logout_page(user): 
    choice = GF.choose_by_key('Are you sure?' , 'Yes' , 'No')
    if choice == 0:
        console = Console()
        console.print('You log out successfully.')
        GF.prompt()
        menu()
    elif choice == 1:
        your_account_page(user)

def task_page_by_status(project, status=pr.Status.BACKLOG.value):
    os.system('cls')
    console = Console()
    console.print(pr.Status(status), style="bold italic white", justify="center")
    #choice = GF.choose_by_key(Create = f"[grey70]Add a task in {pr.Status(status)}s")
    choice = GF.choose_by_key("" , f"[grey70]Add a task in {pr.Status(status)}s" , f"see tasks in {pr.Status(status)}s")
    if choice == 0:
        os.system('cls')
        title = Prompt.ask('Enter a title for you task')
        priority = Prompt.ask('How important in this task?', choices=['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'])
        want_to_add_assignee = Confirm.ask('Wanna add any assignee?')
        task = pr.Task(title, status, priority)
        if want_to_add_assignee:
            assignee = Prompt.ask('Choose the assignees: ')
            collaborators = [collab for collab in project.getCollaborators()]
            choice = GF.normal_choose(collaborators)
            project.addCollaborator(choice)