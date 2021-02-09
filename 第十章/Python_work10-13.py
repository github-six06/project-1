import json
def get_sorted_username():
    filename='username.json'
    with open(filename) as file_object:
        username=json.load(file_object)
        msg=("Your name is " + username + " ,isn't it ?")
        msg+=("(If correct,enter'y',else enter'n'.)")
        msg=input(msg)
    if msg=='y':
        return username
    else:
        return None
def get_new_username():
    username=input("What is your name? ")
    filename='username.json'
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
    return username
def greet_user():
    username=get_sorted_username()
    if username:
        print("Welcome back, " + username + " !")
    else:
        username=get_new_username()
        print("We'll remember you when you come back," + username + " !")

greet_user()
            
