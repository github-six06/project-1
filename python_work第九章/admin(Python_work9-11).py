class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print("The user's name is" + self.first_name + " " +self.last_name)
    def greet_user(self):
        print("You are welcome,my friend.")

class Privileges():
    def __init__(self):
       self.privileges=['can add post,can delete post,can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print("The restrictions of the administrator are " + privilege + ".")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()


