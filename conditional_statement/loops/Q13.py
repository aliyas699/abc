# 13. Use nested loops to print a pyramid pattern of *.

row = 4
for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
        