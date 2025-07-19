# Exception handling.
try:
    n = int(input("Enter a number : "))
    if n > 0:
        print(f"{n} is a positive number")
    elif n < 0:
        print(f"{n} is a negative number")
    else:
        print(f"It is a {n}")
except:
    print("Enter a Valid number")