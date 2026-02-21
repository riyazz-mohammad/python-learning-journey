def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def display_menu():
    """Display conversion menu"""
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

while True:
    display_menu()
    choice=input("Enter the choice (1-5):")
    if choice =='5':
        print("Goodbye")
        exit()
    if choice in ['1','2','3','4']:
        temp=float(input("Enter Temprature:"))
        if choice=='1':
            result=celsius_to_fahrenheit(temp)
            print(f"{temp}C={result:.2f}F")
        elif choice =='2':
            result=fahrenheit_to_celsius(temp)
            print(f"{temp}F={result:.2f}C")
        elif choice=='3':
            result=celsius_to_kelvin(temp)
            print(f"{temp}C={result:.2f}K")
        elif choice=='4':
            result=kelvin_to_celsius(temp)
            print(f"{temp}K={result:.2f}C")
    else:
        print("Enter Valid Choice!")
    
