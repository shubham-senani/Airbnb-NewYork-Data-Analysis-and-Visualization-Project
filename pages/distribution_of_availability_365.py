import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/distribution_of_availability_365',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
        "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn111")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph111', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top": "80px"}),

    html.Div([

        html.H1("The availability in 365 days", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("Based on the histogram plot created using the Seaborn library, it is evident that the 'avail_365' variable has the highest count at around 30,000, indicating the availability of accommodations for 365 days. The plot shows that this is the most common availability value among the listed accommodations on Airbnb."

               "The 'avail_365' variable represents the number of days in a year that an accommodation is available for booking on the platform. The high count at 30,000 suggests that many hosts are willing to make their properties available for booking throughout the year, which could be due to various reasons, such as the location of the accommodation, the type of property, or the host's personal preferences."

               "Understanding the availability of accommodations is crucial for both hosts and guests on Airbnb. Hosts can use this information to optimize their pricing strategies, adjust their availability settings, and plan for maintenance or renovation periods. Guests, on the other hand, can use this information to make informed decisions about their travel plans and ensure that they book accommodations that are available during their desired dates."

               "Overall, the histogram plot provides valuable insights into the distribution of the 'avail_365' variable among Airbnb listings and highlights the importance of considering availability when making decisions about hosting or booking accommodations on the platform.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})


], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph111', component_property='figure'),
    Input(component_id='radio-btn111', component_property='value')
)
def update_graph(stock_slctd):
    return dp.distribution_of_availability_365
