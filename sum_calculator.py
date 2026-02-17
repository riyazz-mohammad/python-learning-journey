# Program 3: Sum Calculator
# Calculates various sums using loops

# Sum 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100 = {total}")

# Sum of even numbers 1-100
even_sum = 0
for i in range(2, 101, 2):
    even_sum += i
print(f"Sum of even numbers (1-100) = {even_sum}")

# Sum of odd numbers 1-100
odd_sum = 0
for i in range(1, 101, 2):
    odd_sum += i
print(f"Sum of odd numbers (1-100) = {odd_sum}")

# User input sum
n = int(input("\nEnter N to sum from 1 to N: "))
user_sum = 0
for i in range(1, n + 1):
    user_sum += i
print(f"Sum of 1 to {n} = {user_sum}")