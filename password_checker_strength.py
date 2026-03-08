import random
import string
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

def suggest_strong_password(length=12,useuppercase=True,uselowercase=True,use_digits=True,usespecialcharacter=True):
    character=string.ascii_lowercase
    if useuppercase:
        character+=string.ascii_uppercase
    if use_digits:
        character+=string.digits
    special_char='!@#$%^&*'
    if usespecialcharacter:
        character+=special_char
    password=''.join(random.choice(character) for _ in range(length))
    return password
    

def common_password(password):
    common_password=['password', '12345678', 'qwerty', 'abc123', 'password123',
        '123456789', 'letmein', 'welcome', 'monkey', 'dragon']
    if password  in common_password:
        return True,"This is commonly used password!"
    if all(char.isdigit() for char in password):
        return True,"All are digits-Weak password!"
    if all(char.islower() for char in password):
        return True,"All are lowercase letters-weak password!"
    if all(char.isupper() for char in password):
        return True,"All are upper_case letters-weak password!"
    for i in range(len(password)-2):
       if password[i]==password[i+1]==password[i+2]:
         return True,"Contains repeated characters (like 'aaa' or '111')"
    return False, "✅ Not a common password!"






print("==PASSWORD STRENGTH CHECKER==")
try:
    choice=int(input("Choose choice between 1(password checker) and 2(strong password generator)"))
    if choice==1:
        password=input("Enter your password to check strength..")
        score,feedback,strength=check_password_strength(password)

        is_common, message = common_password(password)
        if is_common:
            print(message)
            score -= 1


        
        print(f"\n Strength:{strength} ({score}/5)")

        if feedback:
            print("\nImprovement Suggestions:")
            for tip in feedback:
                print(f"{tip}")


    elif choice==2:
        password=suggest_strong_password()
        print(password)
except ValueError:
    print("Invalid choice!")




