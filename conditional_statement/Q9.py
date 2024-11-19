# 9. Take three sides of a triangle as input and check if they form a valid triangle.

a = float(input("Enter the side of a: "))
b = float(input("Enter the side of a: "))
c = float(input("Enter the side of a: "))

if a+b>c and a+c>b and b+c>a:
    print("The sides form a valid triangle.")
else:
    print("The sides don't form a valid triangle.")