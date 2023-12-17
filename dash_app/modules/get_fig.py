import yfinance as yf
import pandas as pd
import plotly.express as px
from modules.get_data import get_data

def get_trend_fig(data,ticker,rolling):
    data = get_data(ticker, rolling)
    fig = px.line(data, x = data.index, y =['Adj Close'])
    fig.update_layout(title = 'Daily Chart for {}'.format(ticker))
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Adj Close $")
    fig.update_layout(showlegend=False)

    return fig


def get_rolling_fig(data,ticker,rolling):
    data = get_data(ticker,rolling)
    fig = px.line(data, x = data.index, y =['Adj Close','Rolling'])
    fig.update_layout(title = 'Daily Chart for {} with {} Rolling Mean'.format(ticker,rolling))
    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Adj Close $")
    #fig.update_layout(showlegend=False)

    return fig
