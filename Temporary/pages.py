import os, json, GlobalFunctions as GF
from rich.console import Console
import user as userlib
import projects as pr, time
from rich.prompt import Prompt, Confirm
import os, uuid
from rich.text import Text

def menu():
    introduction = "\n[bold italic]TRELLOMIZE[/]\n[grey70]Transform your project management experience with our innovative platform,\noffering streamlined coordination, real-time updates, and effective task management.[/]\n"
    choice = GF.choose_by_key_with_kwargs(Text(introduction, justify="center"), SIGNUP = "[grey70]for free![/]", LOGIN = "[grey70]if you already have an account[/]")
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
    while  True:
        try:
            if login_sys.correct_email(email):
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
    console.print("[bold purple4]Enter your password: [/]")
    password = input()
    while  True:
        try:
            if login_sys.correct_password(email , password):
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
            console.print('Successfully logged in!')

    filename = os.path.join("AllFiles/Users", f"{email}.json") #change \\ to /
    with open(filename, 'r') as file:
        data = json.load(file)
        username = data.get("username")
        user = userlib.User(email , username , password)
        your_account_page(user)
            

def your_account_page(user):
    os.system('cls')
    console = Console()
    choice = GF.choose_by_key("[bold italic white]\nI want to ...\n", "create a new project.", "see my projects.", "go to the setting.", "logout from my account.")
    if choice == 0:
        new_project_page(user)
    elif choice == 1:
        load_projects_page()
    elif choice == 2:
        setting(user)
    elif choice == 3:
        logout_page(user)
        
def new_project_page(user): #COMPLETEDDDDDDDD
    os.system('cls')
    console = Console()
    console.print(f"{user.getUsername()}")
    console.print("[grey70]Enter a title for your project: ")
    title = input()

    # Checking the project id
    console.print('[grey70]Enter a title for your project (optional):')
    myprojectid = input()
    directory = "AllFiles\\Users"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{user.getEmail()}.json")
    with open(filename, 'r') as f:
        data = json.load(f)
    if myprojectid != "" and myprojectid not in data['projects']:
        my_project = pr.Project(title, user, myprojectid)
    else:
        my_project = pr.Project(title, user)
    ########################################

    my_project.save_to_file(user)
    choice = GF.choose_by_key_with_kwargs(Text(title, justify="center"), BACKLOG='', TODO='', DOING='', DONE='', ARCHIVED='')
    task_page_by_status(user, my_project, choice+1)

def load_projects_page(user):
    pass

def setting(user):
    choice = GF.choose_by_key("What do you want to do?" , "Edit my profile" , "delete account" , "Back")

    if choice == 0:
        os.system('cls')
        console = Console()
        console.print("[bold purple4]We want to be sure it's your acount, please enter your password.")
        password = input()
        while True:
            try:
                if user.getPassword() == userlib.hashing(password):
                    break
            except:
                os.system('cls')
                console.print("Invalid password"+"\n", style="bold red")
                console.print("Try again: ")
                console.print("[bold purple4]Enter your password: [/]")
                password = input()

        choice = GF.choose_by_key('What do you want to change?' , 'My username' , 'My password' , 'Back')
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
            console.print("\n[bold purple4]Your username has been changed successfully!")
            GF.prompt()
            setting(user)
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
            console.print("\n[bold purple4]Your password has been changed successfully!")
            GF.prompt()
            setting(user)
        elif choice == 2:
            os.system('cls')
            setting(user)

    elif choice == 1:
        os.system('cls')
        console = Console()
        choice = GF.choose_by_key('Are you sure?' , 'Yes' , 'No')
        if choice == 0:
            os.system('cls')
            login_sys = userlib.Login()
            console.print("[bold purple4]Enter your email: [/]")
            email = input()
            while True:
                try:
                    if login_sys.correct_email(email):
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
            console.print("[bold purple4]Enter your password: [/]") 
            password = input()
            while True:
                if userlib.hashing(password) == user.getPassword():
                    break      
                else:
                    os.system('cls')
                    console.print("Invalid password", style="red")
                    console.print("[bold purple4]Enter you email: [/]")
                    console.print(email)
                    console.print("[bold purple4]Enter you password: [/]")
                    password = input()
            console.print("You have delete your acount successfully!")
            user.delete_account()
            menu() 
        elif choice == 1:
            os.system('cls')
            setting(user)

    elif choice == 2:
        os.system('cls')
        your_account_page(user)


def logout_page(user): 
    choice = GF.choose_by_key('Are you sure?' , 'Yes' , 'No')
    if choice == 0:
        console = Console()
        console.print('You log out successfully.')
        GF.prompt()
        menu()
    elif choice == 1:
        your_account_page(user)

def task_page_by_status(user, project, status=pr.Status.BACKLOG): # COMPLETEDDDDDDDDD
    os.system('cls')
    console = Console()
    console.print(pr.Status(status).name, style="bold italic white", justify="center")
    choice = GF.choose_by_key_with_kwargs(Create = f"[grey70]Add a task in {pr.Status(status).name}s")
    #choice = GF.choose_by_key("" , f"[grey70]Add a task in {pr.Status(status)}s" , f"see tasks in {pr.Status(status)}s")
    if choice == 0:
        os.system('cls')
        console.print('Enter a title for your task: ')
        title = input()
        os.system('cls')
        choice = GF.choose_by_key('Enter a title for you task:\n'+title+'\nHow important is this task?', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL', 'DEFAULT')
        priority = pr.Status(choice+1).value
        if choice != 4:
            task = pr.Task(title, status, priority)
        else:
            task = pr.Task(title, status)

        want_to_add_assignee = Confirm.ask('Wanna add any assignee?')        
        if want_to_add_assignee:
            console.print('Choose the assignee: ')
            collaborators = [collab.getUsername() for collab in project.getCollaborators()]
            choice = GF.choose_by_key('Enter a title for you task:\n'+title+'\nHow important is this task?\nWanna add any assignee?\ny', *collaborators) # Choosing one collaborator as the assignee of the task
            task.addAssignee(project.getCollaborators()[choice])
        want_to_add_description = Confirm.ask('Wanna add any description?')
        if want_to_add_description:
            description = Prompt.ask('Write a description for your task: ')
            task.setDescription(description)
        project.addTask(task, user)
        console.print(f'Task created in {pr.Status(status).name}.', justify="center")
        GF.prompt()
        your_account_page(user)
