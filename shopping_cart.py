print("==== Shopping List ====")
print("Enter an item to buy (type done -finish)\n")
cart=[]
total=0.0
while True:
    item=input("Item name (or type done):")
    if item.lower()=='done':
        break
    price=float(input(f"Enter the price of {item}:$"))
    cart.append((item,price))
    total+=price
    print(f"Item added!-The cart value ${total:.2f}\n")
print("====YOUR RECEPIT====")
print("-"*30)
for i,(item,price) in enumerate(cart,1):
    print(f"{i}.{item}:${total:.2f}\n")
print("-"*30)
print(f"Total:${total:.2f}\n")
print(f"Items purchased:{len(cart)}")
print("===Thank You for Shopping===")
