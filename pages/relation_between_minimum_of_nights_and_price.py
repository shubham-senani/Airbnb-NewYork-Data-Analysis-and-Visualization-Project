import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/relation_between_minimum_of_nights_and_price',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={"z-index":"111","position":"fixed", "width":"100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn14")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph14', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top":"80px"}),

    html.Div([

        html.H1("Relation between Minimum of nights and price", style={
                "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top":"50px"}),

        html.P("The scatterplot displayed above provides a visual representation of the relationship between the two variables, minimum nights and price, in the context of Airbnb accommodations. The plot indicates how the values of these two variables are distributed and correlated with one another."

        "Through this visualization, we can observe how the values of minimum nights and price are distributed across the dataset, and how they are related to each other. The plot provides a comprehensive overview of the range and distribution of values for each variable and allows us to see any patterns or trends that may exist in the data."

        "In particular, the scatterplot reveals the nature of the relationship between minimum nights and price, indicating whether the two variables are positively, negatively, or not correlated at all. This information can be valuable for hosts and guests on the platform, allowing them to make informed decisions about pricing and booking strategies based on the observed trends in the data.", style={
               "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})
    
], style={"background-color":"black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph14', component_property='figure'),
    Input(component_id='radio-btn14', component_property='value')
)
def update_graph(stock_slctd):
    return dp.relation_between_minimum_of_nights_and_price
