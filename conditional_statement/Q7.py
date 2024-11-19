# 7. Write a program to find the largest of three numbers.
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
num3 = int(input("Enter the third Number: "))

if num1 > num2 and num1 > num3:
    print(num1, "is largest from", num2,"and",num3)
elif num2 > num1 and num2 > num3:
    print(num2, "is largest from", num1,"and",num3)
elif num3 > num1 and num3 > num2:
    print(num3, "is largest from", num1,"and",num2)
elif num1 == num2 and num1 > num3:
    print(num1,"and",num2, "is largest than", num3)
elif num1 == num3 and num1 > num2:
    print(num1,"and",num3, "is largest than", num2)
else:
    print(num2,"and",num3, "is largest than", num1)
        