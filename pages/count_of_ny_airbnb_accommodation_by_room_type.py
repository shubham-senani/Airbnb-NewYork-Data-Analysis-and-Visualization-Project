import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__,path='/count_of_ny_airbnb_accommodation_by_room_type',title="Data Analysis and Visualization",description="learning simplified",image='logo2.png')

layout = html.Div(children=[
    navbar.navbar,
         dbc.Col([
            dcc.RadioItems(options=["graph"], value="graph", id="radio-btn4")
         ],className="d-none"),
         dbc.Col([
            dcc.Graph(id='line-graph4', figure={})
         ],className="d-flex justify-content-center")
])


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph4', component_property='figure'),
    Input(component_id='radio-btn4', component_property='value')
)
def update_graph(stock_slctd):
    return dp.count_of_ny_airbnb_accommodation_by_room_type