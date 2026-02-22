def display_list(lst,title="List"):
    print(f"{title}:{lst}")
numbers=[10,20,30,40,50]
display_list(numbers,"Original")

numbers.append(60)
display_list(numbers,"After Append(60)")

numbers.insert(0,5)
display_list(numbers,"After Inserting (0,5)")

numbers.remove(30)
display_list(numbers,"After remove(30)")

removed=numbers.pop()
print(f"Popped:{removed}")
display_list(numbers,"After pop()")

print(f"\n Index of 20:{numbers.index(20)}")
numbers.append(20)
print(f"Count of 20:{numbers.count(20)}")

numbers.sort()
display_list(numbers,"After Sorting")
numbers.reverse()
display_list(numbers,"After reverse")

squared=[x**2 for x in numbers]
display_list(squared,"After Squared")

even=[x for x in numbers if x%2==0]
display_list(even,"Even only")


list1=[1,2,3]
list2=[9,0,8]
combined=list1+list2
display_list(combined,"After combaining list1 and list2")

print(f"\nMax: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")


