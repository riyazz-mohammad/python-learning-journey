def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def factorial(n):
    if n==0 or n==1:
        return 1
    result=1
    for i in range(2,n+1):
        result*=i
    return result

def fibonacci(n):
    if n<=0:
        return []
    if n==1:
        return [0]
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[-1]+fib[-2])
    return fib
 

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a*b)//gcd(a,b)

    
while True:
    print("\n=== MATH HELPER ===")
    print("1. Check Prime Number")
    print("2. Calculate Factorial")
    print("3. Generate Fibonacci Sequence")
    print("4. Find GCD")
    print("5. Find LCM")
    print("6. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        num = int(input("Enter number: "))
        if is_prime(num):
            print(f"{num} is PRIME!")
        else:
            print(f"{num} is NOT prime")

    elif choice == "2":
        num = int(input("Enter number: "))
        print(f"{num}! = {factorial(num)}")
    elif choice == "3":
        n = int(input("How many Fibonacci numbers? "))
        print(f"First {n} Fibonacci numbers:")
        print(fibonacci(n))

    elif choice == "4":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"GCD of {a} and {b} = {gcd(a, b)}")

    elif choice == "5":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"LCM of {a} and {b} = {lcm(a, b)}")
    elif choice == "6":
        print("👋 Goodbye!")
        break
    
    