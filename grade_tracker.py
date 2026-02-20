print("=== STUDENT GRADE TRACKER ===")
print("Enter the Student names and marks")
print("Type done when finished!\n")

students=[]
while True:
    name=input("Enter the student name(or type done):")
    if name.lower()=='done':
        break
    marks=float(input("Enter the student marks:"))
    students.append((name,marks))
    print(f"{name} added!")

if len(students)==0:
    print("No student entered!")
else:
    print("\n=== CLASS REPORT ===")
    print("-" * 35)
    total = 0
    highest = students[0]
    lowest = students[0]

    for name, marks in students:
        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"
        print(f"{name}:{marks} ({grade})")
        total+=marks
        if marks>highest[1]:
            highest=(name,marks)
        if marks<lowest[1]:
            lowest=(name,marks)
    print("-"*35)
    avg = total / len(students)
    print(f"Class Average: {avg:.1f}")
    print(f"🏆 Highest: {highest[0]} ({highest[1]})")
    print(f"📉 Lowest: {lowest[0]} ({lowest[1]})")
    print(f"Total Students: {len(students)}")
