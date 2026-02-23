import time

print("=== DATA STRUCTURE PERFORMANCE COMPARISON ===\n")

# Create test data
test_size = 10000

# LIST Performance
print("1. LIST - Ordered, Mutable, Allows Duplicates")
print("   Best for: Sequential access, frequent appends")
start = time.time()
my_list = list(range(test_size))
my_list.append(test_size)
5000 in my_list
list_time = time.time() - start
print(f"   Time: {list_time:.6f} seconds")
print(f"   Use case: Shopping cart, history, queue")

# TUPLE Performance
print("\n2. TUPLE - Ordered, Immutable")
print("   Best for: Fixed data, faster than lists")
start = time.time()
my_tuple = tuple(range(test_size))
5000 in my_tuple
tuple_time = time.time() - start
print(f"   Time: {tuple_time:.6f} seconds")
print(f"   Use case: Coordinates, RGB colors, database rows")


# DICTIONARY Performance
print("\n3. DICTIONARY - Key-Value pairs, Very Fast Lookup")
print("   Best for: Looking up data by key")
start = time.time()
my_dict = {i: i*2 for i in range(test_size)}
value = my_dict.get(5000)
dict_time = time.time() - start
print(f"   Time: {dict_time:.6f} seconds")
print(f"   Use case: User profiles, config, cache")


# SET Performance
print("\n4. SET - Unordered, No Duplicates, Fast Membership")
print("   Best for: Unique items, fast membership testing")
start = time.time()
my_set = set(range(test_size))
5000 in my_set
set_time = time.time() - start
print(f"   Time: {set_time:.6f} seconds")
print(f"   Use case: Tags, categories, unique visitors")

# Summary
print("\n" + "="*50)
print("DECISION GUIDE:")
print("="*50)

scenarios = [
    ("Store user preferences", "DICTIONARY", "Fast key-based lookup"),
    ("Track unique website visitors", "SET", "No duplicates, fast checks"),
    ("Store order of tasks", "LIST", "Order matters, can change"),
    ("Store GPS coordinates", "TUPLE", "Fixed data, can't change"),
    ("Shopping cart items", "LIST", "Can add/remove, order matters"),
    ("Student grades by name", "DICTIONARY", "Look up by name"),
    ("Remove duplicate emails", "SET", "Automatically unique"),
    ("RGB color values", "TUPLE", "Fixed 3 values"),
]

print("\nScenario → Best Data Structure → Reason")
print("-" * 70)
for scenario, ds, reason in scenarios:
    print(f"{scenario:<30} → {ds:<12} → {reason}")


print("\n" + "="*50)
print("MEMORY USAGE:")
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

print(f"List size: {my_list.__sizeof__()} bytes")
print(f"Tuple size: {my_tuple.__sizeof__()} bytes (smallest!)")
print(f"Set size: {my_set.__sizeof__()} bytes")
print(f"Dict size: {my_dict.__sizeof__()} bytes (largest)")

print("\n✅ You now know when to use each data structure!")
