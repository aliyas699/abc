# 8. Create a program that checks if a given string is a palindrome.

str = "PakistanatsikaP"

if str == str[::-1]:
    print(str, "is palindrome")
else:
    print(str, "isn't palindrome")