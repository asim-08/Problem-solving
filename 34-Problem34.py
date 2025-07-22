# Leap year checker
try:
    year = int(input("Enter a year : "))
    if (year <= 0):
        print("Invalid year")
    elif (year % 400 == 0):
        print(f"{year} is a leap year")
    elif (year % 100 == 0):
        print(f"{year} is not a leap year")
    elif (year % 4 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
except ValueError:
    print("Enter a valid year")
