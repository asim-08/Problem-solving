# Checking if input is Alphabet or number.
try:
    user_input = input("Enter input : ")
    if user_input.isdigit():
        print(f"{user_input} is a number")
    elif user_input.isalpha():
        print(f"{user_input} is a alphabet")
    else:
        print("Enter valid type please")
except:
    print("It is an invalid type")