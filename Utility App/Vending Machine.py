import time

products = {
    '1': {'name': 'Water', 'price': 1.00, 'stock': 10, 'type': 'Drinks'},
    '2': {'name': 'Coke', 'price': 2.00, 'stock': 12, 'type': 'Drinks'},
    '3': {'name': 'Pepsi', 'price': 2.00, 'stock': 15, 'type': 'Drinks'},
    '4': {'name': 'Coffee', 'price': 2.00, 'stock': 5, 'type': 'Hot Drinks'},
    '5': {'name': 'Tea', 'price': 2.00, 'stock': 8, 'type': 'Hot Drinks'},
    '6': {'name': 'Lays', 'price': 1.00, 'stock': 6, 'type': 'Snacks'},
    '7': {'name': 'Doritos', 'price': 1.00, 'stock': 12, 'type': 'Snacks'},
    '8': {'name': 'Snickers', 'price': 1.50, 'stock': 13, 'type': 'Chocolate'},
    '9': {'name': 'Mars', 'price': 1.50, 'stock': 15, 'type': 'Chocolate'}
}

good_combinations = {
    'Coffee': ['Mars', 'Snickers'],
    'Tea': ['Mars'],
    'Lays': ['Coke', 'Pepsi'],
    'Doritos': ['Coke', 'Pepsi']
}

def show_menu():
    print("\n===== VENDING MACHINE =====")
    for type in ['Drinks', 'Hot Drinks', 'Snacks', 'Chocolate']:
        print(f"\n--- {type} ---")
        for code, item in products.items():
            if item['type'] == type and item['stock'] > 0:
                print(f"{code}    | {item['name']:<9} | £{item['price']:.2f} | {item['stock']}")

def get_money():
    while True:
        try:
            money = float(input("\nPlease insert money (£): "))
            return money if money > 0 else print("Please insert some money!")
        except ValueError:
            print("That's not a valid amount!")

def get_choice(money):
    choice = input("\nEnter code number (or 'q' to quit): ")
    if choice.lower() == 'q': return None
    
    if choice in products:
        item = products[choice]
        if item['stock'] <= 0:
            print("Sorry, we are out of that!")
            return None
        if money >= item['price']:
            return choice
        print(f"Sorry, you need £{item['price']:.2f}, but only gave £{money:.2f}")
    else:
        print("Invalid code! Please try again.")
    return None

def suggest_another_item(item_name):
    if item_name in good_combinations:
        print("\nGreat choice! You might also like:")
        for suggestion in good_combinations[item_name]:
            for code, product in products.items():
                if product['name'] == suggestion and product['stock'] > 0:
                    print(f"- {suggestion} (Code: {code}, £{product['price']:.2f})")

def give_item(choice, money):
    item = products[choice]
    change = money - item['price']
    products[choice]['stock'] -= 1
    
    print("\nGetting your item ready...")
    time.sleep(1)
    print(f"\n*** Your {item['name']} has been dispensed! ***")
    return item['name'], change

def run_vending_machine():
    while True:
        show_menu()
        money = get_money()
        
        while money > 0:
            choice = get_choice(money)
            if not choice:
                print(f"\nHere's your money back: £{money:.2f}")
                break

            item_name, change = give_item(choice, money)
            print(f"Change: £{change:.2f}")
            suggest_another_item(item_name)
            
            if change > 0:
                if input("\nWant to buy something else with your change? (yes/no): ").lower() == 'yes':
                    money = change
                    show_menu()
                else:
                    break

        if input("\nWould you like to buy something else? (yes/no): ").lower() != 'yes':
            print("\nThanks for using our vending machine!")
            break

if __name__ == "__main__":
    print("Welcome to our vending machine!")
    run_vending_machine()