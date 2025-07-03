# Anjali and Finnley's Orderbook Project

import random # Used for generating a random ID for items
import datetime # Used to add a sold date to items


order_book = {} # Blank dictionary to hold future data

def add_order(asset_type, name, price, quantity):
    """Adds items to the order_book

    Args:
        asset_type (string): The type of the asset
        name (string): The name of the asset
        price (string): The price of the asset
        quantity (string): The quantity of the asset
    """
    
    # Generates a random ID between 100,000 and 999,999
    generated_id = str(random.randint(100000, 999999))
    # If the ID is already being used, keep generating till its unique
    while generated_id in order_book:
        generated_id = str(random.randint(100000, 999999))
    
    # Adds all the details of the item to the order_book
    order_book[generated_id] = {
        "Name": name,
        "Asset Type": asset_type,
        "Price": price,
        "Quantity": quantity,
        "Sold": False,
        "Date of Sale": None
    }

def mark_as_sold(item_id):
    """Marks an item as sold

    Args:
        item_id (string): The unique ID of an item
    """
    
    # Makes all the information accessible with a variable
    item_info = order_book[item_id]
    # Marks the item as sold
    item_info["Sold"] = True
    # Adds todays date and time to the items info
    item_info["Date of Sale"] = datetime.datetime.today()


def show_orders(unsold_only=False):
    """Displays all orders in the output

    Args:
        unsold_only (bool, optional): Decides whether it should only display unsold values. Defaults to False.
    """
    
    # Loops through each ID in the order_book
    for id in order_book:
        # Makes all the information accessible with a variable
        item_info = order_book[id]
        # Gets the name, price, quantity, sold, and date_of_sale information for the item
        name = item_info["Name"]
        asset_type = item_info["Asset Type"]
        price = item_info["Price"]
        quantity = item_info["Quantity"]
        sold = item_info["Sold"]
        date_of_sale = item_info["Date of Sale"]
        
        sold_count = 0
        
        if not sold or not unsold_only:
            sold_count += 1
            # Prints out each line with the data
            print(f"{id}:")
            print(f"  - Name: {name}")
            print(f"  - type: {asset_type}")
            print(f"  - Price: {price}")
            print(f"  - Quantity: {quantity}")
            # If its not showing only sold values, then show the Sold data
            if not unsold_only:
                print(f"  - Sold: {sold}")
                print(f"  - Date of Sale: {date_of_sale}")
    
    return sold_count > 0


# Standard Python practice (I can provide explaination if needed)
if __name__ == "__main__":
    # Runs a while true loop to keep the program continous
    while True:
        # Shows the possible actions and lets the user decide what to do
        print("""
What would you like to do?:
1. Add asset
2. Mark item as sold
3. View Order Book
4. Exit
""")
        choice = input("Enter your choice (1, 2, 3, 4): ")
        
        # If the user does not pick 1-4, they will be prompted again
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Enter your choice (1, 2, 3, 4): ")
        
        if choice == "1": # The 1st choice (Adding an item)
            print("\n-- Add item to orderbook --")
            # Gets the user to give the finance's name, price, and quantity with inputs
            asset_types = {"1": "Stock", "2": "Cryptocurrency", "3": "Commodity"}
            print("""Types of Assets:
1. Stock
2. Cryptocurrency
3. Commodity
""")
            asset_choice = input("What type of asset would you like to add?: ")
            
            # If the user does not pick 1-4, they will be prompted again
            while asset_choice not in ["1", "2", "3"]:
                asset_choice = input("What type of asset would you like to add?: ")
            
            name = input(f"{asset_types[asset_choice]} Name: ")
            price = input(f"{asset_types[asset_choice]} Price: ")
            quantity = input(f"{asset_types[asset_choice]} Quantity: ")
            
            # Runs the function "add_order" with the name, price, quantity
            add_order(asset_types[asset_choice], name, price, quantity)
            print(order_book)
        elif choice == "2": # The 2nd choice (Marking an item as sold)
            print("\n-- Mark item as sold --")
            # Runs the function "show_orders" and sets "unsold_only" to True (to only show unsold items)
            is_sellable_assets = show_orders(unsold_only=True)
            
            if is_sellable_assets:
                print()
                # Makes a while loop where if the entered value is not in the order_book and is
                # not unsold, then it will reprompt the user
                valid_item_id = True
                while valid_item_id:
                    item_id = input("Please select a valid ID to mark as sold: ")
                    
                    # If the item ID given is in the order_book
                    if item_id in order_book:
                        # If the item is not marked as sold
                        if order_book[item_id]["Sold"] == False:
                            # Breaks the loop with this value change
                            valid_item_id = False
            
                # Runs the function "mark_as_sold" with the item_id to mark the item as sold
                mark_as_sold(item_id)
                # Tells the user that the item has been marked as sold
                print(f"Marked {item_id} as sold\n")
            else:
                print(f"There are currently no sellable assets\n")
        elif choice == "3": # The 3rd choice (Showing all items)
            print("\n-- Showing all orders --")
            # Runs the function "show_orders" to show all items in order_book
            show_orders()
        elif choice == "4": # The 4th choice (Exiting the program)
            print("\n-- Exiting Program --")
            break