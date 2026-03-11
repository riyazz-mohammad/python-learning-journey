import json
import csv
contacts=[]
def add_contact():
    print("\n ADD NEW CONTACT")
    print("-"*40)
    name=input("Name:").strip()
    phone=input("Phone:").strip()
    email=input("Email:").strip()
    contact={
        "id":len(contacts)+1,
        "name":name,
        "phone":phone,
        "email":email

    }
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_all_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print(f"ALL CONTACTS(TOTAL:{len(contacts)})")
    print("="*70)
    print(f"{'ID':<5}{'Name':<20}{'Phone':<15}{'Email':<30}")
    print("-"*70)

    for contact in contacts:
        print(f"{contact['id']:<5}{contact['name']:<20}{contact['phone']:<15}{contact['email']:<30}")
    print("="*70)

def search_contacts():
    search_term=input("Enter the contact name:").lower().strip()

    results=[c for c in contacts if search_term in c['name'].lower()]

    if not results:
        print(f"No contact match with {search_term}")
        return
    print("-"*70)
    for contact in results:
        print(f"ID: {contact['id']}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    print("-" * 70)

def delete_contact():
    view_all_contacts()
    if not contacts:
        print("No contacts listed!")
        return
    try:
        contact_id=int(input("Enter the contact id:"))

        for i,contact in enumerate(contacts):
            if contact['id']==contact_id:
                delete_name=contact['name']
                contacts.pop(i)
                print(f"Contact {delete_name} deleted!")
                return
        print(f"Contact with ID {contact_id} not found!")
    except ValueError:
        print("Invalid ID!Please enter number..")


def load_contacts():
    global contacts
    try:
        with open('contacts.json','r') as file:
            contacts=json.load(file)
        print(f"Loaded {len(contacts)} contacts from file!")
    
    except FileNotFoundError:
        print("No saved contacts found. Starting fresh!")
        contacts=[]
    except json.JSONDecodeError:
        print("Contact file corrupted.Starting fresh1")
        contacts=[]

def save_contacts():
    try:
        with open('contacts.json','w')as file:
            json.dump(contacts,file,indent=4)
        print("Contacts saved successfully!")
    except Exception as e:
        print(f" Error saving  contacts:{e}")

def edit_contacts():
    view_all_contacts()
    if not contacts:
        print("No contacts listed!")
        return
    try:
        contact_id=int(input("Enter contact id:"))

        for contact in contacts:
            if contact['id']==contact_id:
                print(f"Editing of: {contact['name']}")
                print("(Press Enter to keep current value)")

                new_name=input(f"Enter new name of{contact['name']}").strip()
                new_phone=input(f"Enter new phone of {contact['phone']}").strip()
                new_email=input(f"Enter new email of {contact['email']}").strip()

                if new_name:
                    contact['name']=new_name
                if new_phone:
                    contact['phone']=new_phone
                if new_email:
                    contact['email']=new_email

                print("Contact Updated!")
                return
            
        print(f"No contacts found with {contact_id} id!")


    except ValueError:
        print("Invalid ID!")

def export_to_csv():
    if not contacts:
        print("No contacts to export!")
        return
    try:
        with open('contacts.csv','w',newline='')as file:
            writer=csv.DictWriter(file,fieldnames=['id','name','phone','email'])
            writer.writeheader()
            writer.writerows(contacts)
        print(f"Exported {len(contacts)} contacts to contacts.csv")
    except Exception as e:
        print(f"Export failed:{e}!")

def import_csv():
    try:
        with open('contacts.csv','r') as file:
            reader=csv.DictReader(file)
            imported=0

            for row in reader:
                row['id']=int(row['id'])
                contacts.append(row)
                imported+=1
        print(f"Imported {imported} contacts from contacts.csv")
    except FileNotFoundError:
        print("contacts.csv not found!")





        


def display_menu():
    print("\n" + "=" * 50)
    print("📇 CONTACT MANAGER")
    print("=" * 50)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Edit Contacts")
    print("6. Export to CSV")
    print("7. Import to CSV")
    print("8. Save & Exit")
    print("=" * 50)
def main():
    """Main program loop"""
    print("\n🎉 Welcome to Contact Manager!")
    
    # Load existing contacts on startup
    load_contacts()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter choice (1-8): "))
            
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_all_contacts()
            elif choice == 3:
                search_contacts()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                edit_contacts()
            elif choice == 6:
                export_to_csv()
            elif choice == 7:
                import_csv()
            elif choice == 8:
                save_contacts()
                print("\n👋 Goodbye! Your contacts are saved!")
                break
            else:
                print("❌ Invalid choice! Choose 1-5")
                
        except ValueError:
            print("❌ Invalid input! Enter a number")

if __name__=="__main__":
    main()
        
    
