def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

def remove_duplicates(numbers):
    numbers=set(numbers)
    return list(numbers)

def count_occurrence(items,item):
    return items.count(item)

def reverse_list(items):
    return items[::-1]

def sort_list(items,descending=False):
    return sorted(items, reverse=descending)



print("=== LIST HELPER DEMO ===")

numbers = [10, 5, 23, 5, 10, 67, 89, 5, 23]
print(f"Original list: {numbers}")

print(f"\nMax: {find_max(numbers)}")
print(f"Min: {find_min(numbers)}")
print(f"Average: {calculate_average(numbers):.2f}")
print(f"Without duplicates: {remove_duplicates(numbers)}")
print(f"Count of 5: {count_occurrence(numbers, 5)}")
print(f"Reversed: {reverse_list(numbers)}")
print(f"Sorted (ascending): {sort_list(numbers)}")
print(f"Sorted (descending): {sort_list(numbers, descending=True)}")