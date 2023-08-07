import json

def load_data():
    try:
        with open('snacks_data.json', 'r') as file:
            snacks_data = json.load(file)
    except FileNotFoundError:
        snacks_data = []
    return snacks_data

def save_data(snacks_data):
    with open('snacks_data.json', 'w') as file:
        json.dump(snacks_data, file)

def add_snack(name, price, quantity):
    snacks_data = load_data()
    snack = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    snacks_data.append(snack)
    save_data(snacks_data)

def get_all_snacks():
    return load_data()

def update_snack(name, new_price=None, new_quantity=None):
    snacks_data = load_data()
    for snack in snacks_data:
        if snack['name'] == name:
            if new_price is not None:
                snack['price'] = new_price
            if new_quantity is not None:
                snack['quantity'] = new_quantity
            save_data(snacks_data)
            break

def delete_snack(name):
    snacks_data = load_data()
    snacks_data = [snack for snack in snacks_data if snack['name'] != name]
    save_data(snacks_data)

if __name__ == "__main__":
    while True:
        print("1. Add a snack")
        print("2. View all snacks")
        print("3. Update a snack")
        print("4. Delete a snack")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the snack name: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            add_snack(name, price, quantity)
        elif choice == '2':
            all_snacks = get_all_snacks()
            for snack in all_snacks:
                print(f"{snack['name']} - Price: ${snack['price']}, Quantity: {snack['quantity']}")
        elif choice == '3':
            name = input("Enter the snack name to update: ")
            new_price = float(input("Enter the new price (press Enter to skip): ") or None)
            new_quantity = int(input("Enter the new quantity (press Enter to skip): ") or None)
            update_snack(name, new_price, new_quantity)
        elif choice == '4':
            name = input("Enter the snack name to delete: ")
            delete_snack(name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
