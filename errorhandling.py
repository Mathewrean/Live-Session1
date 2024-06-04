try:
    f = open("myfile.txt")
    # code that works with the file
except IOError:
    print("Error: Could not find file or read data")