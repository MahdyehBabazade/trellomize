import os, json, GlobalFunctions as GF #, ProjectDisplay as PD
from rich.console import Console
import user as userlib
import projects as pr, time, sys
from rich.prompt import Prompt, Confirm
import os, uuid
from rich.text import Text

def menu():
    choice = GF.choose_by_key_with_kwargs(("\n[bold italic]TRELLOMIZE[/]\n[grey70]Transform your project management experience with our innovative platform,\noffering streamlined coordination, real-time updates, and effective task management.[/]\n"), SIGNUP = "[grey70]for free![/]", LOGIN = "[grey70]if you already have an account[/]")
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
    log_user = GF.log_actions(user)
    log_user.info("user signed up")
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
            console.print("[bold purple4]Enter your email: [/]")
            console.print(email)
            console.print("[bold purple4]Enter your password: [/]")
            password = input()

    user = login_sys.load(email, password)
    if user.getIsActive():
        your_account_page(user)
    else:
        console.print("Sorry, but your account has be deactivated by the system manager.")
        GF.prompt()
        menu()
    log_user = GF.log_actions(user)
    log_user.info("user logged in")

            
def your_account_page(user):
    os.system('cls')
    choice = GF.choose_by_key("[bold italic white]\nI want to ...\n", "create a new project.", "see my projects.", "go to the setting.", "logout from my account.")
    if choice == 0:
        new_project_page(user)
    elif choice == 1:
        load_projects_page(user)
    elif choice == 2:
        setting(user)
    elif choice == 3:
        logout_page(user)
        
def new_project_page(user): #COMPLETEDDDDDDDD
    log_user = GF.log_actions(user)
    os.system('cls')
    console = Console()
    console.print(f"{user.getUsername()}")
    console.print("[grey70]Enter a title for your project: ")
    title = input()
    my_project = pr.Project(title, user)
    my_project.save_to_file(user)
    while True:
        want_collab =Prompt.ask("Wanna add any collaborators? (y/n)")
        if want_collab == "y":
            login_sys = userlib.Login()
            if user.getEmail() == my_project.getLeader().getEmail():
                console.print("Enter the collabrator's email: ", style="bold purple4")
                email = input()
                for attempt in range(5):
                    try:
                        if login_sys.correct_email(email):
                            break
                    except ValueError as error:
                        log_user.warning(f"user takes value error while adding collab to {title} project")
                        os.system('cls')
                        console.print(error, style="red")
                        console.print("[bold purple4]Enter the email: [/]")
                        email = input()
                    except FileExistsError as error:
                        log_user.warning(f"user takes file exist error while adding collab to {title} project")
                        os.system('cls')
                        console.print(error, style="red")
                        console.print("[bold purple4]Enter the email: [/]")
                        email = input()
                filename = os.path.join("AllFiles/Users", f"{email}.json")
                with open(filename, 'r') as file:
                    data = json.load(file)
                username = data.get("username")
                password = data.get("password")
                new_collaborator = userlib.User(email , username , password, True)
                my_project.save_to_file(new_collaborator)
                my_project.addCollaborator(new_collaborator)
                console.print("[bold purple4]You have successfully added a new collaborator")
                log_user.info(f"user added a new collaborator by email {email} to {title} project")
                GF.prompt()
        elif want_collab == "n":
            break
        else:
            console.print("invalid letter!", style="red")
    choice = GF.choose_by_key_with_kwargs(Text(title, justify="center"), BACKLOG='', TODO='', DOING='', DONE='', ARCHIVED='')
    task_page_by_status(user, my_project, choice+1)
    log_user.info(f"user created a new project by title {title} successfully")

