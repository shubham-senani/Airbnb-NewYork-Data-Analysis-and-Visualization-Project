import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/relation_between_minimum_of_nights_and_number_of_reviews',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn13")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph13', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top": "80px"}),

    html.Div([

        html.H1("Relation between Minimum of nights and number of Reviews", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("Based on the scatterplot analysis, it appears that there is no clear relationship between the number of reviews and the number of nights customers stay in accommodations on Airbnb. While a high number of reviews may indicate that an accommodation has been popular with guests, it does not necessarily mean that these guests have stayed for a longer period."

               "There could be several reasons for this lack of correlation between reviews and the length of stay. For example, some guests may leave a review immediately after a short stay, while others may wait until the end of their trip, even if it lasts for several weeks. Additionally, some guests may choose to extend their stay without leaving an additional review, while others may leave multiple reviews for the same accommodation if they have stayed there multiple times."

               "Overall, the lack of a clear relationship between reviews and the length of stay suggests that hosts should not rely solely on the number of reviews as an indicator of how long their guests are likely to stay. Instead, they should consider other factors such as pricing, location, and amenities to attract guests and encourage them to stay for longer periods.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})

], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph13', component_property='figure'),
    Input(component_id='radio-btn13', component_property='value')
)
def update_graph(stock_slctd):
    return dp.relation_between_minimum_of_nights_and_number_of_reviews
