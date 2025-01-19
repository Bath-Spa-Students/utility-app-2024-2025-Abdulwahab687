# Wahab's Vending Machine
# Made this for my store - keeps track of items and handles payments
# Note: Need to install tabulate package first!

from tabulate import tabulate
import time

# All my store items - keeping it simple and organized by type
store_items = {
    'Snacks': {
        'S1': {'name': 'Pringles Original', 'price': 2.50, 'left': 8},
        'S2': {'name': 'Doritos Cool Ranch', 'price': 2.00, 'left': 10},
        'S3': {'name': 'Snickers Bar', 'price': 1.50, 'left': 15},
        'S4': {'name': 'M&Ms Peanut', 'price': 1.50, 'left': 12},
        'S5': {'name': 'Oreos', 'price': 2.00, 'left': 8}
    },
    'Drinks': {
        'D1': {'name': 'Coca Cola', 'price': 1.50, 'left': 20},
        'D2': {'name': 'Sprite', 'price': 1.50, 'left': 15},
        'D3': {'name': 'Water Bottle', 'price': 1.00, 'left': 25},
        'D4': {'name': 'Orange Juice', 'price': 2.00, 'left': 10},
        'D5': {'name': 'Energy Drink', 'price': 2.50, 'left': 8}
    },
    'Fresh Items': {
        'F1': {'name': 'Sandwich', 'price': 3.50, 'left': 6},
        'F2': {'name': 'Fruit Cup', 'price': 2.50, 'left': 5},
        'F3': {'name': 'Yogurt', 'price': 1.50, 'left': 8},
        'F4': {'name': 'Salad Box', 'price': 4.00, 'left': 4}
    }
}

# Some items go well together - suggesting these to customers
combo_deals = {
    'Sandwich': ['Cola', 'Water Bottle'],
    'Pringles': ['Sprite', 'Cola'],
    'Salad Box': ['Water Bottle', 'Fruit Cup']
}

def show_welcome():
    # Simple welcome message
    print("\n=== WELCOME TO WAHAB'S VENDING MACHINE ===")
    print("Quality items at great prices!")
    print(f"Current time: {time.strftime('%I:%M %p')}")
    print("=" * 42)

def display_items():
    # Show all items nicely formatted
    for category in store_items:
        print(f"\n{category}:")
        table_data = []
        for code, item in store_items[category].items():
            # Only show items that are in stock
            if item['left'] > 0:
                table_data.append([
                    code,
                    item['name'],
                    f"${item['price']:.2f}",
                    item['left']
                ])
        print(tabulate(table_data, headers=['Code', 'Item', 'Price', 'Left'], tablefmt='simple'))

def get_money():
    # Handle money input
    while True:
        try:
            money = float(input("\nPlease insert money (or 0 to exit): $"))
            if money >= 0:
                return money
            print("Please enter a valid amount!")
        except ValueError:
            print("That's not a valid amount!")

def get_choice(money_left):
    # Let customer choose an item
    choice = input("\nEnter item code (or 'q' to quit): ").upper()
    
    if choice.lower() == 'q':
        return None, None
        
    # Look through all categories to find the item
    for category in store_items:
        if choice in store_items[category]:
            item = store_items[category][choice]
            
            # Check if we can sell this item
            if item['left'] <= 0:
                print("Sorry, we're out of that item!")
                return None, None
                
            if money_left < item['price']:
                print(f"You need ${item['price']:.2f}, but only have ${money_left:.2f}")
                return None, None
                
            return choice, category
    
    print("Sorry, couldn't find that item!")
    return None, None

def suggest_items(item_name):
    # Suggest items that go well together
    if item_name in combo_deals:
        print("\nGreat choice! These go well with it:")
        for suggested in combo_deals[item_name]:
            # Find and show the suggested item's price
            for category in store_items:
                for code, item in store_items[category].items():
                    if item['name'] == suggested and item['left'] > 0:
                        print(f"- {suggested} (${item['price']:.2f}, Code: {code})")

def run_store():
    while True:
        show_welcome()
        display_items()
        
        money = get_money()
        if money == 0:
            print("\nThanks for visiting Wahab's Vending Machine!")
            break
            
        while money > 0:
            choice, category = get_choice(money)
            
            if not choice:
                break
                
            # Process the sale
            item = store_items[category][choice]
            store_items[category][choice]['left'] -= 1
            money -= item['price']
            
            print(f"\nHere's your {item['name']}!")
            print(f"Money left: ${money:.2f}")
            
            suggest_items(item['name'])
            
            if money > 0:
                if input("\nWant to buy something else? (y/n): ").lower() != 'y':
                    print(f"\nHere's your change: ${money:.2f}")
                    break
            
        if input("\nStart new purchase? (y/n): ").lower() != 'y':
            print("\nThanks for shopping at Wahab's Vending Machine!")
            break

if __name__ == "__main__":
    try:
        run_store()
    except KeyboardInterrupt:
        print("\n\(Closing Wahab's Vending Machine... Come back soon!")
