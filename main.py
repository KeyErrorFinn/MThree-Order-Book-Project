# Anjali and Finnley's Orderbook Project

import random # Used for generating a random ID for items
import datetime # Used to add a time to items
import streamlit as st # Allows for the code to be in website form
import time # Used for delays
import randomcolor # Used to add random colours to stocks


# Makes dictionaries that persist with reruns
if "order_book" not in st.session_state:
    # st.session_state.order_book = {}  # Blank dictionary
    st.session_state.order_book = {'647493': {'Name': 'GOOF', 'Order Type': 'Buy', 'Price': '100.5', 'Quantity': '14', 'Time': '16:19:44', 'Colour': '#c1ea62'}, '140485': {'Name': 'LOOG', 'Order Type': 'Buy', 'Price': '42', 'Quantity': '54', 'Time': '16:19:59', 'Colour': '#c5d613'}, '898995': {'Name': 'POOL', 'Order Type': 'Buy', 'Price': '100.5', 'Quantity': '10', 'Time': '16:20:21', 'Colour': '#c1ea62'}, '590681': {'Name': 'CHUG', 'Order Type': 'Sell', 'Price': '10', 'Quantity': '146', 'Time': '16:20:39', 'Colour': '#028731'}, '710770': {'Name': 'SMOG', 'Order Type': 'Sell', 'Price': '20.3', 'Quantity': '82', 'Time': '16:21:01', 'Colour': '#e19ced'}, '841518': {'Name': 'LUGG', 'Order Type': 'Sell', 'Price': '20.3', 'Quantity': '34', 'Time': '16:21:36', 'Colour': '#e19ced'}, '877877': {'Name': 'POAV', 'Order Type': 'Sell', 'Price': '10', 'Quantity': '132', 'Time': '16:22:00', 'Colour': '#028731'}, '565237': {'Name': 'POAV', 'Order Type': 'Sell', 'Price': '10', 'Quantity': '132', 'Time': '17:28:42', 'Colour': '#028731'}, '601541': {'Name': 'POAV', 'Order Type': 'Buy', 'Price': '154', 'Quantity': '43', 'Time': '19:21:15', 'Colour': '#30c9a8'}, '272181': {'Name': 'POAV', 'Order Type': 'Buy', 'Price': '10', 'Quantity': '132', 'Time': '19:22:25', 'Colour': '#028731'}, '175129': {'Name': 'POAV', 'Order Type': 'Sell', 'Price': '43', 'Quantity': '28', 'Time': '15:42:25', 'Colour': "#B13FC5"}}
if "order_book_colours" not in st.session_state:
    # st.session_state.order_book_colours = {}  # Blank dictionary
    st.session_state.order_book_colours = {'100.5': '#c1ea62', '42': '#c5d613', '10': '#028731', '20.3': '#e19ced', '154': '#30c9a8', '153': '#d18a4d'}


# Adds custom colour classes to colour stocks in the order book section
colour_css_classes = ""
# For each order in the order_book, assign the order_id the item's custom colour
for order_id in st.session_state.order_book:
    order = st.session_state.order_book[order_id]
    # Changes the background colour of the parent element to the stock
    colour_css_classes += f"""
        div:has(> .st-key-{order_id}) {'{'}
            background-color: {order['Colour']}66
        {'}'}
"""

# Makes the main content a bit wider and adds the custom colour classes
st.html(f"""
    <style>
        .stMainBlockContainer {"{"}
            max-width:60rem;
        {"}"}
        {colour_css_classes}
    </style>
    """
)


# Sets the page title and adds a header to the content
st.set_page_config(page_title="Anjali and Finnley's Orderbook")
st.markdown("<h1 style='text-align: center;'>Anjali and Finnley's Orderbook</h1>", unsafe_allow_html=True)


def show_output_message(text_component, output_text, delay):
    """Shows and hides a success or error message.

    Args:
        text_component (any): The text component to display the text.
        output_text (string): The markdown text that will displayed.
        delay (int): The time between showing and hiding the text.
    """
    text_component.markdown(output_text)
    time.sleep(delay)
    text_component.markdown("")


def is_float(value):
    """Checks if a value is a float or not.

    Args:
        value (any): The value to be checked.

    Returns:
        bool: Whether the value is a float or not.
    """
    # If the value is None, return False
    if value is None: 
        return False
    
    # Tries to convert the value to a float, success=True, fail=False
    try:
        float(value)
        return True
    except ValueError:
        return False

