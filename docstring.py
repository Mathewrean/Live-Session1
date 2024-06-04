def odd_even():
    """Our goal with this function is to verify if a number is even or odd"""
    n = [3, 54, 6, 87, 23, 8, 45, 76, 98]
    for i in n:
        if i % 2 == 0:
            print(i, " is even")
        else:
            print(i, " is odd")


print(odd_even.__doc__)     # this is used to print out the doc string text
odd_even()
