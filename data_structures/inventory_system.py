inventory = {
    "LAPTOP001": {"name": "Laptop", "quantity": 10, "price": 50000},
    "PHONE001": {"name": "Smartphone", "quantity": 25, "price": 25000},
    "TABLET001": {"name": "Tablet", "quantity": 15, "price": 30000}
}

def add_product():
    code=input("Enter the code:").upper()
    if code in inventory:
        print("Product code already exists!")
        return
    inventory[code]={
        'name':input("Name:"),
        'quantity':int(input("Quantity:")),
        'price':float(input("Price:"))
    }
    print(f"Product {code} added!")

def update_stock(code,quantity_change):
    if code not in inventory:
        print("Product not found!")
        return
    inventory[code]['quantity']+=quantity_change
    print(f"Stock Updated!New Quantity:{inventory[code]['quantity']}")

def view_product(code):
    if code not in inventory:
        print("Product not found!")
        return
    product=inventory[code]
    print(f"\n{'='*40}")
    print(f"Code:{code}")
    print(f"Name:{product['name']}")
    print(f"Quantity:{product['quantity']}")
    print(f"Price:{product['price']}")
    print(f"Total_value:{product['quantity']*product['price']}")
    print(f"\n{'='*40}")
    

def list_all_products():
    if not inventory:
        print("Inventory is empty!")
        return
    print("\n====Inventory====")
    print(f"{'Code':<12}{'Name':<15}{'Qty':<8} {'Price':<12} {'Value'}")
    print("-" * 60)
    total_value=0
    for code,product in inventory.items():
        value=product['quantity']*product['price']
        total_value+=value
        print(f"{code:<12} {product['name']:<15} {product['quantity']:<8} ${product['price']:<11} ${value}")
    print("-" * 60)
    print(f"{'TOTAL VALUE:':<47} ${total_value}")

def low_stock_alert(threshold=5):
    low_stock={code:pro for code,pro in inventory.items() if pro['quantity']<=5}
    if not low_stock:
        print(f"No items below {threshold} units!")
        return
    print(f"\n LOW STOCK ALERT (≤{threshold} units)")

    for code ,prod in low_stock.items():
        print(f"  {code}: {prod['name']} - {prod['quantity']} left")


def search_products(keyword):
    results={code:prod for code,prod in inventory.items()
            if keyword.lower()in prod['name'].lower()}
    if not results:
        print(f"No products found with '{keyword}'")
        return
    print(f"Found {len(results)} Products:")
    for code, prod in results.items():
        print(f"  {code}: {prod['name']} (₹{prod['price']})")
while True:
    print("\n=== INVENTORY MANAGEMENT ===")
    print("1. Add Product")
    print("2. Update Stock")
    print("3. View Product")
    print("4. List All Products")
    print("5. Low Stock Alert")
    print("6. Search Products")
    print("7. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        code = input("Product code: ").upper()
        change = int(input("Quantity change (+/-): "))
        update_stock(code, change)
    elif choice == "3":
        code = input("Product code: ").upper()
        view_product(code)
    elif choice == "4":
        list_all_products()
    elif choice == "5":
        threshold = int(input("Low stock threshold (default 5): ") or "5")
        low_stock_alert(threshold)
    elif choice == "6":
        keyword = input("Search keyword: ")
        search_products(keyword)
    elif choice == "7":
        print(f"\n Inventory Summary:")
        print(f"   Total products: {len(inventory)}")
        break
    

    






