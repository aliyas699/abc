# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age = int(input("Enter Your Age: "))

if age < 18:
    print("Your age is ",age , " So your are minor")
elif age >= 18 and age <= 50:
    print("Your age is ",age , " So your are adult")
else:
    print("Your age is ",age , " So your are senior citizen")