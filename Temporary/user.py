import json, GlobalFunctions as GF
import hashlib
import os
from rich.console import Console

def hashing(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

class User:
    def __init__(self, email, username, password, is_hashed=False):
        self.__email = email
        self.__username = username
        # is_hashed falg is used in creating an object of this class when we load a user from a JSON file
        self.__password = password if is_hashed else hashing(password)
        self.__isActive = True
    
    # Change  
    def changeUsername(self, username):
        self.__username = username
        GF.load_the_data(self.__email)['username'] = self.__username
    def changePassword(self, password):
        self.__password = hashing(password)
        GF.load_the_data(self.__email)['password'] = self.__password

    # Getters
    def getEmail(self):
        return self.__email
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password 
    def getIsActive(self):
        return self.__isActive

    # Setters
    def setIsActive(self, activeness):
        self.__isActive = activeness
    # Others
    def to_dict(self):
        return {
            "email": self.__email,
            "username": self.__username,
            "password": self.__password,
            "isActive": self.__isActive
        }
    
    def save_to_file(self):
        directory = "AllFiles\\Users"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, f"{self.__email}.json")
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)


class SignUp:

    def email_isvalid(self, email):
        if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
            raise ValueError('Invalid email!')
        
        directory = "AllFiles\\Users"
        filename = os.path.join(directory, f"{email}.json")
        if os.path.exists(filename):
            raise FileExistsError('Email Already Exists!! Try Another One.')

        return True

    def username_isvalid(self, username):
        if len(username) == 0:
            raise ValueError('Invalid username')
        return True

    def password_isvalid(self, password):    
        if len(password) < 8:
            raise ValueError('Password must have at least 8 characters!')
        return True

    def sign_up(self, email, username, password):
        user = User(email, username, password)
        user.save_to_file()

class Login:

    def correct_password(self, email, password):
        if len(password) < 8:
            raise ValueError('Password must have at least 8 characters!')

        directory = "AllFiles\\Users"
        filename = os.path.join(directory, f"{email}.json")
        with open(filename, 'r') as file:
            data = json.load(file)
            my_password = data.get("password")
            if my_password != hashing(password):
                raise ValueError("Incorrect password.")
        return True

    def correct_email(self, email): 
        if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
            raise ValueError('Invalid email!')
        directory = "AllFiles\\Users"
        filename = os.path.join(directory, f"{email}.json")
        if not os.path.exists(filename):
            raise FileExistsError("This email does not exist.")
        return True
    
    def load(self, email, password):
        filename = os.path.join("AllFiles/Users", f"{email}.json") #change \\ to /
        with open(filename, 'r') as file:
            data = json.load(file)
            username = data.get("username")
            activeness = data["isActive"]
            user = User(email , username , password)
            user.setIsActive(activeness)
        return user
