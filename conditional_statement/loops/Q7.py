# 7. Find the factorial of a number using a while loop.

num = int(input("Enter the Number: "))
fac = 1
while num > 1:
    fac *= num
    num -= 1
print(fac)