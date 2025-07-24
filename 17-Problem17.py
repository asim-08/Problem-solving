# Checking if number is dividible by 5 and 11.

n = int(input("Enter a number : "))
if (n%5 == 0 and n%11 == 0):
    print(f"{n} is divisible by both number 5 and 11")
elif(n%5 == 0):
    print(f"{n} is divisible by 5")
elif(n%11 == 0):
    print(f"{n} is divisible by 11")
else:
    print(f"{n} is not divisible by both number 5 and 11")