import json
number=input("Please enter a favorite number: ")
filename='number.json'
with open(filename,'w') as file_object:
    json.dump(number,file_object)


import json
filename='number.json'
with open(filename) as file_object:
    number=json.load(file_object)

print("I know your favorite number!It's " + number + " .")
