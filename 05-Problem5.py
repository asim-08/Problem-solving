# Making small calculator.

a = float(input("Enter first number: "))
print()
print("Select Operations")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (X)")
print("4. Division (/)")

c = int(input("Enter you'r choice (1/2/3/4): "))
print()
b = float(input("Enter second number: "))

if (c == 1):
    print("The sum of two number is: ", a + b)
elif (c == 2):
    print("The subtraction of two number is: ", a - b)
elif (c == 3):
    print("The multiplication of two number is: ", a * b)
elif (c == 4):
    if (b != 0):
        print("The divison of two number is: ", a / b)
    else:
        print("Error: Divided by 0")
else:
    print("Invalid Input")