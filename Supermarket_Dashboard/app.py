import dash
import pandas as pd
import numpy as np
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from dash import no_update



def bar_fig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(XYZ_Company_Datasets, x='Product line', y='Total', color='City', title='TITLE'
                       
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def treeMAp_fig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure = px.treemap(XYZ_Company_Datasets, 
                    path=['City', 'Product line'], 
                    values='Total',
                    color='Total',
                    color_continuous_scale='RdBu',
                    title='TITLE'
                       
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

def pie_fig():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.pie(XYZ_Company_Datasets, values='gross income', names='City', title='THE SUPERMARKET GROSS INCOME'
                       
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])


    

# Text field
def drawText(name,value):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                                        html.Div(children=[html.Div(
                                        html.Div(html.H1(name, 
                                                                style={"text-align": "center", "font-size":"20px","font-family": "Abel","font-weight":"600","font-size": "16px"}),)),                       
                                        html.Div(
                                        html.Div(html.H1(value, 
                                                                style={"text-align": "center", "font-size":"20px","font-family": "Abel","font-weight":"600","font-size": "16px"}),)),
                                                                ],), 
            ])
        ),
    ])



# Dash Application

app = dash.Dash(__name__)


url = "XYZ_Company_Dataset.csv"
XYZ_Company_Datasets = pd.read_csv(url)

City_grp = XYZ_Company_Datasets.groupby('City')
City_Income = City_grp.agg({"gross income":["sum","mean","max"]})


       
    
abuja = City_Income.loc['Abuja',[('gross income',  'sum')]]
AbujaNam ="ABUJA INCOME (N)"
lagos = City_Income.loc['Abuja',[('gross income',  'sum')]]
LagosNam ="LAGOS INCOME (N)"
pH =  City_Income.loc['Port Harcourt',[('gross income',  'sum')]]
pHNam = "PORTHARCOUT INCOME (N)"


# Build App
app = Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText(AbujaNam,abuja)
                ], width=4),
                dbc.Col([
                    drawText(LagosNam,lagos)
                ], width=4),
                dbc.Col([
                    drawText(pHNam,pH)
                ], width=4),
            ], align='center'), 
            html.Br(),
            dbc.Row([
              #   dbc.Col([
              #       pie_fig() 
              #   ], width=3),
                dbc.Col([
                    pie_fig()
                ], width=6),
                dbc.Col([
                    bar_fig() 
                ], width=6),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    treeMAp_fig()
                ], width=9),
                dbc.Col([
                    pie_fig()
                ], width=3),
            ], align='center'),      
        ]), color = 'dark'
    )
])

# Run app and display result inline in the notebook
app.run_server(debug=True) 




