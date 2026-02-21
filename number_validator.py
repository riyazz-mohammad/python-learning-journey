def is_even(n):
    return n%2==0

def is_odd(n):
    return n%2!=0

def is_positive(n):
    return n>0

def is_perfect_square(n):
    if n<0:
        return False
    num=int(n**0.5)
    return num*num==n

def is_armstrong(n):
    digits=str(abs(n))
    power=len(digits)
    total=sum(int(digit)**power for digit in digits)
    return total==n
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print("=== NUMBER VALIDATOR ===")
test_numbers = [153, 16, 25, 370, 9, 100, -5]

for num in test_numbers:
    print(f"\nTesting {num}:")
    print(f"  Even: {is_even(num)}")
    print(f"  Positive: {is_positive(num)}")
    print(f"  Perfect Square: {is_perfect_square(num)}")
    print(f"  Armstrong: {is_armstrong(num)}")
    print(f"  Sum of Digits: {sum_of_digits(num)}")
