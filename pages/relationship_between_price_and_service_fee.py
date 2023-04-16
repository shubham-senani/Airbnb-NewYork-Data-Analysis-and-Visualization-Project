import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/relationship_between_price_and_service_fee',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
        html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn15")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph15', figure={})
    ], className="d-flex justify-content-center bg-black", style={"padding-top":"80px"}),


    html.Div([

        html.H1("Relationship between Price and Service Fee", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("The plot in question indicates that there is a positive correlation between the rental price of Airbnb accommodations and the associated service fee. This suggests that, on average, higher-priced listings on the platform tend to have higher service fees as well."

               "This correlation could be a result of various factors. For instance, hosts of higher-priced listings may be more likely to use premium services or add-ons provided by Airbnb, which could increase the service fee. Additionally, the platform may charge a higher fee percentage for more expensive listings in order to generate greater revenue."

               "The positive correlation between rental price and service fee has implications for both hosts and guests on the platform. Hosts should be aware that higher-priced listings may result in higher service fees, and may need to factor this into their pricing strategies. Meanwhile, guests should consider the total cost of a listing, including the service fee, when making booking decisions."

               "Overall, the plot provides evidence of a positive correlation between rental price and service fee for Airbnb listings. This correlation is an important consideration for hosts and guests on the platform, as it can affect pricing strategies, revenue, and overall booking decisions.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})
], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph15', component_property='figure'),
    Input(component_id='radio-btn15', component_property='value')
)
def update_graph(stock_slctd):
    return dp.relationship_between_price_and_service_fee
