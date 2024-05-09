import manager
class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    def SignUp():
        manager.execute_command()
    def Login():
    def check_email(email):
        isChecked =True
        for i in range(len(email)):
            if email[i]=='@':
                if email[i:]!='gmail.com' or email[i:]!='yahoo.com':
                    isChecked = False
                    break
        if not isChecked:
            raise Exception('Invalid Email')
