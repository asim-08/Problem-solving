#  Calculate electricity bill based on units.
try:
    units = int(input("Enter electricity units : "))
    if units < 0:
        print("Enter units in postive number")
    elif units <= 200:
        print(f"The electricity bill is {units * 15}")
    elif units <= 300:
        print(f"The electricity bill is {(200 * 15) + (units - 200)  * 20}")
    elif units <= 400:
        print(f"The electricity bill is {(200 * 15) + (100 * 20) + (units - 300) * 30}")
    elif units > 400:
        print(f"The electricity bill is {(200 * 15) + (100 * 20) + (100 * 30) + (units - 400) * 35}")

    else:
        print("Enter a valid units")
except ValueError:
    print("Invalid units")


