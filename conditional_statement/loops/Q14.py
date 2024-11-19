# 14. Write a program that breaks the loop when a certain condition is met.

while True:
    num = int(input("Enter the Number: "))  # Enter 56 to stop Loop
    if num == 56:
        print("Loop Complete")
        break
    print(f"You Entered: {num}")