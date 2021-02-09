filename='learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        message=line.replace('Python','C')
        print(message.rstrip())

