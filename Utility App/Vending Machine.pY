import time
import random
from datetime import datetime

products = {
    'A1': {'name': '🍷 Elderberry Wine', 'price': 4.50, 'stock': 8, 'category': 'Artisanal Drinks'},
    'A2': {'name': '🫖 Jasmine Pearl Tea', 'price': 3.50, 'stock': 10, 'category': 'Artisanal Drinks'},
    'A3': {'name': '☕ Turkish Coffee', 'price': 3.00, 'stock': 7, 'category': 'Artisanal Drinks'},
    'B1': {'name': '🍫 Dark Truffle', 'price': 2.50, 'stock': 15, 'category': 'Confections'},
    'B2': {'name': '🍬 Rose Turkish Delight', 'price': 3.00, 'stock': 12, 'category': 'Confections'},
    'B3': {'name': '🍪 Lavender Shortbread', 'price': 2.50, 'stock': 9, 'category': 'Confections'},
    'C1': {'name': '📜 Fortune Scroll', 'price': 1.00, 'stock': 20, 'category': 'Curiosities'},
    'C2': {'name': '🎭 Mystery Box', 'price': 5.00, 'stock': 5, 'category': 'Curiosities'},
    'C3': {'name': '✨ Wishing Coin', 'price': 2.00, 'stock': 15, 'category': 'Curiosities'}
}

perfect_pairings = {
    'Turkish Coffee': ['Dark Truffle', 'Rose Turkish Delight'],
    'Jasmine Pearl Tea': ['Lavender Shortbread'],
    'Elderberry Wine': ['Dark Truffle'],
    'Mystery Box': ['Fortune Scroll']
}

fortunes = [
    "A pleasant surprise is waiting for you.",
    "Your creativity will bring you great joy.",
    "An old friend will bring new opportunities.",
    "The path less traveled will reward you.",
    "A small gift will lead to great happiness."
]

def print_vintage_border():
    print("\n" + "★·.·´¯`·.·★" * 8)

def print_aesthetic_header():
    current_time = datetime.now().strftime("%H:%M")
    print(f"\n═══════ ⟦ CURIOSITY DISPENSARY ⟧ ═══════")
    print(f"       Time Stands at {current_time}")
    print("    'Purveyor of Uncommon Delights'")

def display_catalogue():
    print_aesthetic_header()
    for category in ['Artisanal Drinks', 'Confections', 'Curiosities']:
        print(f"\n✧ {category} ✧")
        print("─" * 45)
        for code, item in products.items():
            if item['category'] == category and item['stock'] > 0:
                print(f"{code} | {item['name']:<20} | £{item['price']:<5} | {item['stock']} left")
    print_vintage_border()

def accept_payment():
    while True:
        try:
            print("\nKindly deposit your coins and notes...")
            payment = float(input("£ "))
            if payment <= 0:
                print("⚠ The machine requires proper payment to operate.")
                continue
            return payment
        except ValueError:
            print("⚠ The machine cannot process this form of payment.")

def select_item(available_funds):
    choice = input("\nPlease select your desire (or 'Q' to quit): ").upper()
    if choice == 'Q':
        return None
    
    if choice in products:
        item = products[choice]
        if item['stock'] <= 0:
            print("※ Regrettably, this item is no longer available.")
            return None
        if available_funds >= item['price']:
            return choice
        print(f"※ This item requires £{item['price']:.2f}, but you've provided £{available_funds:.2f}")
    else:
        print("※ The machine does not recognize this selection.")
    return None

def suggest_complementary_items(item_name):
    if item_name in perfect_pairings:
        print("\n✧ The machine whispers a suggestion ✧")
        print("These items are known to pair wonderfully:")
        for suggestion in perfect_pairings[item_name]:
            for code, product in products.items():
                if product['name'].endswith(suggestion) and product['stock'] > 0:
                    print(f"❥ {suggestion} ({code}: £{product['price']:.2f})")

def dispense_item(choice, payment):
    item = products[choice]
    change = payment - item['price']
    products[choice]['stock'] -= 1
    
    print("\nThe mechanisms whir to life...")
    time.sleep(1)
    print("．．．．．．．．．")
    time.sleep(0.5)
    
    if item['name'].startswith('📜'):
        print(f"\n✧ Your fortune scroll unfurls ✧")
        print(f"「 {random.choice(fortunes)} 」")
    elif item['name'].startswith('🎭'):
        print("\n✧ The mystery box reveals ✧")
        surprises = ["a tiny brass key", "a peculiar stone", "a pressed flower", 
                    "a curious coin", "a small crystal"]
        print(f"「 {random.choice(surprises)} 」")
    else:
        print(f"\n✧ Your {item['name']} materializes ✧")
    
    return item['name'], change

def operate_machine():
    while True:
        display_catalogue()
        payment = accept_payment()
        
        while payment > 0:
            choice = select_item(payment)
            if not choice:
                print(f"\nReturning £{payment:.2f}")
                break

            item_name, change = dispense_item(choice, payment)
            if change > 0:
                print(f"\nYour change: £{change:.2f}")
            suggest_complementary_items(item_name)
            
            if change > 0:
                if input("\nWould you like to make another selection with your change? (Y/N): ").upper() == 'Y':
                    payment = change
                    display_catalogue()
                else:
                    break
            else:
                break

        if input("\nWould you care to make another purchase? (Y/N): ").upper() != 'Y':
            print("\n✧ Thank you for visiting the Curiosity Dispensary ✧")
            print("May your selections bring you joy and wonder.")
            break

if __name__ == "__main__":
    print_vintage_border()
    print("Welcome to the Curiosity Dispensary")
    print("Where the Ordinary Becomes Extraordinary")
    print_vintage_border()
    operate_machine()
