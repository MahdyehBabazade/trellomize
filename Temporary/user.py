import json
import hashlib
import os

def hashing(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

class User:
    def __init__(self, email, username, password):
        self.__email = email
        self.__username = username
        self.__password = hashing(password)

    # Setters   
    def setUsername(self, username):
        self.__username = username
    def setPassword(self, password):
        self.__password = hashing(password)
    def setEmail(self, email):
        self.__email = email

    # Getters
    def getEmail(self):
        return self.__email
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password 

    # Others
    def to_dict(self):
        return {
            "email": self.__email,
            "username": self.__username,
            "password": self.__password
        }
    
    def save_to_file(self):
        directory = "AllFiles\\Users"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, f"{self.__email}.json")
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    def delete_account(self, username):
        filename = f"AllFiles.Users/{username}.json"
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise FileNotFoundError(f"User {username} does not exist.")
    
    def build_project(self):
        pass


class SignUp:

    def email_isvalid(self, email):
        if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
            raise ValueError('Invalid email!')
        
        directory = "AllFiles/Users"
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

        directory = "AllFiles/Users"
        filename = os.path.join(directory, f"{email}.json")
        with open(filename, 'r') as file:
            data = json.load(file)
            my_password = data.get("password")
            if my_password != hashing(password):
                raise ValueError("Incorrect password.")
        return True

    def correct_email(self, email): 
        directory = "AllFiles/Users"
        filename = os.path.join(directory, f"{email}.json")
        if not os.path.exists(filename):
            return False
        return True

    def load(self, email, password):
        if self.correct_email(email) and self.correct_password(email, password):
            return True
        return False
