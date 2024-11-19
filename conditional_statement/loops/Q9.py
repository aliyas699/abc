# 9. Write a program to print the first 10 Fibonacci numbers.

a = 0
b = 1
for i in range(10):
    print(a)
    a,b = b, a+b
    