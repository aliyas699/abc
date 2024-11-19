# 1. Write a program that checks if a given number is positive, negative, or zero.

num = int(input("Enter the Number: "))
if num > 0:
    print(num," is a Positve Number")
elif num < 0:
    print(num," is a Negative Number")
else:
    print(num," is a Zero Number")