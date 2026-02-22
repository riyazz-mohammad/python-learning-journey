print("=== TUPLE OPERATIONS ===")

coordinates = (10.5, 20.3)
date = (2026, 2, 19)
colors = ("red", "green", "blue")

print(f"Coordinates:{coordinates}")
print(f"X:{coordinates[0]}-Y:{coordinates[1]}")

x,y=coordinates
print(f"X:{x} - Y:{y}")

year,month,date=date
print(f"Date:{year}-{month}-{date}")

numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"\nCount of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

user=('Riyaz',23,'Hyderabad')
print(f"User:{user}")
print("\n" + "="*50)
print("=== SET OPERATIONS ===")

numbers = {1, 2, 3, 3, 3, 4, 5}
print(f"Set (duplicates removed): {numbers}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

print(f"Union:{set1.union(set2)}")

print(f"Intersection:{set1.intersection(set2)}")

print(f"Difference:{set1.difference(set2)}")

print(f"Symmetric diff:{set1.symmetric_difference(set2)}")

set1.add(6)
print(f"After adding 6:{set1}")

set1.remove(1)
print(f"Ater removing 1:{set1}")

list_with_dup=[1,2,2,3,4,4,5,8,8,5]
unique=set(list_with_dup)
print(f"Orginal List:{list_with_dup}")
print(f"Unique lst:{unique}")

squared_set={x:x**2 for x in range(1,6)}
print(f"Squared set:{squared_set}")