def add_order(order_type, name, price, quantity):
    """Adds items to the order_book.

    Args:
        asset_type (string): The type of the asset.
        name (string): The name of the asset.
        price (string): The price of the asset.
        quantity (string): The quantity of the asset.
    """
    
    # Generates a random ID between 100,000 and 999,999
    generated_id = str(random.randint(100000, 999999))
    # If the ID is already being used, keep generating till its unique
    while generated_id in st.session_state.order_book:
        generated_id = str(random.randint(100000, 999999))
    
    # Checks if the stock's price is already linked to a colour or not
    if price not in st.session_state.order_book_colours: # If not, generates a unique random colour for the price
        colour = randomcolor.RandomColor().generate()[0]
        while colour in st.session_state.order_book_colours.values():
            colour = randomcolor.RandomColor().generate()[0]
        
        st.session_state.order_book_colours[price] = colour
    else: # If it is, uses the already stored colour
        colour = st.session_state.order_book_colours[price]
        
    # Adds all the details of the item to the order_book
    st.session_state.order_book[generated_id] = {
        "Name": name,
        "Order Type": order_type,
        "Price": price,
        "Quantity": quantity,
        "Time": datetime.datetime.now().time().strftime('%H:%M:%S'),
        "Colour": colour
    }

def process_order_exchange(selected_stock_only_order_book):
    """Removes a Buy or Sell order from order_book.

    Args:
        selected_stock_only_order_book (dict): A dictionary of the selected stock(s).
    """
    # Sorts the dictionary of stocks by oldest to newest
    sorted_selected_stock_only_order_book = dict(sorted(selected_stock_only_order_book.items(), key=lambda item: item[1]['Time']))
    # Selects the oldest stock
    oldest_selected_stock = list(sorted_selected_stock_only_order_book.keys())[0]
    # Removes the stock from the order_book
    st.session_state.order_book.pop(oldest_selected_stock)


# Choice select box for what the user can do
choice = st.selectbox(
    "What would you like to do?",
    ("-", "➕ Add Stock Order", "📈 Purchase Sell Order", "💸 Sell to Buy Order"),
)

# If the user selects "➕ Add Stock Order", show the following content
if choice == "➕ Add Stock Order":
    # Smaller header for this section
    st.subheader("-- Add Stock Order to Order Book --")
    
    # Lets the user decide if they want to add a Buy or Sell Stock Order
    order_type = st.selectbox(
        "Buy or Sell:",
        ("Buy", "Sell")
    )

    # Function to clear inputs once the order is submitted
    def clear_inputs():
        st.session_state["name"] = ""
        st.session_state["price"] = ""
        st.session_state["quantity"] = ""

    # Lets the user type the information of the stock they want to Buy or Sell
    name = st.text_input("Name of Stock (i.e. GOOG): ", key="name").upper()
    quantity = st.text_input("Quantity of Stocks (i.e. 10): ", key="quantity")
    total_price = st.text_input("Total Price of Stocks (i.e. 1000): ", key="price")

    def handle_submit():
        """Handles several types of error checking once the submit button is pressed
        """
        # Error checks
        error_text = ""
        if name == "":
            error_text = ":red[You need to input a **Name**.]"
        elif total_price == "":
            error_text = ":red[You need to input a **Total Price**.]"
        elif quantity == "":
            error_text = ":red[You need to input a **Quantity**.]"
        elif not quantity.isdigit():
            error_text = ":red[The **Quantity** needs to be a **number**]"
        elif int(quantity) < 1:
            error_text = ":red[The **Quantity** needs to be **1 or higher**]"
        elif not is_float(total_price):
            error_text = ":red[The **Total Price** needs to be a **number**]"
        elif float(total_price) <= 0:
            error_text = ":red[The **Total Price** needs to be **1 or higher**]"

        # Checks to see if there were any errors, and if not, then proceed
        if error_text != "":
            # Shows an error message
            show_output_message(output_component, error_text, 2)
        else:
            # Adds an order to the order book using a function
            add_order(order_type, name, total_price, quantity)
            # Shows a success message
            show_output_message(output_component, f':green[**{quantity}x "{name}" ({order_type})** added at **{total_price}** per asset]', 3)
            # Clears the inputs after submitting
            clear_inputs()

    # Creates the submit button
    st.button("Submit", on_click=handle_submit)
    # The text component to show an error or success message
    output_component = st.markdown("")

