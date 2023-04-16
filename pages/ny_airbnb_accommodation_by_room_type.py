import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__,path='/ny_airbnb_accommodation_by_room_type',title="Data Analysis and Visualization",description="learning simplified",image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
         dbc.Col([
            dcc.RadioItems(options=["graph"], value="graph", id="radio-btn11")
         ],className="d-none"),
         dbc.Col([
            dcc.Graph(id='line-graph11', figure={})
         ],className="d-flex justify-content-center", style={"padding-top":"80px"}),

         html.Div([

        html.H1("Percentage of NYC Airbnb accommodation by room type:", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("Based on the count plot, which is a graphical representation of the number of accommodations in different boroughs of New York, it can be observed that Manhattan has the highest number of accommodations, totaling 43,558 rooms. This indicates that Manhattan has the highest availability of accommodations among all the boroughs in New York."

       "Following Manhattan, the borough of Brooklyn has the second highest number of accommodations, with a total of 41,631 rooms. This suggests that Brooklyn is the second most popular borough for accommodations in New York, after Manhattan."

       "In contrast, Staten Island has the lowest number of accommodations among all the boroughs, with only 949 rooms in total. This implies that Staten Island has the least availability of accommodations compared to the other boroughs in New York."

       "It's important to note that the count plot provides a visual representation of the data and allows for a quick overview of the accommodation distribution in different boroughs of New York. However, it does not provide detailed information about the type, quality, or pricing of the accommodations, which may vary within each borough. Further analysis and additional data may be required to fully understand the factors influencing the accommodation distribution in New York City", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})

], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph11', component_property='figure'),
    Input(component_id='radio-btn11', component_property='value')
)
def update_graph(stock_slctd):
    return dp.ny_airbnb_accommodation_by_room_type