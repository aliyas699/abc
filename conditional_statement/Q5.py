# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

num = int(input("Enter the Number: "))

if num >= 48 and num <=60:
    print("A grade")
elif num >= 39 and num < 48:
    print("B grade")
elif num >= 31 and num < 39:
    print("C grade")
elif num >= 24 and num < 31:
    print("D grade")
elif num < 24:
    print("F grade")
else:
    print("Please enter valid score")