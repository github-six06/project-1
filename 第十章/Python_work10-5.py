filename='reason.txt'
while True:
    message=input("Please input the reason why you like to learn programming: ")
    if message=='quit':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(message + '\n')
    
