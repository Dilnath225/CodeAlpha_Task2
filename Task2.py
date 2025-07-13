"""
Stock Portfolio Manager
This script allows users to manage their stock portfolio by buying stocks,
tracking investments, and saving the portfolio summary to a file.

Author: Rathnayaka Pathiranage Sunera Dilnath
Student ID: CA/JU1/26435
Date: 2025- 07-11
Location: Sri Lanka

"""

#stock prices

stock_prices = {
    "AAPL": 180,
    "GOOGL": 250,
    "AMZN": 340,
    "MSFT": 280,
    "TSLA": 550
}

portifolio = {} # to store  the user portfolio

total_investment = 0  

print("Welcome to the Stock Portfolio Manager!")
print("Available stocks:")