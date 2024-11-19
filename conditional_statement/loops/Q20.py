# 20. Create a program that simulates a countdown timer starting from a given number down to zero.

start = int(input("Enter the Number: "))

while start >= 0:
    print(start)
    start -= 1  