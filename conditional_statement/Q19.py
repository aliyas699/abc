# 19. Check if a string input is uppercase, lowercase, or a mix.

char = input("Enter the String: ")
if char.isupper():
    print(char,"is upper case")
elif char.islower():
    print(char,"is lower case")
else:
    print(char,"is mix case")