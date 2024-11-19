# 20. Create a program that evaluates if an inputted number is prime.


number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not a prime number.")
elif number == 2:
    print(f"{number} is a prime number.")
elif number == 3:
    print(f"{number} is a prime number.")
elif number % 2 == 0:
    print(f"{number} is not a prime number.")
elif number % 3 == 0:
    print(f"{number} is not a prime number.")
elif number % 5 == 0 and number != 5:
    print(f"{number} is not a prime number.")
else:
    print(f"{number} is a prime number.")