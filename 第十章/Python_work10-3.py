filename='guest.txt'
with open(filename,'w') as file_object:
    message=input("Please input your name: ")
    file_object.write(message)
