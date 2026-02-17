marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A+"
    result = "Outstanding!"
elif marks >= 80:
    grade = "A"
    result = "Excellent!"
elif marks >= 70:
    grade = "B"
    result = "Good!"
elif marks >= 60:
    grade = "C"
    result = "Average"
elif marks >= 50:
    grade = "D"
    result = "Pass"
else:
    grade = "F"
    result = "Fail - Study harder!"

print("Grade:", grade)
print("Result:", result)