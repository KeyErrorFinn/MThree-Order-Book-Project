# Anjali and Finnley's Orderbook Project

import random # Used for generating a random ID for items
import datetime # Used to add a sold date to items
import streamlit as st
import time

st.html("""
    <style>
        .stMainBlockContainer {
            max-width:60rem;
        }
    </style>
    """
)


st.markdown("<h1 style='text-align: center;'>Anjali and Finnley's Orderbook</h1>", unsafe_allow_html=True)


def show_output_message(text_component, output_text, delay):
    text_component.markdown(output_text)
    time.sleep(delay)
    text_component.markdown("")
    
if "order_book" not in st.session_state:
    st.session_state.order_book = {}

def add_order(order_type, name, price, quantity):
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
    while generated_id in st.session_state.order_book:
        generated_id = str(random.randint(100000, 999999))
    
    # Adds all the details of the item to the order_book
    st.session_state.order_book[generated_id] = {
        "Name": name,
        "Order Type": order_type,
        "Price": price,
        "Quantity": quantity,
        "Time": datetime.datetime.now().time().strftime('%H:%M:%S')
    }

choice = st.selectbox(
    "What would you like to do?",
    ("Nothing", "Add Stock Order", "Mark item as sold"),
)

if choice == "Add Stock Order":
    st.subheader("-- Add Stock Order to Order Book --")
    # asset_type = st.selectbox(
    #     "Type of asset:",
    #     ("Stock", "Cryptocurrency", "Commodity")
    # )
    
    order_type = st.selectbox(
        "Buy or Sell:",
        ("Buy", "Sell")
    )

    def clear_inputs():
        st.session_state["name"] = ""
        st.session_state["price"] = ""
        st.session_state["quantity"] = ""

    name = st.text_input("Name of Stock (i.e. GOOG): ", key="name")
    quantity = st.text_input("Quantity of Stocks (i.e. 10): ", key="quantity")
    total_price = st.text_input("Total Price of Stocks (i.e. 1000): ", key="price")

    output_component = st.markdown("")

    def handle_submit():
        error_text = ""
        if name == "":
            error_text = ":red[You need to input a **Name**.]"
        elif total_price == "":
            error_text = ":red[You need to input a **Total Price**.]"
        elif not total_price.isdigit():
            error_text = ":red[The **Total Price** needs to be a **number**]"
        elif int(total_price) < 1:
            error_text = ":red[The **Total Price** needs to be **1 or higher**]"
        elif quantity == "":
            error_text = ":red[You need to input a **Quantity**.]"
        elif not quantity.isdigit():
            error_text = ":red[The **Quantity** needs to be a **number**]"
        elif int(quantity) < 1:
            error_text = ":red[The **Quantity** needs to be **1 or higher**]"

        if error_text != "":
            show_output_message(output_component, error_text, 2)
        else:
            add_order(order_type, name, total_price, quantity)
            show_output_message(output_component, f':green[**{quantity}x "{name}" ({order_type})** added at **{total_price}** per asset]', 3)
            clear_inputs()

    st.button("Submit", on_click=handle_submit)

st.divider()
order_book_container = st.container(border=True)
order_book_container.markdown("<h3 style='text-align: center;'>Order Book</h3>", unsafe_allow_html=True)
if len(st.session_state.order_book) == 0:
    order_book_container.text("Order book is empty")
else:
    buy_column, sell_column = order_book_container.columns(2, border=True)
    with buy_column:
        st.markdown("<h4 style='text-align: center;'>Buy Orders</h4>", unsafe_allow_html=True)
        
        time_column, name_column, qty_column, price_column = st.columns(4)
        time_column.markdown("<h5 style='text-align: center;'>Time</h5>", unsafe_allow_html=True)
        name_column.markdown("<h5 style='text-align: center;'>Name</h5>", unsafe_allow_html=True)
        qty_column.markdown("<h5 style='text-align: center;'>Qty</h5>", unsafe_allow_html=True)
        price_column.markdown("<h5 style='text-align: center;'>Bid</h5>", unsafe_allow_html=True)
        
        for order_id in st.session_state.order_book:
            order = st.session_state.order_book[order_id]
            if order["Order Type"] == "Buy":
                order_container = st.container(border=True)
                order_time_column, order_name_column, order_qty_column, order_price_column = order_container.columns(4)
                order_time_column.text(order["Time"])
                order_name_column.text(order["Name"])
                order_qty_column.text(order["Quantity"])
                order_price_column.text(order["Price"])
                
    with sell_column:
        st.markdown("<h4 style='text-align: center;'>Sell Orders</h4>", unsafe_allow_html=True)
        
        price_column, qty_column, name_column, time_column = st.columns(4 )
        price_column.markdown("<h5 style='text-align: center;'>Ask</h5>", unsafe_allow_html=True)
        qty_column.markdown("<h5 style='text-align: center;'>Qty</h5>", unsafe_allow_html=True)
        name_column.markdown("<h5 style='text-align: center;'>Name</h5>", unsafe_allow_html=True)
        time_column.markdown("<h5 style='text-align: center;'>Time</h5>", unsafe_allow_html=True)
        
        for order_id in st.session_state.order_book:
            order = st.session_state.order_book[order_id]
            if order["Order Type"] == "Sell":
                order_container = st.container(border=True)
                order_price_column, order_qty_column, order_name_column, order_time_column = order_container.columns(4)
                order_price_column.text(order["Price"])
                order_qty_column.text(order["Quantity"])
                order_name_column.text(order["Name"])
                order_time_column.text(order["Time"])

