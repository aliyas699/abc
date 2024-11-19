# 14. Check if a year input by the user is a century year.

year = int(input("Enter the Year Number: "))

if year % 100 == 0:
    print(f"{year} is a Century Year")
else:
    print(f"{year} isn't a Century Year")