#  Check if a year is century year
try:
    year = int(input("Enter a year : "))
    if year <= 0:
        print("Enter a positive year")
    elif (year % 100 == 0):
        print(f"{year} is a century year")
    else:
        print(f"{year} is not a century year")
except ValueError:
    print("Enter a valid year")