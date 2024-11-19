# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
len1 = int(input("Enter the first length: "))
len2 = int(input("Enter the second length: "))
len3 = int(input("Enter the third length: "))

if len1 == len2 == len3:
    print("this triangle is equilateral")
elif (len1 == len2 != len3) or (len1 == len3 != len2) or (len2 == len3 != len1):
    print("this triangle is isosceles")
else:
    print("this triangle is scalene")