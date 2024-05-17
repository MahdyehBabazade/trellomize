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
    
    filename = os.path.join(directory, f"{user.username}.json")
    with open(filename, "w") as f:
        json.dump(user.__dict__, f, indent=4)

def hashing(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()


def email_isvalid(email):
    if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
        return False
    return True
def username_isvalid(username):
    if len(username) == 0:
        return  False
    return True
def password_isvalid(password):    
    if len(password) < 8:
        return False
    return True
    
def sign_up(email, username, password):
    user = User(email, username, password)
    save_to_file(user)

def correct_password(username , password):
    filename = f"AllFiles.Users/{username}.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        my_password = data.get("password")
        if not my_password:
            raise KeyError("Password not found in user data.")
        return hashing(password) == my_password

def correct_username(username): 
    return os.path.join("AllFiles\\Users", f"{username}.json")

def login(username, password):
    with open(f"AllFiles.Users/{username}.json" , "r") as file: #it does not find direction
        data = json.load(file)
