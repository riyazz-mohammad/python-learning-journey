n=5
print("=== PATTERN 1: Right Triangle ===")
for i in range(1,n+1):
    print("* "*i)

print("\n=== PATTERN 2: Inverted Triangle ===")
for i in range(n,0,-1):
    print("* "*i)


print("\n=== PATTERN 3: Number Pyramid ===")
for i in range(1,n+1):
    spaces=" "*(n-i)
    numbers=" ".join(str(j)for j in range(1,i+1))
    print(spaces+numbers)

print("\n=== PATTERN 4: Diamond ===")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)
for j in range(n-1,0,-1):
    print(" "*(n-j),end="")
    print("* "*j)
