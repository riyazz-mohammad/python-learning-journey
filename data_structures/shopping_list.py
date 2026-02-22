shopping_list=[]
purchased=set()

def add_item(item):
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"Added:{item}")
    else:
        print(f"{item} already in List!")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed!")
    else:
        print(f"{item} not in list!")

def mark_purchased(item):
    if item in shopping_list:
        purchased.add(item)
        shopping_list.remove(item)
        print(f"Marked as Purchased:{item}!")
    else:
        print(f"{item} not in list!")

def view_list():
    if not shopping_list:
        print("Shopping list is empty!")
    else:
        print("\n==Shopping list==")
        for i,item in enumerate(shopping_list,1):
            print(f"{i}.{item}")

def view_purchased():
    if not purchased:
        print("No items Purchased yet!")
    else:
        print("\n==Purchased==")
        for i,item in enumerate(purchased,1):
            print(f"{i}.{item}")

def clear_all():
    shopping_list.clear()
    purchased.clear()
    print("\nAll Cleared!")

print("Adding Initial Items....")
add_item("Milk")
add_item("Bread")
add_item("Eggs")
add_item("Rice")


while True:
    print("\n=== SHOPPING LIST MANAGER ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Mark as Purchased")
    print("4. View Shopping List")
    print("5. View Purchased Items")
    print("6. Clear All")
    print("7. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        item = input("Item name: ").title()
        add_item(item)
    elif choice == "2":
        item = input("Item to remove: ").title()
        remove_item(item)
    elif choice == "3":
        item = input("Item purchased: ").title()
        mark_purchased(item)
    elif choice == "4":
        view_list()
    elif choice == "5":
        view_purchased()
    elif choice == "6":
        confirm = input("Clear everything? (yes/no): ")
        if confirm.lower() == "yes":
            clear_all()
    elif choice == "7":
        print(f"\n📊 Summary:")
        print(f"   Items to buy: {len(shopping_list)}")
        print(f"   Items purchased: {len(purchased)}")
        print("👋 Happy shopping!")
        break




