import yfinance
import matplotlib.pyplot

# Example: Apple stock data
# apple = yfinance.Ticker("AAPL")
# print(apple.info)


# Get S&P 500 intraday data for today
sp500 = yfinance.Ticker("^GSPC")
data = sp500.history(period="1d", interval="5m")

# print(data)

# Plot the Close prices
matplotlib.pyplot.figure(figsize=(10, 5))
matplotlib.pyplot.plot(data.index, data["Close"], label="S&P 500 Close Price")
matplotlib.pyplot.xlabel("Time")
matplotlib.pyplot.ylabel("Price")
matplotlib.pyplot.title("S&P 500")
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()
