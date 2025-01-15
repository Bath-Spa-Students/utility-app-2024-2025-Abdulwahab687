#importing the "tabulate" module, which helps organize the nested dictionary through its product class, code, item, cost, price and stock.
from tabulate import tabulate

#importing a "pyfiglet" module, which gives a text printed along this function to have a design
import pyfiglet
#importing a "fancify text" module, which gives a certain text a unique font within on bracketed () print statements and such.
from fancify_text import boldSerif, bold #type: ignore (to unclassify as a syntax error)

food_menu = { # nested dictionary, which is classified according to category (chips, chocolates.) as an outer key, with an inner key-value pair (code: product) .
    'Chips': { # a category part of a nested dictionary, with its inner key-value pair (code: product)
        'A1': {'Item': 'Lays Chips (Plain Salt)', 'Price': 8.00, 'Stock': 5},
        'A2': {'Item': 'Lays Chips (Tomato Ketchup)', 'Price': 8.00, 'Stock': 5},
        'A3': {'Item': 'Doritos (Nacho Cheese)', 'Price': 8.00, 'Stock': 5},
        'A4': {'Item': 'Doritos (Sweet Chili Pepper)', 'Price': 9.00, 'Stock': 5},
        'A5': {'Item': 'Cheetos (Flamin Hot Spicy)', 'Price': 10.00, 'Stock': 5},
        'B1': {'Item': 'Takis Blue Heat Fuego', 'Price': 14.00, 'Stock': 5},
        'B2': {'Item': 'Salad Chips', 'Price': 3.50, 'Stock': 5},

    },
    'Biscuit': {
        'B3': {'Item': 'Oreo Original Cookies', 'Price': 4.50, 'Stock': 5},
        'B4': {'Item': 'Milky Knots - Chocolate Coated', 'Price': 1.50, 'Stock': 8},
        'B5': {'Item': 'Bread Pan Buttered Toast', 'Price': 5.00, 'Stock': 8},
        'C1': {'Item': 'Marie Biscuits', 'Price': 3.00, 'Stock': 5},
        'C2': {'Item': 'McVities Digestives - Chocolate', 'Price': 12.50, 'Stock': 5},
        'C3': {'Item': 'Britannia Cake Rusk', 'Price': 8.00, 'Stock': 5},
        'C4': {'Item': 'Nagaraya Original', 'Price': 5.00, 'Stock': 5},
        'C5': {'Item': 'Ri-Chee Milk Snack', 'Price': 2.00, 'Stock': 5},

    },
    'Candy & Chocolate': {
        'D1': {'Item': 'Haribo Gummy Bears', 'Price': 11.00, 'Stock': 5},
        'D2': {'Item': 'Mentos Mint', 'Price': 1.00, 'Stock': 10},
        'D3': {'Item': 'Mentos Assorted Fruits Flavor', 'Price': 1.00, 'Stock': 10},
        'D4': {'Item': 'Skittles Fruits', 'Price': 3.00, 'Stock': 10},
        'D5': {'Item': 'Starburst', 'Price': 2.00, 'Stock': 10},
        'D6': {'Item': 'Snickers', 'Price': 3.00, 'Stock': 10},
        'D7': {'Item': 'Maltesers', 'Price': 4.00, 'Stock': 10},
        'D8': {'Item': 'Cadbury ', 'Price': 3.00, 'Stock': 10},
        'D9': {'Item': 'M&Ms Peanut Chocolate', 'Price': 3.00, 'Stock': 10},
        'D10':{'Item': 'KitKat', 'Price': 2.00, 'Stock': 10},
    },
'Cup Noodles' : {
        'E1' : {'Item': 'Indomie Beef Cup Noodles', 'Price': 4.00, 'Stock': 5},
        'E2' : {'Item': 'Indomie Fried BBQ & Chicken Cup', 'Price': 4.00, 'Stock': 5},
        'E3' : {'Item': 'Lucky Me! Chicken Mami Noodles', 'Price': 5.00, 'Stock': 5},
        'E4' : {'Item': 'Lucky Me! Supreme Go Bulalo ', 'Price': 5.00, 'Stock': 5},
        'E5' : {'Item': 'Samyang Buldak Ramen Cup', 'Price': 8.25, 'Stock': 5},
    }
}

