import random

while True:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+=|':;<,>.?/"

    all_chars = lower + upper + numbers + symbols
    length = int(input("Enter the length of your password: "))

    password = ''.join(random.sample(all_chars, length))
    print("Your Password is: ", password)