# If the user selects "📈 Purchase Sell Order" or "💸 Sell to Buy Order", show the following content
elif choice in ["📈 Purchase Sell Order", "💸 Sell to Buy Order"]:
    # Removes the emoji from the choice string
    choice = choice[2:]

    # Smaller header for this section
    st.subheader(f"-- {choice} from Order Book --")

    # Makes the code dynamic and has values depending on the choice selected
    choice_meaning = {"Purchase Sell Order": ["Sell", "Ask", False], "Sell to Buy Order": ["Buy", "Bid", True]}

    # Function to clear inputs once stock is sold or bought
    def clear_inputs():
        st.session_state["stock_name"] = "-"
        st.session_state["stock_info"] = "-"

    # Filters the order books to only have order type values based on the choice (Sell or Buy)
    choice_only_order_book = {order_id: order for order_id, order in st.session_state.order_book.items() if order['Order Type'] == choice_meaning[choice][0]}
    # Makes a list of stock names from the filtered list
    all_sale_names = set(["-"] + [choice_only_order_book[order]["Name"] for order in choice_only_order_book])
    # Shows the stock names in a select box
    stock_name = st.selectbox(
        "Name of Stock:",
        all_sale_names,
        key="stock_name"
    )
    
    # If the stock name has been selected, show the "Stock Ask Price and Shares" option, else sets stock_info to default value
    if stock_name != "-":
        # Filters the choice filtered dictionary to only have stocks that have the same name as in stock_name
        stock_name_only_order_book = {order_id: order for order_id, order in choice_only_order_book.items() if order['Name'] == stock_name}
        # Sorts the stock_name filtered dictionary by price, "Purchase Sell Order" = Lowest to Highest, "Sell to Buy Order" = Highest to Lowest
        sorted_stock_name_only_order_book = dict(sorted(stock_name_only_order_book.items(), key=lambda item: float(item[1]['Price']), reverse=choice_meaning[choice][2]))
        # Provides the Ask/Bid price along with the Shares in a list
        all_stock_name_info = list(dict.fromkeys(["-"] + [f"{choice_meaning[choice][1]}: {sorted_stock_name_only_order_book[order]['Price']} | Shares: {sorted_stock_name_only_order_book[order]['Quantity']}" for order in sorted_stock_name_only_order_book]))
        # Shows that stock info in a select box
        stock_info = st.selectbox(
            f"Stock {choice_meaning[choice][1]} Price and Shares:",
            all_stock_name_info,
            key="stock_info"
        )
    else:
        # Sets stock_info to the default value
        stock_info = "-"
    
    def handle_submit():
        """Handles several types of error checking once the submit button is pressed
        """
        # Error checks
        error_text = ""
        if stock_name == "-":
            error_text = ":red[Please select a **Stock Name**.]"
        elif stock_info == "-":
            error_text = f":red[Please select a **Stock {choice_meaning[choice][1]} Price and Shares**.]"

        # Checks to see if there were any errors, and if not, then proceed
        if error_text != "":
            # Shows an error message
            show_output_message(output_component, error_text, 2)
        else:
            # Splits the selected stock info value into the Ask/Bid price, and shares value
            selected_stock_price = stock_info.split(" | ")[0].replace(f"{choice_meaning[choice][1]}: ", "")
            selected_stock_shares = stock_info.split(" | ")[1].replace("Shares: ", "")
            # Filters the choice and stock_name filtered dictionary to only have stocks that have the same price and shares as selected
            selected_stock_only_order_book = {order_id: order for order_id, order in stock_name_only_order_book.items() if order['Price'] == selected_stock_price and order['Quantity'] == selected_stock_shares}
            # Processes the order exchange by removing the order from the order_book using a function
            process_order_exchange(selected_stock_only_order_book)
            # Shows a success message
            show_output_message(output_component, f':green[Purchased **{selected_stock_shares}x {stock_name}** for **{selected_stock_price}**]', 3)
            # Clears the inputs after submitting
            clear_inputs()
    
    # If the stock info has been selected, show the Purchase/Sell button
    if stock_info != "-":
        # Splits the selected stock info value into the Ask/Bid price, and shares value
        selected_stock_price = stock_info.split(" | ")[0].replace(f"{choice_meaning[choice][1]}: ", "")
        selected_stock_shares = stock_info.split(" | ")[1].replace("Shares: ", "")
        # Creates the Purchase/Sell button
        purchase_sell_order_button = st.button(choice, on_click=handle_submit)
        # The text component to show an error or success message
        output_component = st.markdown("")

