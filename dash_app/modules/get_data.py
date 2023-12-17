import yfinance as yf
import pandas as pd


# function to get data 
def get_data(ticker, rolling,start_date = "2020-12-01"):
    data = yf.download(ticker, start = start_date)
    data['Rolling'] = data['Adj Close'].rolling(rolling).mean()


    return data

