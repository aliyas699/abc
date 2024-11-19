# 2. Use a while loop to print even numbers from 1 to 50.
num = []
i = 1
while i <= 50:
    if i % 2 == 0:
        num.append(i)
    i += 1
print(num)
    