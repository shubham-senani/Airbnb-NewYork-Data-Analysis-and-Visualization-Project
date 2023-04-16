import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/distribution_of_service_fee',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn10")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph10', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top": "80px"}),

    html.Div([

        html.H1("Distribution of service fee", style={
                "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("The analysis of the service fee data also reveals an even distribution of fees across the price bins. The service fee is a charge levied by Airbnb to cover the costs of processing and managing bookings on the platform. Like the listing prices, the service fees are spread evenly across the various price levels, indicating that Airbnb charges a consistent fee percentage for all bookings."

               "Overall, the even distribution of listing prices and service fees across the price bins suggests that Airbnb offers a diverse range of pricing options for both hosts and guests on the platform. This flexibility in pricing allows hosts to maximize their earnings and guests to find accommodations that fit their budget and travel needs.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})


],style={"background-color":"black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph10', component_property='figure'),
    Input(component_id='radio-btn10', component_property='value')
)
def update_graph(stock_slctd):
    return dp.distribution_of_service_fee
