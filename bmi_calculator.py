# Program 6: BMI Calculator
# Calculates and categorizes Body Mass Index

print("=== BMI CALCULATOR ===")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
bmi = round(bmi, 2)

print("\nYour BMI:", bmi)

if bmi < 18.5:
    print("Category: UNDERWEIGHT")
    print("Advice: Eat more nutritious food!")
elif bmi < 25:
    print("Category: NORMAL WEIGHT ✅")
    print("Advice: Keep it up! You're healthy!")
elif bmi < 30:
    print("Category: OVERWEIGHT")
    print("Advice: Exercise more, eat less junk!")
else:
    print("Category: OBESE")
    print("Advice: Consult a doctor immediately!")