'''
summary - where you csn bring in multiple tickers and show the data for the tickers
analysis page, rolling mean
news page

'''

# Import packages
from dash import Dash, html, dash_table, dcc,  Input, Output, State, callback
import yfinance as yf
import pandas as pd
import plotly.express as px
from modules.get_data import get_data, get_data_compare
from modules.get_fig import get_trend_fig, get_rolling_fig, get_compare_fig
from modules.components import search_input, date_input, card_body
import dash_bootstrap_components as dbc
import modules.css_styles
import numpy as np
from dash.exceptions import PreventUpdate

import warnings
warnings.filterwarnings('ignore')



# Import specific style sheet
ex_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

# Initialize the app and add css to instance
app = Dash(__name__, external_stylesheets = ex_css)

# App layout
app.layout = html.Div([

    # Header
    html.H1('Stock App',className="text-dark text-center fw-bold fs-1"),
    html.Br(),

    #TABS

    dcc.Tabs([
        #First Tab
        dcc.Tab(
            label = 'Summary',
            children = [
                # filters
                html.Label('Enter Ticker: ',style={'marginRight':'10px'}),
                # Add input with default value 
                search_input(id="ticker-sum", value="AAPL"),

                #html.Label('Enter Moving Average Value: ',style={'marginRight':'10px'}),
                #search_input(id="rolling", value="100"),

                html.Label('Date Period: ',style={'marginRight':'10px'}),
                date_input('date_period-sum'),

                # Add a submit button for the Input. .Button is used to trigger the data retrieval
                # n_clicks represents the number of times the button has been clicked
                # initialized at 0
                html.Button(id='submit-button-sum',n_clicks=0,children='Submit'),

                dcc.Graph(id='stock-graph'),
                html.Div([
                # Add a title, instead of inputting the title, aim is to make this dynamic so add an id to reference in callback

                    html.H3(id = 'data-title',className="text-dark text-center fw-bold fs-1"),
                      # dashTable coponent is used to display the data in a tabular format
                    dash_table.DataTable(id='data-table', page_size=10)
                ])
            ]
        ),

        dcc.Tab(
            label = 'Analysis',
            children = [
                # filters
                html.Label('Enter Ticker: ',style={'marginRight':'10px'}),
                # Add input with default value 
                search_input(id="ticker-ana", value="AAPL"),

                html.Label('Enter Moving Average Value: ',style={'marginRight':'10px'}),
                search_input(id="rolling-ana", value="100"),

                html.Label('Date Period: ',style={'marginRight':'10px'}),
                date_input('date_period-ana'),
                
                # Add a submit button for the Input. .Button is used to trigger the data retrieval
                # n_clicks represents the number of times the button has been clicked
                # initialized at 0
                html.Button(id='submit-button-ana',n_clicks=0,children='Submit'),

            
                ## Cards
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        card_body('close-card-ana','Latest Close')
                    ])
                ]),
                dcc.Graph(id='rolling-graph'),
                html.Div([
                # Add a title, instead of inputting the title, aim is to make this dynamic so add an id to reference in callback

                    #html.H3(id = 'data-title-su,',className="text-dark text-center fw-bold fs-1"),
                      # dashTable coponent is used to display the data in a tabular format
                    dash_table.DataTable(id='data-table-ana', page_size=10)
                ])
            ]
        )
    ])
])

#Summary Page

@app.callback(
    Output('stock-graph','figure'),
    Output('data-title','children'),
    Output('data-table','data'),

    Input('submit-button-sum','n_clicks'),
    State('ticker-sum','value'),
    State('date_period-sum','start_date'),
    State('date_period-sum', 'end_date'),
    prevent_initial_call = False
)
def render_summary(n_clicks,ticker_sum,start_date,end_date):
    # if n_clicks == 0:
    #     raise PreventUpdate 
    
    data_sum = get_data_compare(ticker_sum,start_date,end_date)

    figure = get_compare_fig(data_sum,ticker_sum)
    data_title = 'Data for {}'.format(ticker_sum)

    #data['Return'] = data[ticker+'Close'].pct_change() *100
    data_sum = data_sum.round(2).reset_index().sort_values(by='Date', ascending=False)
    df = data_sum.to_dict('records')
    
    return figure,data_title, df


#Analysis Page
@app.callback(
    Output('rolling-graph','figure'),
    Output('close-card-ana','children'),
    Output('data-table-ana','data'),

    Input('submit-button-ana', 'n_clicks'),
    State('ticker-ana','value'),
    State('rolling-ana','value'),
    State('date_period-ana','start_date'),
    State('date_period-ana','end_date'),
    prevent_initial_call = True
)

def render_analysis(n_clicks,ticker,rolling,start_date,end_date):
   
    data_ana = get_data(ticker,start_date,end_date)

    figure_ana = get_rolling_fig(data_ana,ticker,int(rolling))

    data_ana = data_ana.round(2).reset_index().sort_values(by='Date', ascending=False)

    latest_close = data_ana['Close'].iloc[0]
    change = data_ana['Return'].iloc[0]

    df_ana = data_ana.to_dict('records')
    card_output = '{:.2f} ({:.2f}%)'.format(latest_close,change)
    
    return figure_ana, card_output,df_ana

# Run the app
if __name__ == '__main__':
    app.run(debug=True)