beverage_menu = {  # nested dictionary, which is classified according to category (chips, chocolates.) as an outer key, with an inner key-value pair (code: product). 
    'Softdrinks': { # a category part of a nested dictionary, with its inner key-value pair (code: product)
        'F1' : {'Item': 'Coca-Cola ', 'Price': 2.50, 'Stock': 5},
        'F2' : {'Item': 'Sprite ', 'Price': 2.50, 'Stock': 5},
        'F3' : {'Item': 'Fanta Blueberry', 'Price': 2.50, 'Stock': 5},
        'F4' : {'Item': 'A&W Root Beer', 'Price': 4.00, 'Stock': 5},
        'F5' : {'Item': 'Chupa Chups Melon Cream Soda', 'Price': 10.00, 'Stock': 5},
    },
    'Juice and Water': {
        'F6' : {'Item': 'Al Marai Mango Juice', 'Price': 3.00, 'Stock': 10},
        'F7' : {'Item': 'Al Marai Orange Juice', 'Price': 3.00, 'Stock': 10},
        'F8' : {'Item': 'Al Marai Apple Juice', 'Price': 3.00, 'Stock': 10},
        'F9' : {'Item': 'Aquafina Water ', 'Price': 1.00, 'Stock': 10},
        'F10' : {'Item': 'Evian Natural Water', 'Price': 6.00, 'Stock': 5}
    },
    'Iced Coffee': {
        'G1' : {'Item': 'Al Marai One Bean Spanish Latte', 'Price': 8.50, 'Stock': 5},
        'G2' : {'Item': 'StarBucks Frappucino Cookies & Cream', 'Price': 10.50, 'Stock': 5},
        'G3' : {'Item': 'StarBucks Frappucino Vanilla Coffee', 'Price': 11.50, 'Stock': 5},
        'G4' : {'Item': 'Balade Farms Cafe Frappe Low Fat', 'Price': 6.50, 'Stock': 5},
        'G5' : {'Item': 'Nescafe Latte Iced Coffee ', 'Price': 7.50, 'Stock': 5}
    },
    'Energy & Sports Drinks' :{
        'G6' : {'Item': 'Red Bull Energy Drink Sugar Free', 'Price': 10.00, 'Stock': 5},
        'G7' : {'Item': 'Monster Green Energy Drink ', 'Price': 13.50, 'Stock': 5},
        'G8' : {'Item': 'PRIME Ice Pop Hydration Drink', 'Price': 15.00, 'Stock': 5},
        'G9' : {'Item': 'Pocari Sweat Drink', 'Price': 4.50, 'Stock': 5},
        'G10' : {'Item': 'Gatorade Blue Bolt', 'Price': 5.00, 'Stock': 5}
    }
}     

product_menu = {**food_menu, **beverage_menu} # merging both dictionaries into one variable (for easier handling on functions)

cash_input = float(input(boldSerif("Please Enter Cash:")))  #cash input 

item_header = ['Code', 'Item', 'Price', 'Stock'] # to group and classify the inner key-value pair (code-product)


#function for tabulating the food_menu dict
def display_food_items(): #declaring the function
    for category, items in food_menu.items(): # for loop that classifies the outer key (category: chips)
        print(f"{category.capitalize()}: ") # displaying the outer key (chips, chocolates)
        table = [] # table shape
        for code_item, details in items.items(): # for loop to classify and display the inner key-value pair (code-product)
            table.append([code_item.capitalize(), details['Item'], f"{details['Price']} AED", details['Stock']]) # appending the nested dict loops into the table
        print(tabulate(table, headers=item_header, tablefmt="pretty")) # setting up the tabulate module, with its headers and design.

