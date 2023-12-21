import yfinance as yf
import pandas as pd
import plotly.express as px
from modules.get_data import get_data, get_data_compare


def get_trend_fig(data,ticker):
    #data = get_data(ticker,start_date, end_date)
    print(data.columns)
    fig = px.line(data, x = data.index, y =['Close'])
    fig.update_layout(title = 'Daily Chart for {}'.format(ticker))
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Close $")
    fig.update_layout(showlegend=False)
    
    

    return fig


def get_rolling_fig(data,ticker,rolling):
    #data = data.reset_index()
    data['Rolling'] = data['Close'].rolling(rolling).mean()
    fig = px.line(data, x = data.index, y =['Close','Rolling'])
    fig.update_layout(title = 'Daily Chart for {} with {} Rolling Mean'.format(ticker,rolling))
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Close $")
    #fig.update_layout(showlegend=False)

    return fig  

def get_compare_fig(data,ticker):
    #data = get_data_compare(ticker,start_date, end_date)
    yaxis = [x for x in data.columns if "_Close" in x]
    
    fig2 = px.line(data,x = data.index, y=yaxis)
    fig2.update_layout(title = f'Daily Chart for {ticker}')
    fig2.update_xaxes(title="Year")
    fig2.update_yaxes(title="Close $")

    return fig2