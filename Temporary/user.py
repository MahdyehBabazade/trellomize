import json
import hashlib
import os

class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = hashing(password)
        
    def set_username(self, username):
        self.username = username
    
    def set_password(self, password):
        self.password = hashing(password)
    
    def set_email(self, email):
        self.email = email
    
    def delete_account(self, username):
        filename = f"AllFiles.Users/{username}.json"
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise FileNotFoundError(f"User {username} does not exist.")
    
    def build_project(self):
        pass

def save_to_file(user):
    directory = "AllFiles\\Users"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = os.path.join(directory, f"{user.email}.json")
    with open(filename, "w") as f:
        json.dump(user.__dict__, f, indent=4)

def hashing(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()


def email_isvalid(email):
    output = False
    try:
        if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
            raise ValueError('Invalid email!')
        else:
            output = True
    except ValueError as error:
        raise ValueError(str(error))
    return output

def username_isvalid(username):
    output = False
    try:
        if len(username) == 0:
            raise ValueError('Invalid username')
        else:
            output = True
    except ValueError as error:
        raise ValueError(str(error))
    return output

def password_isvalid(password):    
    output = False
    try:
        if len(password) < 8:
            raise ValueError('Password must have at least 8 characters!')
        else:
            output = True
    except ValueError as error:
        raise ValueError(str(error))
    return output
    
def sign_up(email, username, password):
    user = User(email, username, password)
    save_to_file(user)

def correct_password(username , password):
    filename = f"AllFiles.Users/{username}.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        my_password = data.get("password")
        try:
            if not my_password:
                raise KeyError("Password not found in user data.")
        except KeyError as error:
            raise KeyError(str(error))
        return hashing(password) == my_password

def correct_username(username): 
    dir = os.path.join("AllFiles.Users", f"{username}.json")
    if not os.path.exists(dir):
        return False
    return True

def login(username, password):
    with open(f"AllFiles.Users/{username}.json" , "r") as file: #it does not find direction
        data = json.load(file)
        try:
            if correct_username(username):
                if correct_password(username, password):
                    return True
                else:
                    raise Exception('Incorrect Password!')
            else:
                raise Exception('User not found!')
        except Exception as error:
            raise Exception(str(error))
