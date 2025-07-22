# Grading students based on marks.

try:
    student_marks = int(input("Enter a student marks : "))
    if student_marks > 100 or student_marks < 0:
        print("Enter marks in range of 0 to 100")
    elif student_marks >= 90 and student_marks <= 100:
        print("Grade A+")
    elif student_marks >= 80 and student_marks < 90:
        print("Grade A")
    elif student_marks >= 70 and student_marks < 80:
        print("Grade B")
    elif student_marks >= 60 and student_marks < 70:
        print("Grade C")
    elif student_marks >= 50 and student_marks < 60:
        print("Grade D")

    else:
        print("Fail")
except ValueError:
    print("Invalid Input")