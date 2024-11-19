# 15. Write a program to check if a number is within a specified range.

num = int(input("Enter the Number: "))
lower = int(input("Enter the Lower Rang: "))
upper = int(input("Enter the Upper Rang: "))

if num >= lower and num <= upper:
    print(f"{num} is between {lower} and {upper}")
else:
    print(f"{num} isn't between {lower} and {upper}")