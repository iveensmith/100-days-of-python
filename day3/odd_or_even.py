# This program works out is a number is odd or even
# an odd number is a number that cannot be divided by 2 without a remainder
# an even number has no remainder when divided by 2

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")