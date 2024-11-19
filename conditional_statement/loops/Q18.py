# 18. Use a loop to print numbers in reverse order within a given range.

start_value = int(input("Enter the starting value: "))
end_value = int(input("Enter the ending value: "))
value = []
for i in range(start_value, end_value+1):
    value.append(i)
    value.sort()
    value.reverse()
print(value)