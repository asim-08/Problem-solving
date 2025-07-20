# Checking if age is eligible for voting.
try:
    n = int(input("Enter you'r age: "))
    if n > 18:
        print("You are eligible for this vote")
    elif n < 18:
        print("You are not eligible for this vote")
    else:
        ("Please enter a valid number/age")
except(ValueError):
    print("Invalid age")