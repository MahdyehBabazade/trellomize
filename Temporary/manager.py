import argparse

def create_admin(username, password):
    print(f"Username: {username}, Password: {password}")
    
def execute_command():
    parser = argparse.ArgumentParser(description='Create an Admin')
    subparser = parser.add_subparsers(dest='command', help='sub-command help')
    create_admin_parser = subparser.add_parser('create-admin', help='Create admin user')
    create_admin_parser.add_argument('--username', type=str, required=True,  help='The username of the admin')
    create_admin_parser.add_argument('--password', type=str, required=True, help='The password of the admin')
    args = parser.parse_args()
    if args.command == 'create-admin':
        if args.username and args.password:
            create_admin(args.username, args.password)
        else:
            print('You should provide both username and password.')
    else:
        print("Invalid command. Use 'create-admin'.")
if __name__ == "__main__":
    execute_command()