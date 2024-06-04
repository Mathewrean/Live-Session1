def even():
    Inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 35]
    for i in Inputs:
        if (i % 2) == 0:
            print("These are the even numbers: ", ''.join([i]))
        else:
            print("These are the odd numbers: ", ''.join(i))


even()
