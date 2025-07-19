# Checking if a number is positive, negative or Zero.
n = int(input("Enter a number : "))
if n > 0:
    print(f"{n} is a positive number")
elif n < 0:
    print(f"{n} is a negative number")
else:
    print(f"It is a {n}")