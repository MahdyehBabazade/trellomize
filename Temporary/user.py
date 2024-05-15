import argparse
#import Temporary.CreateAdmin as CreateAdmin
import json
import hashlib

def hashing(password):
    sha256 = hashlib.sha256()
    sha256.update(password)
    return sha256.hexdigest()

def SignUp(email, username, password):
    def check():
        isValid = True
        for i in range(len(email)):
            if email[i]=='@':
                if email[i:]!='gmail.com' or email[i:]!='yahoo.com' or i == 0:
                    isValid = False
                    break

        if not isValid:
            raise Exception('Invalid Email.')
        elif len(username) == 0 :
            isValid = False
            raise Exception('Enter username!!')      #elif for  step by step error (Email ->  Username -> Password)
        elif len(password) < 8:
            isValid = False
            raise Exception('Password must be 8 or more characters.')
        return isValid
    
    if check():
            with open('AllFiles.users', 'a') as file: #this is for appending in file we can not read email in file , fix it
                if email in json.load(file) or username in json.load(file):
                    raise Exception('This email or username exist. Try another one or use Login if you have already signed up.')
                else:
                    file.append(json.dumps({"Email":email, "Username":username, "Password":hashing(password)}))
        
def log_in(email , username , password):
    def check(username , password):
        with open('AllFiles.users', 'r') as file:
            if username in json.load(file):
                correct_password = json.load(file)[username]["Password"]
                this_password = hashing(password)
                if this_password == correct_password:
                    pass
                    #constructor
                else:
                    raise Exception('Invalid password!!')
            else:
                raise Exception('Invalid username!!')
                
