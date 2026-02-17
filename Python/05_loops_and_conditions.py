# loops and conditions in python

numbers = [10, 15, 20, 25, 30]

print("Even numbers in the list:")

for num in numbers:
    if num % 2 == 0:
        print(num)

print("\nChecking positive or negative:")

values = [-5, 0, 7, -2, 9]

for v in values:
    if v > 0:
        print(v, "is positive")
    elif v < 0:
        print(v, "is negative")
    else:
        print(v, "is zero")
