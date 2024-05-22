import json
import hashlib
import os

def hashing(password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

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
    
    def get_email(self):
        return self.email
        
    def delete_account(self, username):
        filename = f"AllFiles.Users/{username}.json"
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise FileNotFoundError(f"User {username} does not exist.")
    
    def build_project(self):
        pass


class SignUp:

    def save_to_file(user):
        directory = "AllFiles\\Users"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, f"{user.email}.json")
        with open(filename, "w") as f:
            json.dump(user.__dict__, f, indent=4)

    def email_isvalid(self, email):
        output = False
        try:
            if not (email.endswith('@gmail.com') or email.endswith('@yahoo.com')):
                raise ValueError('Invalid email!')
            else:
                output = True
        except ValueError as error:
            raise ValueError(str(error))
        return output

    def username_isvalid(self, username):
        output = False
        try:
            if len(username) == 0:
                raise ValueError('Invalid username')
            else:
                output = True
        except ValueError as error:
            raise ValueError(str(error))
        return output

    def password_isvalid(self, password):    
        output = False
        try:
            if len(password) < 8:
                raise ValueError('Password must have at least 8 characters!')
            else:
                output = True
        except ValueError as error:
            raise ValueError(str(error)) 
        return output

    def sign_up(self, email, username, password):
        user = User(email, username, password)
        SignUp.save_to_file(user)

class Login:

    def correct_password(self, email , password):
        directory = "AllFiles\\Users"
        filename = os.path.join(directory, f"{email}.json")
        with open(filename, 'r') as file:
            data = json.load(file)
            my_password = data.get("password")
            try:
                if not my_password:
                    raise KeyError("Password not found in user data.")
            except KeyError as error:
                raise KeyError(str(error))
            return hashing(password) == my_password

    def correct_email(self, email): 
        directory = "AllFiles\\Users"
        filename = os.path.join(directory, f"{email}.json")
        if not os.path.exists(filename):
            return False
        return True

    def load(self, email, password):
        directory = "AllFiles\\Users"
        filename = os.path.join(directory, f"{email}.json")
        with open(filename, 'r') as file:
            data = json.load(file)
            login_instance = Login()
            try:
                if login_instance.correct_email(email):
                    if login_instance.correct_password(email, password):
                        return True
                    else:
                        raise ValueError('Incorrect Password!')
                else:
                    raise ValueError('User not found!')
            except ValueError as error:
                raise ValueError(str(error))