#function for tabulating the beverage_menu dict
def display_beverage_items(): #declaring the function
    for category, items in beverage_menu.items(): # for loop that classifies the outer key (category: chips)
        print(f"{category.capitalize()}: ") # displaying the outer key (chips, chocolates)
        table = [] # table shape
        for code_item, details in items.items(): # for loop to classify and display the inner key-value pair (code-product)
            table.append([code_item.capitalize(), details['Item'], f"{details['Price']} AED", details['Stock']]) # appending the nested dict loops into the table
        print(tabulate(table, headers=item_header, tablefmt="pretty")) # setting up the tabulate module, with its headers and design.

#function for accessing the input codes
def get_product_items(menu, code): 
    for category, items in menu.items(): # for loop that classifies checks  the outer key, and its inner key nested (to check if code is valid and accessible. )
        if code in items: # if code input checked  is within the dictionary, it take its contents and info
            return items[code] #returns the info if the code exists
    return None # returns nothing if the code does not exists

#function for stocking system on purchases
def purchase_items(product, amount):
    product['Stock'] -= amount  # an operation which subtracts per purchase of a specific product

#function for the menu selection option
def selection(cash_left):
    # message for selection option
    option_msg = (bold(f"\n1. Food\n2. Beverage"))
    selection_msg = int(input(f"{option_msg}\nPlease Enter a Selection option (1 or 2): "))
    #if-else statement to display the menu if input is according to the message.
    if selection_msg == 1:
        display_food_items()
        code(cash_left)
    elif selection_msg == 2:
        display_beverage_items()
        code(cash_left)
    #shows message if input is invalid
    else:
        print("Invalid number input. Please try again.")
    #returns the value from the cash_left variable (for tracking amount of cash when switching menu)
    return cash_left  

# function for the code input and main purchases(the key element of a vending machine proccess)
def code(cash_left):
    #while loop that iterates itself until program ends
    while True:
        # input statement for purchase through the code of a product (inner key)
        code_input = input("Please Enter Item Code to Purchase (enter 'quit' to exit): ").upper()

        #fethcing the information product_menu merged dict through the function for ACCESSING INPUT CODES, which compares from the input statement if it is valid.
        code_item = get_product_items(product_menu, code_input)
        cash_subtract = cash_left # transfers the contents from the cash_left variable to the cash_subtract variable (for a subtraction operation for purchase).
        #if-else statement for either menu switch or to end program. 
        if code_input.lower() == "quit": 
            additional_purchase = input("""Would you like to buy more from another menu? 
                                    (yes - switch menu 
                                    no - print receipt):""") 
            
            if additional_purchase.lower() == "yes": # if user enters yes, the program directs back to the selection function
                selection(cash_left)

            elif additional_purchase.lower() == "no": # if user enters no, then the program prints statement with its goodbye message and its remaining cash
                print(f"Thank you for using our vending machine. Your remaining change is {cash_left}. Have a great time.")
                break

            else: # else statement for any other input besides its required input, which proceeds to the program again
                print("Invalid input, please type yes or no.")
                continue

        #if-else statement for handling purchase 
        #if statement that handles the stock system by removing 1 from the chosen product purchase
        if code_item and code_item['Stock'] > 0 and cash_subtract >= code_item['Price']:
            purchase_items(code_item, 1)
            cash_left -= code_item['Price'] # subtracts the currrent cash variable according to the item price
            #print statement that displays the item purchase and its cost.
            print(f"You have purchased {code_item['Item']} for {code_item['Price']} AED.")
            #print statement for the remaining cash left
            print(f"You still have {cash_left} AED remaining. ")

        #if statement for a purchase, but the amount of cash is not enough 
        elif code_item and code_item['Price'] > cash_subtract:
            print("Not enough amount of cash, please purchase another.")
        #if statement for a purchase, but the item is out of stock
        elif code_item and code_item['Stock'] == 0:
            print("Sorry, the item you are choosing is out of stock.")

        #else statement for any invalid input
        else:
            print("Invalid code input, please try again. ")
        
        
    #returns the value from the cash_left variable (for tracking amount of cash when switching menu)        
    return cash_left

#message variable for the introduction menu 
message = pyfiglet.figlet_format("WELCOME! TO HANNI PHAM ' S VENDING MACHINE")
print(message)

# while loop that iterates cash_input being passed unto two functions called selection and code.
while True:
    selection(cash_input)
    code(cash_input)