def add(a,b):
    return a+b;

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error:Can't Divide by Zero"
    return a/b

def power(a,b):
    return a**b


print("=== Advanced Calculator ===")
num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
operation=input("Enter operation:+,-,*,/,** :")
 
if operation=='+':
    result=add(num1,num2)
elif operation=='-':
    result=sub(num1,num2)
elif operation=='*':
    result=mul(num1,num2)
elif operation=='/':
    result=divide(num1,num2)
elif operation=='**':
    result=power(num1,num2)
else:
    result="Invalid Operation"

print(f"\nResult:{result}")
