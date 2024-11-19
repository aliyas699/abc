# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

tem = int(input("Enter the temperature in Celsius: "))

if tem <= 0:
    print(f"{tem}°C is freezing")
elif tem >= 1 and tem <= 30:
    print(f"{tem}°C is moderate")
else:
    print(f"{tem}°C is hot")