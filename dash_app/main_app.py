# Import packages
from dash import Dash, html, dash_table, dcc,  Input, Output, State, callback
import yfinance as yf
import pandas as pd
import plotly.express as px
from modules.get_data import get_data
from modules.get_fig import get_trend_fig, get_rolling_fig
import dash_bootstrap_components as dbc
import modules.css_styles
import numpy as np

import warnings
warnings.filterwarnings('ignore')

# Import specific style sheet
ex_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

# Initialize the app and add css to instance
app = Dash(__name__, external_stylesheets = ex_css)

def create_card(title, content, card_id):
    return html.Div(
        id = card_id,
        className='card',
        children=[
            html.Div(className='card-header', children=title),
            html.Div(className='card-body', children=content),
        ],style={"width": "15rem"}
    )

# App layout
app.layout = html.Div([

    # Header
    html.H1('Stock App',className="text-dark text-center fw-bold fs-1"),
    html.Br(),
    html.Label('Enter Ticker: ',style={'marginRight':'10px'}),
    # Add input with default value 
    dcc.Input(id="ticker", type="text", value="AAPL", style={'marginRight':'10px'}),
    dcc.Input(id="rolling", type="text", value="100", style={'marginRight':'10px'}),

    # Add a submit button for the Input. .Button is used to trigger the data retrieval
    # n_clicks represents the number of times the button has been clicked
    # initialized at 0
    html.Button(id='submit-button',n_clicks=0,children='Submit'),
    html.Br(),

    create_card('Latest Close','', 'output-card'),
    html.Br(),
   
    # Tabs

    dcc.Tabs([
          # First Tab
          dcc.Tab(label = 'Summary', children = [
                # Label for input - 
                html.Br(),
                
                dcc.Graph(id='stock-graph'),

                # Add a specific div for the table
                html.Div([
                      # Add a title, instead of inputting the title, aim is to make this dynamic so add an id to reference in callback

                      html.H3(id = 'data-title',className="text-dark text-center fw-bold fs-1"),
                      # dashTable coponent is used to display the data in a tabular format
                      dash_table.DataTable(id='data-table', page_size=10)
                ])

          ],style=modules.css_styles.tab_style, selected_style=modules.css_styles.tab_selected_style),
          
          dcc.Tab(label = 'Analysis', children = [
                # Label for input - 
                html.Br(),

                dcc.Graph(id='rolling-graph'),
                ],style=modules.css_styles.tab_style, selected_style=modules.css_styles.tab_selected_style)
                ]
                )
])
    
# Call back to output particular ID

#Callback to update Graph upon button click
# Identify which object is to be changed based on the ID
# the inputs and outputs of our application are the properties of a particular component. 



'''
Example:

@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
'''

#### See if you can build multiple callbacks for each tab to clean up output
'''
Top level filter callback

Tab1 callback

Tab 2 callback


'''
@app.callback(
    Output('stock-graph','figure'),
    Output('rolling-graph','figure'),
    Output('data-title','children'),
    Output('data-table','data'),
    Output('output-card','children'),

    # any changes to Input will prompt a change, ie, each typing instance. 
    # State preserves the need to refresh and only refreshes when button is clicked, at that point, the current state 'Input value' will be passed to the callback
    Input('submit-button', 'n_clicks'),
    State('ticker','value'),
    State('rolling','value')
)

# function to get data 

def render(n_clicks,ticker,rolling):
    # Set up data and figures
    data = get_data(ticker,int(rolling))
    trend_fig = get_trend_fig(data,ticker,int(rolling))
    rolling_fig = get_rolling_fig(data,ticker,int(rolling))
    data_title = 'Data for {}'.format(ticker)

    
    data['Return'] = data['Close'].pct_change() *100
        
    data = data.reset_index().sort_values(by='Date', ascending=False)
    latest_close = data['Adj Close'].iloc[0]
    change = data['Return'].iloc[0]

    df = data.to_dict('records')
    card_output = '{:.2f} ({:.2f}%)'.format(latest_close,change)
    # Here, the order of the output needs to match the order of the outputs in the callback
    return (
            trend_fig,
            rolling_fig,
            data_title,
            df,
            card_output

    )

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