# Creates a divider from the selectable options and the Order Book
st.divider()

# Creates a Order Book box
order_book_container = st.container(border=True)
# Adds a "📖 Order Book" header to the box
order_book_container.markdown("<h3 style='text-align: center;'>📖 Order Book</h3>", unsafe_allow_html=True)

# If there are no orders in the order_book, just show "Order book is empty"
if len(st.session_state.order_book) == 0:
    order_book_container.text("Order book is empty")
# Shows stocks if there are stocks in the order_book
else:
    # Creates columns for a "Buy Orders" section, and a "Sell Orders" section
    buy_column, sell_column = order_book_container.columns(2, border=True)
    
    # Creates data in the Buy Column
    with buy_column:
        # Adds a Buy Column header
        st.markdown("<h4 style='text-align: center;'>Buy Orders</h4>", unsafe_allow_html=True)
        
        # Creates 4 columns for the Time, Name, Qty, and Price
        time_column, name_column, qty_column, price_column = st.columns(4)
        # Adds a header for each column
        time_column.markdown("<h5 style='text-align: center;'>Time</h5>", unsafe_allow_html=True)
        name_column.markdown("<h5 style='text-align: center;'>Name</h5>", unsafe_allow_html=True)
        qty_column.markdown("<h5 style='text-align: center;'>Shares</h5>", unsafe_allow_html=True)
        price_column.markdown("<h5 style='text-align: center;'>Bid</h5>", unsafe_allow_html=True)
        
        # Sorts the order_book by the item price, from Highest to Lowest
        sorted_order_book = dict(sorted(st.session_state.order_book.items(), key=lambda item: float(item[1]['Price']), reverse=True))
        # Goes through each order in the sorted order_book
        for order_id in sorted_order_book:
            # Gets the specific order information
            order = sorted_order_book[order_id]
            # Only goes through orders with an "Order Type" of "Buy"
            if order["Order Type"] == "Buy":
                # Creates a container for the order
                order_container = st.container(border=True, key=order_id)
                # Creates 4 columns within the container for each piece of data
                order_time_column, order_name_column, order_qty_column, order_price_column = order_container.columns(4)
                # Adds the data as text to each column
                order_time_column.text(order["Time"])
                order_name_column.text(order["Name"])
                order_qty_column.markdown(f'<p align="right">{order["Quantity"]}</p>', unsafe_allow_html=True)
                order_price_column.markdown(f'<p align="right">{order["Price"]}</p>', unsafe_allow_html=True)
    
    # Creates data in the Sell Column
    with sell_column:
        # Adds a Sell Column header
        st.markdown("<h4 style='text-align: center;'>Sell Orders</h4>", unsafe_allow_html=True)
        
        # Creates 4 columns for the Price, Qty, Name, and Time
        price_column, qty_column, name_column, time_column = st.columns(4)
        # Adds a header for each column
        price_column.markdown("<h5 style='text-align: center;'>Ask</h5>", unsafe_allow_html=True)
        qty_column.markdown("<h5 style='text-align: center;'>Shares</h5>", unsafe_allow_html=True)
        name_column.markdown("<h5 style='text-align: center;'>Name</h5>", unsafe_allow_html=True)
        time_column.markdown("<h5 style='text-align: center;'>Time</h5>", unsafe_allow_html=True)
        
        # Sorts the order_book by the item price, from Lowest to Highest
        sorted_order_book = dict(sorted(st.session_state.order_book.items(), key=lambda item: float(item[1]['Price'])))
        # Goes through each order in the sorted order_book
        for order_id in sorted_order_book:
            # Gets the specific order information
            order = sorted_order_book[order_id]
            # Only goes through orders with an "Order Type" of "Sell"
            if order["Order Type"] == "Sell":
                # Creates a container for the order
                order_container = st.container(border=True, key=order_id)
                # Creates 4 columns within the container for each piece of data
                order_price_column, order_qty_column, order_name_column, order_time_column = order_container.columns(4)
                # Adds the data as text to each column
                order_price_column.text(order["Price"])
                order_qty_column.text(order["Quantity"])
                order_name_column.text(order["Name"])
                order_time_column.text(order["Time"])