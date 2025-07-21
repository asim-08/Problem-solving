# Grading students based on marks.

try:
    student_marks = int(input("Enter a student marks : "))
    if student_marks >= 90 or student_marks <= 100:
        print("Grade A+")
    elif student_marks >= 80 or student_marks < 90:
        print("Grade A")
    elif student_marks >= 70 or student_marks < 80:
        print("Grade B")
    elif student_marks >= 60 or student_marks < 70:
        print("Grade C")
    elif student_marks >= 50 or student_marks < 60:
        print("Grade D")
    elif student_marks > 100:
        print("Enter marks in range of 0 to 100")
    else:
        print("Fail")
except ValueError:
    print("Invalid Input")