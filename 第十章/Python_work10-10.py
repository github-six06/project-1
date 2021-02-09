filename='story.txt'
try:
    with open(filename) as file_object:
        contents=file_object.read()
except FileNotFoundError:
    print("Sorry,the file" + filename + " dose not exist.")
else:
    word1=contents.count('the')
    word2=contents.lower().count('the')
    print("The file " + filename + " has about " + str(word1) +" 个小写, " + str(word2) + " 个大小写.")
    
