import os
def create_file():
    filename=input("Enter the filename(with .txt extension):")
    content=input("Enter the content to put in file:")

    with open(filename,'w') as file:
        file.write(content)
    print(f"File {filename} created sucessfully!")

def read_file():
    filename=input("Enter the filename to read(with .txt extension):")
    try:
        with open(filename,'r')as file:
            content=file.read()
        
        print(f"Content of {filename}")
        print("-"*40)
        print(content)
        print("-"*40)

    except FileNotFoundError:
        print(f"{filename} not found!")

def append_to_file():
    filename=input("Enter the filename to append(with .txt extension):")
    new_content=input("Enter the content to append:")

    try:
        with open(filename,'a') as file:
            file.write(f"\n"+new_content)
        print(f"Content appended to {filename}")
    except FileNotFoundError:
        print(f"{filename} not found!")

def count_lines():
    filename=input("Enter the filename to count lines:")
    try:
        with open(filename,'r')as file:
            lines=file.readlines()
        print(f"The no of lines of {filename} are {len(lines)}")
    except FileNotFoundError:
        print(f"{filename} not found!")

def delete_file():
    filename=input("Enter the file to delete or file path:")
    try:
        file_exists=os.path.exists(filename)
        if file_exists:
            os.remove(filename)
            print(f"{filename} deleted successfully!")
        else:
            print("Path does not Exist!")
    except FileNotFoundError:
        print(f"{filename} not found!")
def copy_new_file():
    filename=input("Enter the older filename(with .txt extension) to copy:")
    file_name=input("Enter the new filename(with .txt extension): ")
    try:
        with open(filename,'r') as file:
            lines=file.readlines()
            print(f"{filename} copied successfully!")
        with open(file_name,'w') as file:
            for line in lines:
                file.write(line)
            print("File copied successfully!")
        print(f"{file_name} copied content:")
        with open(file_name,'r') as file:
            content=file.read()
            print("-"*40)
            print(content)
            print("-"*40)
    except FileNotFoundError:
        print("Not found!")

def search_in_file():
    filename=input("Enter the filename(with .txt extension):")
    search_term=input("Enter the term to serach:")

    try:
        with open(filename,'r') as file:
            lines=file.readlines()

        found=False
        for num,line in enumerate(lines,1):
            if search_term in line:
                print(f"{num}:{line.strip()}")
                found=True
        if not found:
            print(f"{search_term} not found in file!")
    except FileNotFoundError:
        print("File not found!")




def display_menu():
    """Display main menu"""
    print("\n" + "=" * 40)
    print("TEXT FILE MANAGER")
    print("=" * 40)
    print("1. Create File")
    print("2. Read File")
    print("3. Append to File")
    print("4. Count Lines")
    print("5. Delete File")
    print("6. Copy File")
    print("7. Search in File")
    print("8. Exit")
    print("=" * 40)


# Main program loop
while True:
    display_menu()
    
    try:
        choice = int(input("\nEnter choice (1-8): "))
        
        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            append_to_file()
        elif choice == 4:
            count_lines()
        elif choice == 5:
            delete_file()
        elif choice == 6:
            copy_new_file()
        elif choice == 7:
            search_in_file()
        elif choice == 8:
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Choose 1-5")
            
    except ValueError:
        print("❌ Invalid input! Enter a number")
