# 10. Write a program to determine if a given character is a vowel or consonant.

char = input("Enter the character: ")

if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U":
    print(char, "is a vowel")
else:
    print(char, "is a consonant")