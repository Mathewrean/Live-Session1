import random

trials = 5
attempts = 0
computer = random.randint(0, 10)

while attempts < trials:
    attempts += 1
    Input: int = int(input("Enter your guess: "))
    if Input == computer:
        print("Congratulations! You have guessed the correct number.\n Computer: ", computer, " You ", Input)
        quit()
    else:
        print("You have guessed a wrong value! Try again.\n Computer: ", computer, " You ", Input)
        chances = trials - attempts
        print("You have ", chances, "chances remaining")

quit()
