<h1 align="center">
  Orderbook Project<br>by Anjali & Finnley
</h1>

<p align="center">
  <a href="https://github.com/KeyErrorFinn/rpuk-park-ranger-bills/commits/main/"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KeyErrorFinn/rpuk-park-ranger-bills" /></a>
</p>
<p align="center">
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" /></a>
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Streamlit-%23FE4B4B?logo=streamlit&logoColor=white" /></a>
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About the Project](#about-the-project)
- [How it Works](#how-it-works)
- [How to Run](#how-to-run)
- [Possible Additions](#possible-additions)

## About the Project

This project implements a simple Orderbook web application using Python and Streamlit.

It allows users to add buy and sell orders for stocks, providing a real-time view of the active bids and asks that you input. You can also purchase sell orders, or sell to a buy order.

It is designed to be intuitive and easy to use, demonstrating the fundamental concept of an orderbook in a financial context.

## Features

- **Add Buy/Sell Orders:** Easily input new stock orders, specifying the stock name, quantity, and total price.
- **Purchase Sell Orders:** Purchase any available sell order by selecting the name of the stock, and its information.
- **Sell to Buy Orders:** Sell to any available buy order by selecting the name of the stock, and its information.
- **Dynamic Order Display:** You can view the separate columns for "Buy Orders" and "Sell Orders", which are updated as new orders are added.
- **Input Validation:** Checks on all input fields to make sure there is not invalid data inputted, and that the output is correct.
- **Unique Order IDs:** Each order is assigned a unique, generated ID.
- **Stock Colouring:** Each stock price is assigned a unique colour and groups together similar stock prices in the same column.

## How it Works

- **User Interface:** Streamlit produces the interactive web interface such as display of the orderbook, selection dropdowns, input fields, and buttons.
- **Order Addition:** When a new order is submitted, it validates the inputs, generates a unique ID, and then adds the order details *(Name, Order Type, Price, Quantity, Time, and Colour)* to the orderbook.
- **Buying/Selling Stocks:** The selection dropdowns automatically populate with all unique stock names, then once a user selects the stock name, a new dropdown appears with all stock info for that stock, and once a user has selected the correct information and submitted it, it validates the inputted information, then it removes a the selected stock from the order book. If there is a stock with the exact same information, it will remove the oldest stock.
- **Real-time Update:** The orderbook display automatically refreshes to show the latest buy and sell orders.

## How to Run

1. Make sure to have all the files in a folder.
2. Open up a terminal and set your path to the folder.
3. Install the required packages by entering the following in your terminal:

   ```
   pip install -r requirements.txt
   ```
4. Run the script using streamlit by enterting the following in your terminal:

   ```
   streamlit run main.py
   ```
5. A web page should open and you can access the application there.

## Possible Additions

- [ ] Add a database (Either JSON or SQL).
- [ ] Make into a Flask website.
