import json
filename='number.json'
try:
    with open(filename) as file_object:
        number=json.load(file_object)
except FileNotFoundError:
    number=input("Please enter a favorite number: ")
    with open(filename,'w') as file_object:
            json.dump(number,file_object)
else:
    print("I know your favorite number!It's " + number + " .")
