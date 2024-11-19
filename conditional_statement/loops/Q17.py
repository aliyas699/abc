# 17. Write a program that continues to ask for a number until the correct number is guessed.

correct_num = 56  #Baber number
while True:
    num = int(input("Enter the Number: "))
    if num == correct_num:
        print(f"Congratulations! You guessed it. {correct_num}")
        break
    else:
        print("Try again!")
    
    