
class user:
    def __init__(self,firstname,lastname,id,username):
        self.firstname=firstname
        self.lastname=lastname
        self.id=id
        self.username=username
        self.login_attempts=0
        

    def describe_user(self):
       print('firstname: '+self.firstname)
       print('lastname: '+self.lastname)
       print('id: '+str(self.id))
       print('username: '+self.username)

    def greet_user(self):
        print('hello '+self.username)

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

