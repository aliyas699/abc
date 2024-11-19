# 11. Check if a given number is a multiple of both 3 and 5.

num = int(input("Enter the Number: "))

if num % 3 == 0 and num % 5 == 0:
    print(num, "mutiple both 3 and 5")
else:
    print(num, "not mutiple both 3 and 5")