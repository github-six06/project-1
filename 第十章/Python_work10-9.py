def file(filename):
    try:
        with open(filename) as file_object:
            for line in file_object:
                print(line.rstrip())
    except FileNotFoundError:
        pass
        
filenames=['cats.txt','dogs.txt']
for filename in filenames:
    file(filename)    

