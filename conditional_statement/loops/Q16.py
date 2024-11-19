# 16. Create a program to calculate the sum of the digits of an inputted integer.

number = int(input("Enter an integer: "))
sum = 0

while number > 0:
    digit = number % 10  # Extract the last digit
    sum += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit

print("Sum of the digits:", sum)