class User():
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        
    def describe_user(self):
        print("The user's name is" + self.first_name + " " +self.last_name)
        
    def greet_user(self):
        print("You are welcome,my friend.")
        
    def increment_login_attempts(self):
        self.login_attempts+=1
        
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
        
the_user=User('Bai','Li')
the_user.describe_user()
for n in range(4):
    the_user.increment_login_attempts()
print(the_user.login_attempts)
the_user.reset_login_attempts()
print(the_user.login_attempts)


        
        
        
