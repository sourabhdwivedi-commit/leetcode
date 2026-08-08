from user import user 
class Privileges:

    def __init__(self):
        self.privileges=['can kick','can delete post','can add post',
        'can ban user']
    
    def show_privileges(self):
        
        for i in self.privileges:
            print(i)


class admin(user):
    def __init__(self, firstname, lastname, id, username):
        super().__init__(firstname, lastname, id, username)
        
        self.privileges=Privileges()