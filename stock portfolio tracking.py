import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        #Add stocks to the portfolio
        symbol = symbol.upper()  # Convert symbol to uppercase
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        #Remove stocks from the portfolio
        symbol = symbol.upper()  # Convert symbol to uppercase
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]  # Remove the stock if quantity becomes 0
            else:
                print("Error: Insufficient quantity to remove.")
        else:
            print("Error: Stock not found in portfolio.")

    def get_stock_price(self, symbol):
        #Get the current price of a stock using Alpha Vantage API
        api_key = input("Enter your API_KEY: ")
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        try:
            response = requests.get(url)
            data = response.json()
            price = float(data['Global Quote']['05. price'])
            return price
        except Exception as e:
            print(f"Error retrieving data for {symbol}: {e}")
            return None

    def display_portfolio(self):
        #current portfolio with current prices
        print("\nCurrent Portfolio:")
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                print(f"{symbol}: {quantity} shares - Current Price: ${price:.2f}")

# Example usage
portfolio = StockPortfolio()
portfolio.add_stock("AAPL", 20)
portfolio.add_stock('GOOGL', 8)
portfolio.add_stock('MSFT', 5)
portfolio.display_portfolio()
portfolio.remove_stock('AAPL', 5)
portfolio.display_portfolio()
