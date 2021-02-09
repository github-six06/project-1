with open('learning_python.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())



filename='learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())



filename='learning_python.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())



