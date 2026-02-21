import random
import string

def generate_password(length=12,use_upper=True,use_digits=True,use_special=True):
    characters=string.ascii_lowercase

    if use_upper:
        characters+=string.ascii_uppercase
    if use_digits:
        characters+=string.digits
    if use_special:
        characters+="!@#$%^&*"
    password=''.join(random.choice(characters) for _ in range(length))
    
    return password

password=generate_password()
print(password)

def check_password_strength(password):
    score=0
    feedback=[]
    if len(password)>=8:
        score+=1
    else:
        feedback.append("Too short (minimum 8 characters)")
    if any(c.isupper() for c in password):
        score+=1
    else:
        feedback.append("Add uppercase letters")
    if any(c.isdigit for c in password):
        score+=1
    else:
        feedback.append("Add numbers")
    if any(c.islower() for c in password):
        score+=1
    else:
        feedback.append("Add lowercase letters")
    if any(c in "!@#$%^&*" for c in password):
        score+=1
    else:
        feedback.append("Add special characters (!@#$%^&*)")
    return score,feedback
print("=== PASSWORD GENERATOR ===")

while True:
    print("\n1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")
    
    choice = input("\nChoice: ")
    if choice=="1":
        length = int(input("Password length (8-32): "))
        use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special chars? (y/n): ").lower() == 'y'
        password = generate_password(length, use_upper, use_digits, use_special)
        print(f"\n Generated Password: {password}")
        score, _ = check_password_strength(password)
        print(f"Strength: {score}/5" )
    elif choice=="2":
        password=input("Enter password to check:")
        score,feedback=check_password_strength(password)
        print(f"\n Password Strength: {score}/5")
        if score == 5:
            print("EXCELLENT! Very strong password!")
        elif score >= 3:
            print("GOOD! But could be better:")
            for tip in feedback:
                print(f"  {tip}")
        else:
            print("WEAK! Improve your password:")
            for tip in feedback:
                print(f"  {tip}")
    
    elif choice == "3":
        break
