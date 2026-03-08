def check_password_strength(password):
    score=0
    feedback=[]
    if len(password)>=8:
        score+=1
    else:
        feedback.append("Too short(Minimum 8 characters required.)!")
    if any(char.isupper()  for char in password):
        score+=1
    else:
        feedback.append("Atleast one uppercase character required!")
    if any(char.islower() for char in password):
        score+=1
    else:
        feedback.append("Atleast one lower_Case required!")
    special_char='!@#$%&*^'
    if any(char in special_char for char in password):
        score+=1
    else:
        feedback.append("Atleast one special character required!")
    if any(char.isdigit() for char in password):
        score+=1
    else:
        feedback.append("Atleast one digit is required!")

    if score==5:
        strength='Excellent!'
    elif score>=3:
        strength='Good!'
    else:
        strength='Weak!'

    return score,feedback,strength

print("==PASSWORD STRENGTH CHECKER==")
password=input("Enter your password to check strength..")

score,feedback,strength=check_password_strength(password)
print(f"\n Strength:{strength} ({score}/5)")

if feedback:
    print("\nImprovement Suggestions:")
    for tip in feedback:
        print(f"{tip}")
