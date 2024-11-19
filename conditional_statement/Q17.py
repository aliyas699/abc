# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

num = int(input("Enter the Number: "))

if num % 2 == 0 and num % 3 == 0:
    print(num,"is divide by both 2 and 3")
elif num % 3 == 0:
    print(num,"is divide by 3")
elif num % 2 == 0:
    print(num,"is divide by 2")
else:
    print(num, "isn't divide by 2 and 3 or both")
    
    