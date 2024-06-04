number = int(input("Enter your number to be checked: "))
original = str(number)
reverse = original[::-1]

# reverse = 0
# while (number>0):
#     digits = number % 10
#     reverse = reverse*0 + digits
#     number = number // 10
# print(reverse)
if reverse != original:
    print("It is not a Palindrome")
else:
    print("It is a palindrome")
