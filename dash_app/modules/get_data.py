import yfinance as yf
import pandas as pd

pd.options.display.float_format = "{:,.2f}".format

# function to get data 
def get_data(ticker,start_date, end_date):
    data = yf.download(ticker, start = start_date, end = end_date)
    data['Return'] = data['Close'].pct_change() *100


    return data



def get_data_compare(ticker,start_date, end_date):
    data = yf.download(ticker, start = start_date, end = end_date)
    if isinstance(data.columns,pd.MultiIndex):
        data.columns = [f'{ticker}_{col}' for col, ticker in data.columns]
    else:
        data.columns = [f'{ticker}_{col}' for col in data.columns]

    return data

