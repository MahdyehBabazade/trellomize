import argparse, time, os, shutil, hashlib, json, GlobalFunctions as GF
from rich.console import Console
from rich.prompt import Confirm
from rich.progress import Progress

def hashing(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

class Admin:
    def __init__(self, username, password):
        self.__username = username
        self.__password = hashing(password)
    
    # Setters
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
    admin = Admin(username, password)
    directory = "AllFiles\\Managers"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{admin.getUsername()}.json")  #files works with email not username
    while True:
        try:
            if os.path.exists(filename):
                raise FileExistsError('Admin Already Exists!! Try Another Username.')
            else:
                with open(filename, "w") as f:
                    json.dump(admin.to_dict(), f, indent=4)
                break
        except FileExistsError as error:
            console = Console()
            console.print(str(error), style='bold red')            
    

def purge_data():
    wante_to_purge_data = Confirm.ask("Are you sure you want to purge all data? This action cannot be undone.: ")
    if wante_to_purge_data:
        directory = "AllFiles\\Users"
        if os.path.exists(directory):
            progress = Progress()
            task = progress.add_task("Purging all data...", total=100)
            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(0.05)
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
    purge_data_parser = subparser.add_parser('purge-data', help='Purge all data')
    args = parser.parse_args()
    
    if args.command == 'create-admin':
        if args.username and args.password:
            manager_signup(args.username, args.password)
        else:
            print('You should provide both username and password.')
    elif args.command == 'purge-data':
        purge_data()
    else:
        print("Invalid command. Use 'create-admin' or 'purge-data'.")

if __name__ == "__main__":
    execute_command()