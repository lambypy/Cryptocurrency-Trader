import pandas as pd
import numpy as np

from market_data import retrieve_stock_data


def turtle_trading_strategy(stock, start_date=None, end_date=None):
    """A trend-following strategy to take advantage of sustained momentum in a market.

    Args:
        stock: The stock or stocks that you want to trade using this strategy.
        start_date: Optional start date for backtesting, default is current date.
        end_date: Optional end date for backtesting, default is strategy-based. 

    Returns:
    """

    # Data retrieved in a dataframe for each of the required stocks
    stock_data = retrieve_stock_data()




def breakout_strategy():
    """Following periods of high volatility and momentum, trading on those breakouts.
    
    Args:
        stock:
        start:
        end:

    Returns:
    """

    stock_data = retrieve_stock_data()

    # calculate the resistance and support levels
    #stock_data[]
    pass





def flag_pattern_strategy():
    """

    """

    stock_data = retrieve_stock_data()
    stock_data.columns = ["time", "open", "high", "low", "close", "volume"]

    # Removes values without volume/price movements such as weekends/days off
    stock_data = stock_data[stock_data["volume"] != 0]
    stock_data.reset_index(drop=True, implace=True)
    stock_data.isna().sum()
    print(stock_data.head(10))