def load_projects_page(user):
    console = Console()
    data = GF.load_the_data(user.getEmail())
    if "projects" not in data:
        os.system('cls')
        console.print("No projects ever created. Try creating one." , style="red")
        GF.prompt()
        your_account_page(user)
    else:
        title_list = []
        projectID_list = []
        for word in data["projects"].values():
            title_list.append(word["title"])
            projectID_list.append(word["ProjectID"])
        title_list.append("Back")
        while True:
            choice = GF.choose_by_key("[bold italic white]\nWhich one of your projects..?" , *title_list)
            if choice == len(title_list) - 1:
                your_account_page(user)
                return
            project_title = title_list[choice]
            project_id = projectID_list[choice]
            project = pr.load_from_file(project_id, user)
            
            while True:
                choice = GF.choose_by_key(f"[bold italic white]\nWhat do you want to do with {project_title} project?", "see the project board" , "collaborators" , "setting of project" , "Back")
                if choice == 0:
                    backlogs = ""
                    for task in project.getTasks():
                        if task.getStatus() == 1:
                            backlogs += f"{task.getTitle()}\n"
                    todos = ""
                    for task in project.getTasks():
                        if task.getStatus() == 2:
                            todos += f"{task.getTitle()}\n"
                    doings = ""
                    for task in project.getTasks():
                        if task.getStatus() == 3:
                            doings += f"{task.getTitle()}\n"
                    dones = ""
                    for task in project.getTasks():
                        if task.getStatus() == 4:
                            dones += f"{task.getTitle()}\n"
                    archiveds = ""
                    for task in project.getTasks():
                        if task.getStatus() == 5:
                            archiveds += f"{task.getTitle()}\n"
                    pd_choice = GF.switch_panels(GF.create_layout(project), ["BACKLOG", "TODO", "DOING", "DONE", "ARCHIVED"], [backlogs, todos, doings, dones, archiveds])
                    tasks = [task for task in project.getTasks() if pd_choice + 1 == task.getStatus()]
                    while True:
                        os.system('cls')
                        tasks_title_and_id = [task.getTitle()+' - '+ task.getTaskID() for task in tasks]
                        tasks_title_and_id.insert(0, "+ Add a task on this project")
                        tasks_title_and_id.append("Back")
                        #while True:
                        choice = GF.choose_by_key("", *tasks_title_and_id)
                        if choice == len(tasks_title_and_id) - 1: 
                            break
                        elif choice == 0: #want to add task
                            task_page_by_status(user, project, tasks[choice - 1].getStatus())
                        else:
                            task = tasks[choice-1]
                            choice = GF.choose_by_key(f"[bold italic white]Choose what you want to do to {task.getTitle()} tasks:", "remove task", "change title", "change the status", "change its priority", "change the description", "comments", "assignees")
                            if user.getEmail() in [assignee.getEmail() for assignee in task.getAssignees()] or user.getEmail() == project.getLeader().getEmail():
                                if choice == 0: # remove task
                                    want_to_remove = Confirm.ask("Are you sure you want to remove this task?")
                                    if want_to_remove:
                                        project.removeTask(task)
                                        console.print('Task successfully deleted.')
                                        log_user.info(f"user remove {task.getTitle()} task from {project_title} project")
                                elif choice == 1: # change title
                                    console.print(f"This tasks' title: {task.getTitle()}\nEnter the new title: ")
                                    task.changeTitle(input())
                                    console.print("[green]Title successfullly changed.")
                                    log_user.info(f"user changed {task.getTitle()} title from {project_title} project")
                                elif choice == 2: # change the status
                                    choice = GF.choose_by_key(f"This task's status: {pr.Status(task.getStatus()).name}\nI want to move this task to the: ", "BACKLOG", "TODO", "DOING", "DONE", "ARCHIEVED")
                                    task.changeStatus(pr.Status(choice+1).value)
                                    console.print("[green]Status successfullly changed.")
                                    log_user.info(f"user changed {task.getTitle()} status from {project_title} project")
                                elif choice == 3: # change the priority
                                    choice = GF.choose_by_key(f"This tasks' priority: {pr.Priority(task.getStatus()).name}\nChange its priority to:", "LOW", "MEDIUM", "HIGH", "CRITICAL")
                                    task.changePriority(pr.Priority(choice+1).value)
                                    console.print("[green]Priority successfullly changed.")
                                    log_user.info(f"user changed {task.getTitle()} priority from {project_title} project")
                                elif choice == 4: # change the description
                                    console.print(f"This tasks' description: {task.getDescription()}\nWrite the new description here:")
                                    task.changeDescription(input())
                                    console.print("[green]Description successfullly changed.")
                                    log_user.info(f"user changed {task.getTitle()} description from {project_title} project")
                                elif choice == 5: # comments
                                    comments = [f'{cm.getPerson().getUsername()}: {cm.getText()}\n' for cm in task.getComments()]
                                    comments.insert(0, "+ Add a comment on this task\n")
                                    choice = GF.normal_choose("", "+ Add a comment on this task\n", *comments)
                                    if choice == 0:
                                        console.print('Write your comment below here:')
                                        print(f'{user.getUsername()}:')
                                        comment = pr.Comment(input(), user)
                                        task.addComment(comment)
                                        console.print("[green]Comment successfully added.")
                                        log_user.info(f"user added comment to {task.getTitle()} task from {project_title} project")
                                    else:
                                        comment = task.getComments()[choice-1]
                                        if task.getComments()[choice].getPerson().getEmail() == user.getEmail(): # This conditition checks if the user is the writer of this comment
                                            choice1 = GF.choose_by_key("Want do you want to do with this comment?", "edit the comment", "remove the comment")
                                            if choice1 == 0:
                                                comment = pr.Comment()
                                                console.print(f'Current comment text: {task.getComments()[choice].getText()}\nEnter the new text for this comment: ')
                                                # بقیه اش کو؟
                                                log_user.info(f"user edited a comment from {task.getTitle()} task from {project_title} project")
                                            if choice1 == 1:
                                                want_to_remove = Confirm.ask("Are you sure you want to remove this comment?")
                                                if want_to_remove:
                                                    task.deleteComment(task.getComments()[choice])
                                                log_user.info(f"user remove a comment from {task.getTitle()} task from {project_title} project")
                                        else:
                                            console.print(f'The text of the comment: {task.getComments()[choice].getText()}\nWho posted it: {task.getComments()[choice].getPerson().getUsername()} ({task.getComments()[choice].getPerson().getEmail()})')
                                elif choice == 6: #assignees
                                    assignees = [f'{assi.getUsername()} - {assi.getEmail()}' for assi in task.getAssignees()]
                                    if user.getEmail() == project.getLeader().getEmail():  # this had error project.getProject? and still have error
                                        choice = GF.choose_by_key("", "+ Add an assignee for this task", *assignees)
                                        if choice == 0:
                                            console.print('Write the email of the assignee you want to add: ')
                                            assi_email = input()
                                            while True:
                                                filename = os.path.join("AllFiles\\Users", f"{assi_email}.json")
                                                if not os.path.exists(filename):
                                                    console.print('User does not exist! Try another one: ')
                                                    assi_email = input()
                                                    log_user.warning(f"user takes an file not exist error while adding assignees from {task.getTitle()} task from {project_title} project")
                                                else:
                                                    project.addCollaborator(userlib.User(assi_email, GF.load_the_data(assi_email)["username"], GF.load_the_data(assi_email)["password"], True))
                                                    console.print("[green]Assignee added to the task")
                                                    log_user.info(f"user add a assignee from {task.getTitle()} task from {project_title} project")
                                    else:
                                        assignees = [f'{assi.getUsername()} - {assi.getEmail()}' for assi in task.getAssignees()]
                                        for assignee in assignees:
                                            console.print(assignee)
                                GF.prompt()
                            else:
                                console.print("You don't have access to this. You aren't an assignee of this task!")
                                log_user.warning(f"user takes an error you are not available to add assignees to {task.getTitle()} task from {project_title} project")
                                break
                elif choice == 1: #collab
                    os.system('cls')
                    while True:
                        choice = GF.choose_by_key("[bold italic white]\nWhat do you want to do with collaborators?" , "see collaborators" , "add collaborator" , "remove collaborator" , "Back")
                        if choice == 0: # See collabs
                            os.system('cls')
                            collab_emails = [collab.getEmail() for collab in project.getCollaborators()]
                            collaborators = GF.load_the_collaborators_data(*collab_emails)
                            console.print("[bold italic white]\nHere you can see the collaborators...")
                            for i in range(len(collaborators)):
                                console.print(f"{i+1}. [bold purple4]{collaborators[i]["username"]} - {collaborators[i]["email"]}")
                            GF.prompt()
                        elif choice == 1: #add collab
                            os.system('cls')
                            console = Console()
                            login_sys = userlib.Login()
                            if user.getEmail() == project.getLeader().getEmail():
                                console.print("Enter the collabrator's email: ", style="bold purple4")
                                email = input()
                                for attempt in range(5):
                                    try:
                                        if login_sys.correct_email(email):
                                            filename = os.path.join("AllFiles/Users", f"{email}.json")
                                            with open(filename, 'r') as file:
                                                data = json.load(file)
                                            username = data.get("username")
                                            password = data.get("password")
                                            new_collaborator = userlib.User(email , username , password, True)
                                            project.save_to_file(new_collaborator)
                                            project.addCollaborator(new_collaborator)
                                            console.print("[bold purple4]You have successfully added a new collaborator")
                                            log_user.info(f"user added a new collaborator by email {email} to {title} project")
                                            GF.prompt()
                                            break
                                    except ValueError as error:
                                        log_user.warning(f"user takes value error while adding collab to {title} project")
                                        os.system('cls')
                                        console.print(error, style="red")
                                        console.print("[bold purple4]Enter the email: [/]")
                                        email = input()
                                    except FileExistsError as error:
                                        log_user.warning(f"user takes file exists error while adding collab to {title} project")
                                        os.system('cls')
                                        console.print(error, style="red")
                                        console.print("[bold purple4]Enter the email: [/]")
                                        email = input()
                            else:
                                console.print("You are not the leader. You cannot add anyone to the project")
                                log_user.warning(f"user takes an error you are not available to add collab to {project_title} project")
                                break
                        elif choice == 2: #remove collab
                            os.system('cls')
                            if user.getEmail() == project.getLeader().getEmail():
                                collab_emails = [collab.getEmail() for collab in project.getCollaborators()]
                                collab_emails.append("Back")
                                choice = GF.normal_choose("[bold italic white]\nWhich one of the collaborators do you want to remove from the project?", *collab_emails)
                                print(choice)
                                if choice == len(collab_emails)-1:
                                    break
                                else:
                                    if choice != 0:
                                        collab = project.getCollaborators()[choice]
                                        project.removeCollaborator(collab)
                                        project.remove_from_file(collab) #بعلاوه یک میکنیم چون نمیخوایم خود لیدر هم حساب بشه
                                        console.print("[bold purple4]You have successfully removed a collaborator")
                                        log_user.info(f"user has removed a collab from {project_title} project")
                                    else:
                                        console.print("You can't remove yourself from your own project!")
                            else:
                                console.print("You are not the leader. You cannot remove anyone from the project")
                                log_user.warning(f"user takes an error that you are not availabe to remove anyone from {project_title} project")
                                break
                        elif choice == 3:
                            break
                elif choice == 2: #setting
                    os.system('cls')
                    while True:
                        choice = GF.choose_by_key("[bold italic white]\nWhat do you want to do?" , "see information" , "Change information" , "Back")
                        if choice == 0:
                            os.system('cls')
                            console.print("[bold italic white]\nHere is the project information :")
                            console.print(f"[bold purple4]Title : {project.getTitle()}")
                            console.print(f"[bold purple4]Id : {project.getProjectID()}")
                            leader = project.getLeader()
                            console.print(f"[bold purple4]Leader : {leader.getEmail()}")
                            GF.prompt()
                        elif choice == 1:
                            os.system('cls')
                            while True:
                                choice4 = GF.choose_by_key("[bold italic white]\nWhat do you want to change?" , "Title" , "Id" , "Back")
                                if choice4 == 0:
                                    os.system('cls')
                                    console.print("[bold italic white]\nEnter your new title :")
                                    new_title = input()
                                    project.changeTitle(new_title)
                                    console.print("[bold purple4]Your title has been successfully changed!")
                                    log_user.info(f"user has changed {project_title} project's title")
                                    GF.prompt()
                                elif choice4 == 1:
                                    os.system('cls')
                                    new_id = input("[bold italic white]\nEnter your new id :")
                                    project.changeProjectId(new_id)
                                    console.print("[bold purple4]Your id has been successfully changed!")
                                    log_user.info(f"user has changed {project_title} project's id")
                                    GF.prompt()
                                elif choice4 == 2:
                                    os.system('cls')
                                    break
                        elif choice == 2:
                            os.system('cls')
                            break
                elif choice == 3:
                    os.system('cls')
                    break

