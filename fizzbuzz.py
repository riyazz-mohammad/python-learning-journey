print("=== FIZZBUZZ (1 to 50) ===")

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FIZBUZZ",end=" ")
    elif i%3==0:
        print("Fizz",end=" ")
    elif i%5==0:
        print("Buzz",end=" ")
    else:
        print(i,end=" ")
print("\n\n FizzBuzz complete!")
print("(This is asked in REAL coding interviews!)")