#  Determining if triangle is valid based on angles.
try:
    angle_1 = int(input("Enter angle-1 : "))
    angle_2 = int(input("Enter angle-2 : "))
    angle_3 = int(input("Enter angle-3 : "))
    if (angle_1 > 0 and angle_2 > 0 and angle_3 > 0) and (angle_1 + angle_2 + angle_3 == 180):
        print("Valid Triangle")
    elif angle_1 < 0 or angle_2 < 0 or angle_3 < 0:
        print("Enter a positive angle")
    else:
        print("Invalid Triangle")
except ValueError:
    print("Enter a valid angles")
