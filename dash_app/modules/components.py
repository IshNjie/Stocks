# Import packages
from dash import Dash, html, dash_table, dcc
from datetime import date
import dash_bootstrap_components as dbc

def search_input(id, value, style={'marginRight':'10px'}):
    com = dcc.Input(id=id, type="text", value=value, style=style)

    return com

def date_input(id):
    com = dcc.DatePickerRange(
        id=id,
        min_date_allowed=date(1990, 1, 1),
        max_date_allowed=date.today(),
        initial_visible_month=date.today(),
        start_date =date(2020,1,1),
        end_date = date.today()
    )

    return com


def card_body(id,title):
    com = dbc.Card(
        dbc.CardBody([
            html.H4('', id = id ),
            html.P(title)
            ]),
            style={'textAlign': 'center',"width": "18rem"})
    
    return com
    