# Program 4: Simple Login System
# Validates username and password

# Stored credentials
correct_username = "riyaz"
correct_password = "outreachy2026"

print("=== LOGIN SYSTEM ===")
username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login SUCCESSFUL!")
    print("Welcome,", username + "!")
elif username == correct_username and password != correct_password:
    print(" Wrong PASSWORD!")
    print("Hint: It's related to your goal...")
elif username != correct_username and password == correct_password:
    print("Wrong USERNAME!")
else:
    print("Both username and password are WRONG!")
    print("Access DENIED!")