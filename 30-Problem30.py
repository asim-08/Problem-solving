# Checking if a number is positive, negative or zero using function and Exception handling.
def number_nature(number):
    try:
        number = int(number)
        if number > 0:
            print(f"{number} is a positive number")
        elif number < 0:
            print(f"{number} is a negative number")
        else:
            print(f"It is a {number}")
    except ValueError:
        print("Enter a Valid number")



n = (input("Enter a number : "))


number_nature(n)