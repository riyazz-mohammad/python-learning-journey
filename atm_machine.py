balance=10000.0
pin="1234"
attempts=0

while attempts<3:
    entered_pin=input("Enter PIN:")
    if entered_pin==pin:
        print("PIN correct!/n")
        break
    else:
        attempts+=1
        remaining=3-attempts
        if remaining>0:
            print(f"Worng PIN! {remaining} attempts left!")
        else:
            print("CARD BLOCKED! Contack your Bank!")
            exit()
while True:
    print("\n=== MAIN MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice=input("/nEnter the choice(1-4): ")
    if choice=="1":
        print(f"Current Balance ${balance:.2f}")
    elif choice=="2":
        amount=float(input("Enter deposit amount:$"))
        if amount>0:
            balance+=amount
            print(f"${amount} deposited!")
            print(f"New Balance:${balance:.2f}")
        else:
            print("Invalid Number!/n")
    elif choice=="3":
        amount=float(input("Enter withdrawal amount $:"))
        if amount<=0:
            print("Invalid Number")
        elif amount>balance:
            print(f"Insufficient Funds! Balance :{balance:.2f}")
        else:
            balance-=amount
            print(f"${amount} Withdrawn!")
            print(f"Remaining Balance:${balance:.2f}")
    elif choice=="4":
        print("\n👋 Thank you for using our ATM!")
        print("Have a great day!")
        break
    else:
        print("Invalid choice!(Enter 1-4)")

        


