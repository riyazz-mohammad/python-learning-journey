print("=== PATTERN 1: Simple Triangle ===")
for i in range(1,6):
    print("* "*i)

print("\n=== PATTERN 2: Number Triangle ===")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("\n=== PATTERN 3: Countdown ===")
for i in range(10, 0, -1):
    print(i, end=" ")
print("BLAST OFF!")

print("\n=== PATTERN 4: Even Numbers 1-20 ===")
for i in range(2, 21, 2):
    print(i, end=" ")
print()