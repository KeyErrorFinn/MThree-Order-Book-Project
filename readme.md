# Order Book Project

Description -
This project implements a simple Orderbook application using Python and Streamlit. It allows users to add buy and sell orders for stocks, providing a real-time view of the active bids and asks that you input. It is designed to be intuitive and easy to use, demonstrating the fundamental concept of an orderbook in a financial context.

Features -
Add Buy/Sell Orders: Easily input new stock orders, specifying the stock name, quantity, and total price.
Dynamic Order Display: You can view the separate columns for "Buy Orders" and "Sell Orders", which are updated as new orders are added.
Input Validation: Checks ensure that price and quantity inputs are valid numbers and greater than zero.
Unique Order IDs: Each order is assigned a unique, generated ID.

How It Works -
User Interface: Streamlit produces the interactive web interface such as display of the orderbook, input fields, buttons and buttons.
Order Addition: When a new order is submitted, it generates a unique ID, validates the inputs, and then adds the order details (Name, Order Type, Price, Quantity, Time) to the orderbook.
Real-time Update: The orderbook display automatically refreshes to show the latest buy and sell orders.
