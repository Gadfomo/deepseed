inventory = { }

def add_item(inventory):
    name = input("Enter item name: ").strip().lower()
    if name in inventory:
        print("Please item already exist...")
        return
    try:
        price = float(input("Enter item price: "))
        stock = int(input("Enter stock quantity: "))
        category = input("Enter item category: ").strip().lower()
        inventory[name]= {"price": price, "stock": stock, "category": category}
        print(f"{name} added to inventory")
    except ValueError:
        print("Invalid input. price and stock must be numbers.")

def update_item(inventory):
    name = input("Enter item name: ").strip().lower()
    if name not in inventory:
        print(f"{name} item not found ..")
        return
    try:
        update = int(input("Enter what should be added or subtracted(can be positive or negative): "))
        new_stock = inventory[name]['stock'] + update

        if new_stock < 0:
            print("Price can't reduce below zero! ")
        else:
            inventory[name]['stock']= new_stock
            print(f"Update. {name} now has {new_stock} in stock")
    except ValueError:
        print("Invalid input. Entr whole number for stock change.")


def search_by_category(inventory):
    category = input("Enter categroy to search: ").strip().lower()
    found = False

    print(f"\n Items in category : {category}")

    for name, detail in inventory.items():
        if detail['category']== category:
            price = f"${detail['price']:.2f}"
            print(f" - {name}: price: {price}, stock: {detail}")
            found = True
        
    if not found:
        print("No items found i this category.")


def check_low_stock(inventory):
    print("\nLow Stock Items (5 units or less):")
    found = False

    for name, detail in inventory.items():
        if detail['stock'] <= 5:
            price = f"${detail['price']:.2f}"
            print(f"- {name.title()}: Price: {price}, Stock: {detail['stock']}, Category: {detail['category']}")
            found = True

    if not found:
        print("All items have sufficient stock.")

def calculate_total_value(inventory):
    total = 0

    for item in inventory.values():
        total += item['price'] * item['stock']
    
    print(f"\n total inventory value: ${total:.2f}")




while True:
        print("\n Inventory Manager Menu")
        print("1. Add new item")
        print("2. Update stock")
        print("3. Search items by category")
        print("4. Check low stock items")
        print("5. Calculate total inventory value")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ").strip()

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            update_item(inventory)
        elif choice == '3':
            search_by_category(inventory)
        elif choice == '4':
            check_low_stock(inventory)
        elif choice == '5':
            calculate_total_value(inventory)
        elif choice == '6':
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")
