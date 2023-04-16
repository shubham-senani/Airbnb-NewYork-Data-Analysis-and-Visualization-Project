import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/distribution_of_price_by_host_verification_status',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn8")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph8', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top": "80px"}),

    html.Div([

             html.H1("Distribution of price by host verification status", style={
                 "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

             html.P("In the context of a data analysis or visualization, the distribution of price by host verification status can be presented using sns boxplots. The sns boxplot is a type of chart that displays the distribution of a numerical variable across different categories."

                    "In this particular case, the host verification status is used as the categorical variable, while the price is the numerical variable. The sns boxplot is represented by two colored boxes: a red one and a blue one."

                    "The red sns boxplot represents the verified identity of the host, meaning that the host has provided documentation to prove their identity. The blue sns boxplot, on the other hand, represents the unconfirmed identity of the host, meaning that the host has not yet provided documentation to verify their identity."

                    "By comparing the distribution of price between the two verification status categories, one can gain insight into any potential differences in pricing between verified and unverified hosts. This information can be useful for both hosts and guests, as it can help hosts set appropriate prices for their listings and help guests make informed decisions about where to stay.", style={
                        "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
             html.H1("skipper", style={"visibility": "hidden"})
             ], style={})

], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph8', component_property='figure'),
    Input(component_id='radio-btn8', component_property='value')
)
def update_graph(stock_slctd):
    return dp.distribution_of_price_by_host_verification_status
