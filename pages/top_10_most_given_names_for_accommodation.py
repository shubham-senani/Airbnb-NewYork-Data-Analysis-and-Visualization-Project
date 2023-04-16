import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__,path='/top_10_most_given_names_for_accommodation',title="Data Analysis and Visualization",description="learning simplified",image='logo2.png')

layout = html.Div(children=[
        html.Div([navbar.navbar], style={
        "z-index": "111", "position": "fixed", "width": "100%"}),
         dbc.Col([
            dcc.RadioItems(options=["graph"], value="graph", id="radio-btn16")
         ],className="d-none"),
         dbc.Col([
            dcc.Graph(id='line-graph16', figure={})
         ],className="d-flex justify-content-center", style={"padding-top":"80px"}),

         html.Div([

        html.H1("Top 10 most given names for accommodation", style={
                "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("The information provided above regarding the most common names on Airbnb listings is quite intriguing. Notably, the name 'Home away from home' ranks as the most common with 33 occurrences, indicating a desire among travelers for a comfortable and familiar environment during their stay. The second most common names, 'Hillside Hotel' and 'Water View King Bed Hotel Room', emphasize luxurious accommodations and scenic locations, which can be major selling points for potential guests. Interestingly, the tenth position belongs to 'Cozy home away from home' with 18 occurrences, highlighting the appeal of a cozy and inviting environment for travelers seeking a more intimate and personalized experience. Collectively, these names offer valuable insights into the marketing strategies employed by Airbnb hosts to differentiate their listings and attract potential guests.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})
    
], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph16', component_property='figure'),
    Input(component_id='radio-btn16', component_property='value')
)
def update_graph(stock_slctd):
    return dp.top_10_most_given_names_for_accommodation