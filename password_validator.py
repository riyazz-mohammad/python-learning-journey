
correct_password="Outreachy2026"
max_attempts=3
attempt=0

print("=== SECURE LOGIN SYSTEM ===")

while max_attempts>attempt:
    password=input("Enter the Password:")
    attempt+=1
    if password==correct_password:
        print("Access GRANTED! Welcome!")
        print("Redirecting to Dashboard")
        break
    else:
        remaining=max_attempts-attempt
        if remaining>0:
          print(f"Wrong Password ! {remaining} attempt remaining!")
        else:
            print("Account LOCKED! Too many failed attempts!")
            print("Please contact support.")

    