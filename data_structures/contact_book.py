contacts={}

def add_contact(name,phone,email):
    contacts[name]={
        'phone':phone,
        'email':email
    }
    print(f"{name} added Successfully")

def view_contact(name):
    if name in contacts:
        info=contacts[name]
        print(f"\n{name}")
        print(f"Phone:{info['phone']}")
        print(f"Email:{info['email']}")
    else:
        print("{name} not Found")

def view_all():
    if not contacts:
        print("No contacts saved!")
        return
    print("\n=== ALL CONTACTS ===")
    for name, info in contacts.items():
        print(f"{name}:{info['phone']}")

def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"{name} deleted!")
    else:
        print("\nContact Not found!")


def search_contact(keyword):
    results=[name for name in contacts if keyword.lower() in name.lower()]
    if results:
        print(f"{len(results)} contacts found!")
        for name in results:
            view_contact(name)
    else:
        print(f"Not found with {keyword}")


while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. View All Contacts")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    
    elif choice == "2":
        name = input("Name: ")
        view_contact(name)
    
    elif choice == "3":
        view_all()
    elif choice == "4":
        keyword = input("Search: ")
        search_contact(keyword)
    
    elif choice == "5":
        name = input("Name to delete: ")
        delete_contact(name)
    
    elif choice == "6":
        print("👋 Goodbye!")
        break


