# Printing pass or fail.
try:
    marks = int(input("Enter student marks : "))
    if marks >= 33:
        print("PASS")
    elif marks > 75:
        print("Enter marks out of 75")
    else:
        print("FAIL")
except ValueError:
    print("Invalid marks")