def setting(user):
    log_user = GF.log_actions(user)
    choice = GF.choose_by_key("What do you want to do?" , "edit my profile" , "logout" , "Back")
    if choice == 0:
        os.system('cls')
        console = Console()
        console.print("[bold purple4]We want to be sure it's your account, please enter your password.")
        password = input()
        while True:
            try:
                if user.getPassword() == userlib.hashing(password):
                    break
            except:
                os.system('cls')
                log_user.warning("user takes invalid password error while editing profile in setting")
                console.print("Invalid password"+"\n", style="bold red")
                console.print("Try again: ")
                console.print("[bold purple4]Enter your password: [/]")
                password = input()
        while True:
            choice = GF.choose_by_key('What do you want to change?' , 'My username' , 'My password' , 'Back')
            if choice == 0:
                os.system('cls')
                console.print("[bold purple4]Enter your new username.")
                new_username = input()
                user.changeUsername(new_username)
                os.system('cls')
                console.print("\n[bold purple4]Your username has been changed successfully!")
                log_user.info(f"user has changed his/her username")
                GF.prompt()
                setting(user)
            elif choice == 1:
                os.system('cls')
                console.print("[bold purple4]Enter your new password.")
                new_password = userlib.hashing(input())
                user.changePassword(new_password)
                os.system('cls')
                console.print("\n[bold purple4]Your password has been changed successfully!")
                log_user.info(f"user has changed his/her password")
                GF.prompt()
                setting(user)
            elif choice == 2:
                os.system('cls')
                break

    elif choice == 1:
        logout_page(user)
            
    elif choice == 2:
        os.system('cls')
        your_account_page(user)


