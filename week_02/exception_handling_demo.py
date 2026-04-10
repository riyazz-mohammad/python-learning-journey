import sys

def basic_division():
    try:
        num1=int(input("Enter the number:"))
        num2=int(input("Enter the number:"))
        result=num1/num2
    except ZeroDivisionError:
        print("Enter the valid denominator!")
    except ValueError:
        print("Incorrect value!")

def advanced_division():
    try:
        num1=int(input("Enter the number:"))
        num2=int(input("Enter the number:"))
        result=num1/num2
    except ZeroDivisionError:
        print("Enter the valid denominator!")
    except ValueError:
        print("Incorrect value!")
    except Exception as e:
        print(e)
    else:
        print(f"The result:{result:.2f}")  
    finally:
        print("Division completed!")


def file_reader():
    try:
        filename=input("Enter the filename to read:")
        with open(filename,'r')as file:
            content=file.read()
            lines=content.split('\n')
            print(f"The no of lines:{len(lines)}")
            print(f"First Line:{lines[0]}")
    except PermissionError:
        print("No permission allowed!")
    except FileNotFoundError:
        print("No file found!")
    except Exception as e:
        print(f"Unexcepted error:{e}")

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def bank_withdrawal():
    print("\n Bank Withrawal..")
    balance=1000
    print(f"The current balance is:{balance}")
    try:
        amount=int(input("Enter the amount to withdraw:"))
        if amount>balance:
            raise InsufficientFundsError("Low Balance!")
        if amount<0:
            raise InvalidAmountError("Enter the postive amount!")
        balance-=amount
        print("Withdrawal Successful!")
        print(f"The current balance:{balance}")
    
    except InsufficientFundsError as e:
        print(f"Invalid!:{e}")
    except InvalidAmountError as e:
        print(f"Invalid:{e}")
    except ValueError:
        print("Invalid value!")

def divide_number(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero! & Enter the value > 0!")
    return a/b

def process_division():
    try:
        num1=float(input("Enter the num1:"))
        num2=float(input("Enter the num2:"))
        result=divide_number(num1,num2)
        print(f"Result:{result}")
    except ValueError as e:
        print(f"Error! {e}")

def safe_calculator():
    try:
        num1=float(input("Enter the num1:"))
        operator=input("Enter the operator:(+,-,*,/,%,**(power))")
        num2=float(input("Enter the num2:"))
        valid_operators=['+','-','*','/','%','**']
        if operator not in valid_operators:
            raise ValueError(f"Invalid operator!Use operator from this:{', '.join(valid_operators)}")
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif  operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result= num1 / num2
        elif operator == '**':
            if num2 == 0 and num1<0:
                raise ValueError("Error! Negatives not allowed in powers!")
            result=num1**num2
        print(f"{num1} {operator} {num2} = {result}")
    except ValueError as e:
        print(f"Error:{e}")
    except ZeroDivisionError as e:
        print(f"Error:{e}")
    except Exception as e:
        print(f"Invalid:{e}")
    finally:
        print("calculator operation completed!")

def division_with_logging():
    print("\n=== DIVISION WITH LOGGING ===")
    errors=[]
    try:
        num1=float(input("Enter the num1:"))
        num2=float(input("Enter the num2:"))
        result=num1/num2
        print(f"The result:{result}")
    except ZeroDivisionError as e:
        error_msg=f"ZeroDivisionErrorr:{e}"
        errors.append(error_msg)
        print(f"Error:{error_msg}")
    except ValueError as e:
        error_msg=f"ValueErrorr:{e}"
        errors.append(error_msg)
        print(f"Error:{error_msg}")
    finally:
        if errors:
            with open('errors_log.txt','a') as file:
                from datetime import datetime
                timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"[{timestamp}] {errors[-1]}\n")
            print("Errors logged to errors_lof.txt")

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("🛡️  EXCEPTION HANDLING MASTER CLASS")
    print("=" * 60)
    print("1. Basic Division (try/except)")
    print("2. Advanced Division (try/except/else/finally)")
    print("3. File Reader (multiple exceptions)")
    print("4. Bank Withdrawal (custom exceptions)")
    print("5. Exception Chaining")
    print("6. Safe Calculator (comprehensive)")
    print("7. Division with Logging")
    print("8. Exit")
    print("=" * 60)


def main():
    """Main program loop"""
    print("\n🎉 Welcome to Exception Handling Master Class!")
    print("Learn how to write robust, professional code!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter choice (1-8): "))
            
            if choice == 1:
                basic_division()
            elif choice == 2:
                advanced_division()
            elif choice == 3:
                file_reader()
            elif choice == 4:
                bank_withdrawal()
            elif choice == 5:
                process_division()
            elif choice == 6:
                safe_calculator()
            elif choice == 7:
                division_with_logging()
            elif choice == 8:
                print("\n👋 Goodbye! Keep writing robust code!")
                break
            else:
                print("❌ Invalid choice! Choose 1-8")
                
        except ValueError:
            print("❌ Invalid input! Enter a number")
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted! Exiting...")
            break


if __name__ == "__main__":
    main()



    





