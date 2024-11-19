# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1 = int(input("Enter the Number: "))
opt = input("Enter the Operator: ")
num2 = int(input("Enter the Number: "))

if opt == "+":
    print(num1 + num2)
elif opt == "-":
    print(num1 - num2)
elif opt == "*":
    print(num1 * num2)
elif opt == "/":
    print(num1 / num2)
else:
    print(f"{opt} is invalid operator")