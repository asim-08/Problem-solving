# Using While loop.
n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(f"The sum of {n} natural number is: {sum}")

# Using For loop.
n = int(input("Enter a number: "))
sum = 0
for i in range (1,n+1):
    sum += i
print(f"The sum of {n} natural number is: {sum}")

