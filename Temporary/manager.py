import argparse
import time
import os, shutil
import hashlib
import json

def hashing(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

class Admin:
    def __init__(self, username, password) -> None:
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
    
def manager_signup(username, password):
    admin = Admin(username, password)
    directory = "AllFiles\\Managers"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, f"{admin.getUsername}.json")  #files works with email not username
    with open(filename, "w") as f:
            json.dump(admin.__dict__, f, indent=4)
    

def purge_data():
    confirmation = input("Are you sure you want to purge all data? This action cannot be undone. (yes/no): ")
    if confirmation.lower() == 'yes':
        print("Purging all data...")
        time.sleep(2)
        directory = "AllFiles\\Users"
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