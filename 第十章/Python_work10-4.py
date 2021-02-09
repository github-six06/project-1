filename='guest_book.txt'
while True:
        message=input("Please input your name: ")
        if message=='quit':
            break
        else:
            with open(filename,'w') as file_object:
                file_object.write(message + '\n')
                file_object.write("Welcome," + message + '\n')
