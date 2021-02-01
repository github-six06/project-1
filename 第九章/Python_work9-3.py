class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print("The user's name is" + self.first_name + " " +self.last_name)
    def greet_user(self):
        print("You are welcome,my friend.")
the_user1=User('Bai','Li')
the_user2=User('Fu','Du')
the_user1.describe_user()
the_user1.greet_user()
the_user2.describe_user()
the_user2.greet_user()

        
        
        
