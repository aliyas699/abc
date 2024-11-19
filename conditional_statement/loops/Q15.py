# 15. Print the sum of even and odd numbers separately up to a given number.
even_num = []
odd_num = []
for i in range(10):
    num = int(input("Enter the Number: "))
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
print(f"Sum of Even Number {sum(even_num)}")
print(f"Sum of Odd Number {sum(odd_num)}")