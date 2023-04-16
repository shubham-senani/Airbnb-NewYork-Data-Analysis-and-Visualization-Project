import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/distribution_of_accommodation_price',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn6")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph6', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top": "80px"}),

    html.Div([

        html.H1("Distributions of Accommodation price", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("Based on the analysis of the Airbnb pricing data, it appears that the prices of listings on the platform are distributed evenly across the price bins. This means that there are roughly equal numbers of listings at each price point, with no significant concentration of listings at particular price levels."

               "This even distribution of prices suggests that hosts on Airbnb are using a variety of pricing strategies to attract guests, rather than relying on a fixed pricing model. Hosts may adjust their prices based on factors such as demand, seasonality, or local events, which could explain the lack of a clear pricing pattern across the platform.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})

], style={"background-color":"black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph6', component_property='figure'),
    Input(component_id='radio-btn6', component_property='value')
)
def update_graph(stock_slctd):
    return dp.distribution_of_accommodation_price
