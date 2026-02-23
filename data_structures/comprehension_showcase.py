# Program 8: List/Dict/Set Comprehension Showcase

print("=== LIST COMPREHENSION ===")

# Basic list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Even numbers only
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# Conditional transformation
modified = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(f"Squared evens, cubed odds: {modified}")

# String operations
names = ["riyaz", "ahmed", "fatima", "sara"]
capitalized = [name.title() for name in names]
print(f"\nCapitalized names: {capitalized}")

# Filter by length
long_names = [name for name in names if len(name) > 5]
print(f"Long names (>5 chars): {long_names}")

# Nested lists (matrix)
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMultiplication table:")
for row in matrix:
    print(row)

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(f"\nFlattened: {flat}")

print("\n" + "="*50)
print("=== DICTIONARY COMPREHENSION ===")

# Square dictionary
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Filter dictionary
numbers_dict = {"a": 10, "b": 5, "c": 15, "d": 3}
filtered = {k: v for k, v in numbers_dict.items() if v > 5}
print(f"Values > 5: {filtered}")

# Transform values
doubled = {k: v*2 for k, v in numbers_dict.items()}
print(f"Doubled values: {doubled}")

# Create dict from two lists
keys = ["name", "age", "city"]
values = ["Riyaz", 25, "Hyderabad"]
person = {k: v for k, v in zip(keys, values)}
print(f"Person dict: {person}")

print("\n" + "="*50)
print("=== SET COMPREHENSION ===")

# Unique squares
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers_with_dupes}
print(f"Unique squares: {unique_squares}")

# Filter set
even_set = {x for x in range(1, 21) if x % 2 == 0}
print(f"Even numbers (1-20): {even_set}")

print("\n" + "="*50)
print("=== PRACTICAL EXAMPLES ===")

# Email validation
emails = ["user@email.com", "invalid", "test@domain.com", "nope"]
valid_emails = [e for e in emails if "@" in e and "." in e]
print(f"\nValid emails: {valid_emails}")

# Temperature conversion
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(f"\nCelsius to Fahrenheit:")
for c, f in zip(celsius, fahrenheit):
    print(f"  {c}°C = {f}°F")

# Grade classification
marks = [45, 78, 92, 34, 88, 56, 91]
grades = ["Pass" if m >= 50 else "Fail" for m in marks]
print(f"\nMarks: {marks}")
print(f"Results: {grades}")