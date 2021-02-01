class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print("The user's name is" + self.first_name + " " +self.last_name)
    def greet_user(self):
        print("You are welcome,my friend.")
