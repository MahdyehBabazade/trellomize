import argparse
import os
import shutil
import hashlib
import json
import glob
from rich.console import Console
from rich.prompt import Confirm
from rich.progress import Progress
import GlobalFunctions as GF

def hashing(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

class Admin:
    def __init__(self, username, password):
        self.__username = username
        self.__password = hashing(password)
    
    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = hashing(password)
    
    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password
    
    def to_dict(self):
        return {
            'username': self.__username,
            'password': self.__password
        }

def manager_signup(username, password):
    console = Console()
    admin = Admin(username, password)
    directory = "AllFiles/Managers"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{admin.getUsername()}.json")
    try:
        if os.path.exists(filename):
            raise FileExistsError('Admin Already Exists!! Try Another Username.')
    except FileExistsError as error:
        console.print(str(error), style='bold red')
        return
    with open(filename, "w") as f:
        json.dump(admin.to_dict(), f, indent=4)
    choice = GF.choose_by_key("What do you want to do?", "See the list of users")
    if choice == 0:
        show_users()

def show_users():
    dir = "AllFiles/Users"
    users = []
    json_files = glob.glob(os.path.join(dir, '*.json'))
    for file in json_files:
        users.append(os.path.basename(file))
    choice = GF.choose_by_key('Choose the user to see their info', *users)
    user_email = users[choice]
    filename = os.path.join(dir, f"{user_email}")
    with open(filename, 'r') as f:
        data = json.load(f)
    if data['isActive']:
        choice = GF.choose_by_key('This account is active. Press Enter to deactivate it.')
        change_activeness = Confirm.ask('Are you sure?')
        if change_activeness:
            data['isActive'] = False
    else:
        choice = GF.choose_by_key('This account is not active. Press Enter to activate it.', )
        change_activeness = Confirm.ask('Are you sure?')
        if change_activeness:
            data['isActive'] = True
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def manager_login(username, password):
    console = Console()
    directory = "AllFiles/Managers"
    filename = os.path.join(directory, f"{username}.json")
    if not os.path.exists(filename):
        console.print("This username does not exist.", style="bold red")
        return
    if len(password) < 8:
        console.print('Password must have at least 8 characters!', style='bold red')
        return
    with open(filename, 'r') as file:
        data = json.load(file)
    if data.get("password") != hashing(password):
        console.print("Incorrect password.", style="bold red")
        return
    console.print("Login successful!", style="bold green")
    choice = GF.choose_by_key("What do you want to do?", "See the list of users")
    if choice == 0:
        show_users()

def purge_data():
    confirm_purge = Confirm.ask("Are you sure you want to purge all data? This action cannot be undone.")
    if confirm_purge:
        directory = "AllFiles/Users"
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print("All data has been purged.")
    else:
        print("Purge data operation canceled.")

def execute_command():
    parser = argparse.ArgumentParser(description='Admin Management')
    subparser = parser.add_subparsers(dest='command', help='sub-command help')
    
    create_admin_parser = subparser.add_parser('create-admin', help='Create admin user')
    create_admin_parser.add_argument('--username', type=str, required=True, help='The username of the admin')
    create_admin_parser.add_argument('--password', type=str, required=True, help='The password of the admin')
    
    admin_login_parser = subparser.add_parser('admin-login', help='Admin user login')
    admin_login_parser.add_argument('--username', type=str, required=True, help='The username of the admin')
    admin_login_parser.add_argument('--password', type=str, required=True, help='The password of the admin')
    
    purge_data_parser = subparser.add_parser('purge-data', help='Purge all data')
    
    args = parser.parse_args()
    
    if args.command == 'create-admin':
        manager_signup(args.username, args.password)
    elif args.command == "admin-login":
        manager_login(args.username, args.password)
    elif args.command == 'purge-data':
        purge_data()
    else:
        print("Invalid command. Use 'create-admin', 'admin-login' or 'purge-data'.")

if __name__ == "__main__":
    execute_command()
