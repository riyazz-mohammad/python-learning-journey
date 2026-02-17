num = int(input("Enter a number: "))


if num > 0:
    print(num, "is POSITIVE")
elif num < 0:
    print(num, "is NEGATIVE")
else:
    print("The number is ZERO")

# Check even/odd
if num % 2 == 0:
    print(num, "is EVEN")
else:
    print(num, "is ODD")

# Check if large
if num > 1000:
    print(num, "is a LARGE number")
elif num > 100:
    print(num, "is a MEDIUM number")
else:
    print(num, "is a SMALL number")