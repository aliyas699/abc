# 5. Print all odd numbers between 1 and 100 using a loop.
num = []
for i in range(1,100,2):
    if i % 2 != 0:
        num.append(i)
print(num)