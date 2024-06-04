# creating a new file
from pathlib import Path

Path('file.txt').touch()

open("FILE.txt", 'x')

# opening the file in writing mode
with open('file.txt', 'w') as file_object:
    # adding content to the file
    file_object.write("Writing the \nfirst content \nto the file\n")

# Opening the file in reading mode
file_object = open('file.txt', 'r')
# storing the content in variable
content = file_object.read()
# print the content
print(content)

# Opening the file in reading mode
with open('file.txt', 'r') as file_object:
    # for loop to acces each line
    for line in file_object:
        print(line)