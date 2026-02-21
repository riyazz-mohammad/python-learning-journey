students={}

def add_student(name,marks):
    students[name]=marks
    print(f"{name} added Successfully!")

def get_grade(marks):
    if marks>=90:return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else: return "F"

def display_student(name):
    if name in students:
        marks=students[name]
        grade=get_grade(marks)
        print(f"{name}:{marks} marks (Grade:{grade})")

def display_all():
    if not students:
        print("\nNo Students in system!")
        return
    for name,marks in students.items():
        grade=get_grade(marks)
        print(f"{name}:{marks} marks (Grade:{grade})")

def class_statistics():
    if not students:
        print("\nNo Data Available!")
        return

    mark_list=list(students.values())
    avg=sum(mark_list)/len(mark_list)
    highest=max(mark_list)
    lowest=min(mark_list)
    print(f"\n=== CLASS STATISTICS ===")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Total Students: {len(students)}")


while True:
    print("\n=== GRADE MANAGER ===")
    print("1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Class Statistics")
    print("5. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        name = input("Student name: ")
        marks = float(input("Marks: "))
        add_student(name, marks)
    elif choice == "2":
        name = input("Student name: ")
        display_student(name)
    elif choice == "3":
        display_all()
    elif choice == "4":
        class_statistics()
    elif choice == "5":
        break