def logout_page(user):
    log_user = GF.log_actions(user)
    choice = GF.choose_by_key('Are you sure?' , 'Yes' , 'No')
    if choice == 0:
        console = Console()
        console.print('You log out successfully.')
        log_user.info("user logged out")
        GF.prompt()
        menu()
    elif choice == 1:
        your_account_page(user)

def task_page(user, project):
    log_user = GF.log_actions(user)
    os.system('cls')
    console = Console()
    console.print('Enter a title for your task: ')
    title = input()
    status = pr.Status[Prompt.ask("What is the status of this task?", choices=["BACKLOG", "TODO", "DOING", "DONE", "ARCHIVED", "DEFAULT"])].value
    priority = pr.Priority[Prompt.ask('How important is this task to you', choices=["LOW", "MEDIUM", "HIGH", "CRITICAL", "DEFAULT"])].value
    task = pr.Task(title, project, status, priority)
    project.addTask(task)
    want_to_add_assignee = Confirm.ask('Wanna add any assignee?')        
    if want_to_add_assignee:
        console.print('Choose the assignee: ')
        collaborators = [collab.getUsername() for collab in project.getCollaborators()]
        choice = GF.choose_by_key("", *collaborators) # Choosing one collaborator as the assignee of the task
        task.addAssignee(project.getCollaborators()[choice])
    want_to_add_description = Confirm.ask('Wanna add any description?')
    if want_to_add_description:
        description = Prompt.ask('Write a description for your task')
        task.changeDescription(description)
    console.print(f'Task created in {pr.Status(status).name}', justify="center")
    log_user.info(f" user created {task.getTitle()} task to {project.getTitle()} project")
    GF.prompt()
    your_account_page(user)

