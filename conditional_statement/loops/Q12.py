# 12. Print all prime numbers between 1 and 50.


for num in range(1, 51):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        # Check if the number has any divisors other than 1 and itself
        for i in range(2, num):
            if num % i == 0:
                is_prime = False  # Not a prime number
                break
        if is_prime:
            print(num)