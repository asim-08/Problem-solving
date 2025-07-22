# Checking if character is vowel or consonant.

character = input("Enter a single alphabet character : ")
vowels = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"
if len(character) == 1 and character.isalpha():
    if character.lower() in vowels:
        print(f"{character} is vowel")
    else:
        print(f"{character} is consonant")
else:
    print("Enter a valid character")