def task_page_by_status(user, project, status=pr.Status.BACKLOG): # COMPLETEDDDDDDDDD
    log_user = GF.log_actions(user)
    os.system('cls')
    console = Console()
    os.system('cls')
    console.print('Enter a title for your task: ')
    title = input()
    os.system('cls')
    priority = pr.Priority[Prompt.ask('How important is this task to you', choices=["LOW", "MEDIUM", "HIGH", "CRITICAL", "DEFAULT"])].value
    task = pr.Task(title, project, status, priority)
    project.addTask(task)
    want_to_add_assignee = Confirm.ask('Wanna add any assignee?')        
    if want_to_add_assignee:
        console.print('Choose the assignee: ')
        collaborators = [collab.getUsername() for collab in project.getCollaborators()]
        choice = GF.choose_by_key('Enter a title for you task:\n'+title+'\nHow important is this task?\nWanna add any assignee?\ny', *collaborators) # Choosing one collaborator as the assignee of the task
        task.addAssignee(project.getCollaborators()[choice])
    want_to_add_description = Confirm.ask('Wanna add any description?')
    if want_to_add_description:
        description = Prompt.ask('Write a description for your task: ')
        task.changeDescription(description)
    console.print(f'Task created in {pr.Status(status).name}.', justify="center")
    log_user.info(f" user created {task.getTitle()} task to {project.getTitle()} project")
    GF.prompt()
    your_account_page(user)

def change_task_info():
    pass
