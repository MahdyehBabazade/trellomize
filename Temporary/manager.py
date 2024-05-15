import argparse

def create_admin(username, password):
    print(f"Username: {username}, Password: {password}")

def purge_data():
    confirmation = input("Are you sure you want to purge all data? This action cannot be undone. (yes/no): ")
    if confirmation.lower() == 'yes':
        print("Purging all data...")
        pass
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
            create_admin(args.username, args.password)
        else:
            print('You should provide both username and password.')
    elif args.command == 'purge-data':
        purge_data()
    else:
        print("Invalid command. Use 'create-admin' or 'purge-data'.")

if __name__ == "__main__":
    execute_command()
