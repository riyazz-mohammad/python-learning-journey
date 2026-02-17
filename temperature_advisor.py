# Program 5: Temperature Advisor
# Gives clothing advice based on temperature

temp = float(input("Enter temperature in Celsius: "))

if temp >= 35:
    print(" It's VERY HOT!")
    print("Advice: Wear light clothes, stay hydrated!")
elif temp >= 25:
    print("It's WARM!")
    print("Advice: T-shirt and shorts weather!")
elif temp >= 15:
    print("It's MILD!")
    print("Advice: Light jacket recommended!")
elif temp >= 5:
    print("It's COLD!")
    print("Advice: Wear warm clothes and jacket!")
else:
    print("It's FREEZING!")
    print("Advice: Heavy coat, gloves, stay indoors!")