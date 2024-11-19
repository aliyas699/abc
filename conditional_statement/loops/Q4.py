# 4.Print the multiplication table of a given number.

num = int(input("Enter the Number: "))
i = 1
while i < 11:
    mul = num * i
    print(f"{num} * {i} = {mul}")
    i += 1