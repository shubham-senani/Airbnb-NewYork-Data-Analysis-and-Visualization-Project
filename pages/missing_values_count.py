import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp
grap = navbar.Graph

dash.register_page(__name__, path='/missing_values_count', title="Data Analysis and Visualization",
                   description="learning simplified", image='logo2.png')

layout = html.Div(children=[

    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn0")
    ], className="d-none py-5"),
    dbc.Col([
        dcc.Graph(id='line-graph0', figure={})
    ], className="d-flex justify-content-center", style={"padding-top": "90px"}),

    html.Div([

        html.H1("Missing Values Count", style={
                "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600"}),

        html.P("When analyzing data related to Airbnb listings, it is important to consider the presence of missing values, which are data points that are absent from the dataset. One way to visualize the extent of missing values is to create a graph that displays the count of missing values for each variable."

               "In this graph, each variable is listed on the x-axis, while the y-axis represents the count of missing values for each variable. The graph can be presented using a bar chart, where the height of each bar represents the count of missing values for the corresponding variable."

               "By examining this graph, one can gain insight into the completeness of the dataset, as well as identify variables that may require further investigation or cleaning due to a high number of missing values. This information can be useful for ensuring the accuracy and reliability of any analyses or models built using the data.", style={"margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})

], style={"background": "black"})

# Callback section: connecting the components


@dash.callback(
    Output('line-graph0', 'figure'),
    Input('radio-btn0', 'value')
)
def update_graph(stock_slctd):
    return dp.missing_values_count
