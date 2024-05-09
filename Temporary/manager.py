import argparse
import Temporary.CreateAdmin as CreateAdmin
import json
import hashlib

#def create_admin(username, password):
#    print(f"Username: {username}, Password: {password}")
#   
def hashing(password):
    sha256 = hashlib.sha256()
    sha256.update(password)
    return sha256.hexdigest()

def SignUp(email, usename, password):
    def check(email, username):
        isValid = True
        for i in range(len(email)):
            if email[i]=='@':
                if email[i:]!='gmail.com' or email[i:]!='yahoo.com' or i == 0:
                    isValid = False
                    break

        if not isValid:
            raise Exception('Invalid Email.')
        elif len(username) == 0:
            isValid = False
            raise Exception('Enter username!!')
        elif len(password) < 8:
            isValid = False
            raise Exception('Password must be 8 or more characters.')
           
        if isValid:
            with open('AllFiles.users', 'a') as file:
                if email in file or username in file:
                    raise Exception('This email or username exist. Try another one or use Login.')
                else:
                    file.append(json.dumps({"Email":email, "Username":username, "Password":hashing(password)}))
        

def execute_command():
    parser = argparse.ArgumentParser(description='Create an Admin')
    subparser = parser.add_subparsers(dest='command', help='sub-command help')
    create_admin_parser = subparser.add_parser('create-admin', help='Create admin user')
    create_admin_parser.add_argument('--username', type=str, required=True,  help='The username of the admin')
    create_admin_parser.add_argument('--password', type=str, required=True, help='The password of the admin')
    args = parser.parse_args()
    if args.command == 'create-admin':
        if args.username and args.password:
            SignUp(args.username, args.password)
        else:
            print('You should provide both username and password.')
    else:
        print("Invalid command. Use 'create-admin'.")
if __name__ == "__main__":
    execute_command()