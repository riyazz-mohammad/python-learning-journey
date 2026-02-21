
def greet(name="Guest", greeting="Hello"):
    """Function with default parameters"""
    return f"{greeting}, {name}!"

def calculate(*numbers):
    """Function with variable arguments"""
    if not numbers:
        return 0
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

def get_user_info(**kwargs):
    """Function with keyword arguments"""
    return kwargs

def recursive_countdown(n):
    """Recursive function example"""
    if n <= 0:
        print("BLAST OFF!")
        return
    print(n)
    recursive_countdown(n - 1)


square = lambda x: x ** 2
cube = lambda x: x ** 3
is_adult = lambda age: age >= 18

print("=== FUNCTION SHOWCASE ===")


print(f"\n1. Default parameters: {greet()}")
print(f"2. Custom parameters: {greet('Riyaz', 'Namaste')}")

print(f"\n3. Variable arguments:")
stats = calculate(10, 20, 30, 40, 50)
for key, value in stats.items():
    print(f"   {key}: {value}")

print(f"\n4. Keyword arguments:")
user = get_user_info(name="Riyaz", age=25, city="Hyderabad", goal="Outreachy")
for key, value in user.items():
    print(f"   {key}: {value}")

print(f"\n5. Recursive function:")
recursive_countdown(5)

print(f"\n6. Lambda functions:")
print(f"   Square of 5: {square(5)}")
print(f"   Cube of 3: {cube(3)}")
print(f"   Is 20 adult? {is_adult(20)}")