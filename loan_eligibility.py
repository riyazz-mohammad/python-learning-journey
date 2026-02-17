# Program 9: Loan Eligibility Checker
# Checks if a person qualifies for a loan

print("=== LOAN ELIGIBILITY CHECKER ===")
age = int(input("Enter age: "))
income = float(input("Enter monthly income (₹): "))
credit_score = int(input("Enter credit score (300-900): "))
existing_loans = int(input("Number of existing loans: "))

print("\n🔍 Checking eligibility...")

eligible = True
reasons = []

if age < 21 or age > 65:
    eligible = False
    reasons.append("Age must be between 21-65")

if income < 25000:
    eligible = False
    reasons.append("Minimum income ₹25,000 required")

if credit_score < 650:
    eligible = False
    reasons.append("Credit score must be 650+")

if existing_loans >= 3:
    eligible = False
    reasons.append("Too many existing loans (max 2)")

if eligible:
    print("CONGRATULATIONS! You're ELIGIBLE for a loan!")
    if credit_score >= 800:
        print("Excellent credit score! Best interest rates!")
    elif credit_score >= 700:
        print("Good credit score! Favorable rates!")
else:
    print("Sorry, you're NOT eligible. Reasons:")
    for reason in reasons:
        print(" -", reason)