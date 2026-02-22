student = {
    "name": "Riyaz",
    "age": 25,
    "city": "Hyderabad",
    "course": "Open Source",
    "goal": "Outreachy 2026"
}

print("===Orginal Dictionary===")
for key,value in student.items():
    print(f"{key}:{value}")

print(f"Student name:{student['name']}")
print(f"Goal:{student['goal']}")
print(f"Country:{student.get('country','not specified')}")
student['email']='riyaz@gmail.com'
student['age']=22
print("===After Updates===")
print(student)

removed=student.pop('course')
print(f"Popped course:{removed}")

print(f"\n keys:{list(student.keys())}")
print(f"\n Values:{list(student.values())}")


students = {
    "student1": {"name": "Riyaz", "marks": 95},
    "student2": {"name": "Ahmed", "marks": 87},
    "student3": {"name": "Fatima", "marks": 92}
}
print("\n=== CLASS RECORDS ===")
for id ,info in students.items():
    print(f"{id}:{info['name']}-{info['marks']} marks")

numbers=[1,2,3,4,5]
squared={x:x**2 for x in numbers}
print(squared)


text = "hello world hello python"
word_count={}

for word in text.split():
    word_count[word]=word_count.get(word,0)+1
print(f"\nWord count: {word_count}")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged={**dict1,**dict2}
print(f"After Merged:{merged}")