# order_book = {} # Blank dictionary to hold future data

# def add_order(asset_type, name, price, quantity):
#     """Adds items to the order_book

#     Args:
#         asset_type (string): The type of the asset
#         name (string): The name of the asset
#         price (string): The price of the asset
#         quantity (string): The quantity of the asset
#     """
    
#     # Generates a random ID between 100,000 and 999,999
#     generated_id = str(random.randint(100000, 999999))
#     # If the ID is already being used, keep generating till its unique
#     while generated_id in order_book:
#         generated_id = str(random.randint(100000, 999999))
    
#     # Adds all the details of the item to the order_book
#     order_book[generated_id] = {
#         "Name": name,
#         "Asset Type": asset_type,
#         "Price": price,
#         "Quantity": quantity,
#         "Sold": False,
#         "Date of Sale": None
#     }

# def mark_as_sold(item_id):
#     """Marks an item as sold

#     Args:
#         item_id (string): The unique ID of an item
#     """
    
#     # Makes all the information accessible with a variable
#     item_info = order_book[item_id]
#     # Marks the item as sold
#     item_info["Sold"] = True
#     # Adds todays date and time to the items info
#     item_info["Date of Sale"] = datetime.datetime.today()


# def show_orders(unsold_only=False):
#     """Displays all orders in the output

#     Args:
#         unsold_only (bool, optional): Decides whether it should only display unsold values. Defaults to False.
#     """
    
#     # Loops through each ID in the order_book
#     for id in order_book:
#         # Makes all the information accessible with a variable
#         item_info = order_book[id]
#         # Gets the name, price, quantity, sold, and date_of_sale information for the item
#         name = item_info["Name"]
#         asset_type = item_info["Asset Type"]
#         price = item_info["Price"]
#         quantity = item_info["Quantity"]
#         sold = item_info["Sold"]
#         date_of_sale = item_info["Date of Sale"]
        
#         sold_count = 0
        
#         if not sold or not unsold_only:
#             sold_count += 1
#             # Prints out each line with the data
#             print(f"{id}:")
#             print(f"  - Name: {name}")
#             print(f"  - type: {asset_type}")
#             print(f"  - Price: {price}")
#             print(f"  - Quantity: {quantity}")
#             # If its not showing only sold values, then show the Sold data
#             if not unsold_only:
#                 print(f"  - Sold: {sold}")
#                 print(f"  - Date of Sale: {date_of_sale}")
    
#     return sold_count > 0


# # Standard Python practice (I can provide explaination if needed)
# if __name__ == "__main__":
#     # Runs a while true loop to keep the program continous
#     while True:
#         # Shows the possible actions and lets the user decide what to do
#         print("""
# What would you like to do?:
# 1. Add asset
# 2. Mark item as sold
# 3. View Order Book
# 4. Exit
# """)
#         choice = input("Enter your choice (1, 2, 3, 4): ")
        
#         # If the user does not pick 1-4, they will be prompted again
#         while choice not in ["1", "2", "3", "4"]:
#             choice = input("Enter your choice (1, 2, 3, 4): ")
        
#         if choice == "1": # The 1st choice (Adding an item)
#             print("\n-- Add item to orderbook --")
#             # Gets the user to give the finance's name, price, and quantity with inputs
#             asset_types = {"1": "Stock", "2": "Cryptocurrency", "3": "Commodity"}
#             print("""Types of Assets:
# 1. Stock
# 2. Cryptocurrency
# 3. Commodity
# """)
#             asset_choice = input("What type of asset would you like to add?: ")
            
#             # If the user does not pick 1-4, they will be prompted again
#             while asset_choice not in ["1", "2", "3"]:
#                 asset_choice = input("What type of asset would you like to add?: ")
            
#             name = input(f"{asset_types[asset_choice]} Name: ")
#             price = input(f"{asset_types[asset_choice]} Price: ")
#             quantity = input(f"{asset_types[asset_choice]} Quantity: ")
            
#             # Runs the function "add_order" with the name, price, quantity
#             add_order(asset_types[asset_choice], name, price, quantity)
#             print(order_book)
#         elif choice == "2": # The 2nd choice (Marking an item as sold)
#             print("\n-- Mark item as sold --")
#             # Runs the function "show_orders" and sets "unsold_only" to True (to only show unsold items)
#             is_sellable_assets = show_orders(unsold_only=True)
            
#             if is_sellable_assets:
#                 print()
#                 # Makes a while loop where if the entered value is not in the order_book and is
#                 # not unsold, then it will reprompt the user
#                 valid_item_id = True
#                 while valid_item_id:
#                     item_id = input("Please select a valid ID to mark as sold: ")
                    
#                     # If the item ID given is in the order_book
#                     if item_id in order_book:
#                         # If the item is not marked as sold
#                         if order_book[item_id]["Sold"] == False:
#                             # Breaks the loop with this value change
#                             valid_item_id = False
            
#                 # Runs the function "mark_as_sold" with the item_id to mark the item as sold
#                 mark_as_sold(item_id)
#                 # Tells the user that the item has been marked as sold
#                 print(f"Marked {item_id} as sold\n")
#             else:
#                 print(f"There are currently no sellable assets\n")
#         elif choice == "3": # The 3rd choice (Showing all items)
#             print("\n-- Showing all orders --")
#             # Runs the function "show_orders" to show all items in order_book
#             show_orders()
#         elif choice == "4": # The 4th choice (Exiting the program)
#             print("\n-- Exiting Program --")
#             break