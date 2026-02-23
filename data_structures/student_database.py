students=[]

def add_student():
    student={
        'id':len(students)+1,
        'name':input("Name:"),
        'age':int(input('Age:')),
        'grade':input('Grade:'),
        'subjects':input("Enter Subjects (comma-sepearted):").split(","),
        'marks':{}

    }

    for subject in student['subjects']:
        marks=float(input(f"Enter marks {subject.strip()}:"))
        student['marks'][subject.strip()]=marks
    students.append(student)
    print(f"Student added with id:{student['id']}")

def view_student(student_id):
    for student in students:
        if student['id']==student_id:
            print(f"\n{'='*50}")
            print(f"Id:{student['id']}")
            print(f"Name:{student['name']}")
            print(f"Age:{student['age']}")
            print(f"Grade:{student['grade']}")
            print(f"Subjects:{','.join(student['subjects'])}")
            print("\nMarks")
            for subject,mark in student['marks'].items():
                print(f"{subject}:{mark}")

            avg=sum(student['marks'].values())/len(student['marks'])
            print(f"\nAverage: {avg:.2f}")
            print(f"{'='*50}")
            return
    print(f"Student with id:{student_id} not found!")

def list_all_students():
    if not students:
        print("No student in Database!")
        return
    print("\n===All Students===")
    for student in students:
      avg=sum(student['marks'].values())/len(student['marks'])
      print(f"ID {student['id']}:{student['name']} (Avg:{avg:.2f})")


def top_performers():
    if not students:
        print("No Students in Database!")
        return
    
    student_avgs=[]
    for student in students:
        avg=sum(student['marks'].values())/len(student['marks'])
        student_avgs.append((student['name'],avg))

    student_avgs.sort(key=lambda x:x[1],reverse=True)

    print("\n TOP PERFORMER")
    for i,(name,avg) in enumerate(student_avgs[:3],1):
        print(f"{i}.{name}:{avg:.2f}")

while True:
    print("\n=== STUDENT DATABASE ===")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Top Performers")
    print("5. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        student_id = int(input("Student ID: "))
        view_student(student_id)
    elif choice == "3":
        list_all_students()
    elif choice == "4":
        top_performers()
    elif choice == "5":
        print(f"Total students: {len(students)}")
        break




        


