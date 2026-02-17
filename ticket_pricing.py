# Program 7: Ticket Pricing System
# Movie theater ticket price calculator

print("=== MOVIE TICKET PRICING ===")
age = int(input("Enter age: "))
is_student = input("Are you a student? (yes/no): ").lower()
is_weekend = input("Is it a weekend? (yes/no): ").lower()

base_price = 200  # Base price in rupees

# Age discount
if age < 5:
    price = 0
    print("Children under 5: FREE!")
elif age < 12:
    price = base_price * 0.5
    print("Child discount applied (50%)")
elif age > 60:
    price = base_price * 0.6
    print("Senior citizen discount applied (40%)")
else:
    price = base_price

# Student discount
if is_student == "yes" and age >= 12:
    price = price * 0.8
    print("Student discount applied (20%)")

# Weekend surcharge
if is_weekend == "yes":
    price = price * 1.2
    print("Weekend surcharge added (20%)")

print("\n💰 Final Ticket Price: ₹" + str(round(price, 2)))