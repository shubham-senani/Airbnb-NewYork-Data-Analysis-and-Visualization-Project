import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__,path='/distribution_of_price_by_nyc_borough',title="Data Analysis and Visualization",description="learning simplified",image='logo2.png')

layout = html.Div(children=[
     html.Div([navbar.navbar], style={"z-index":"111","position":"fixed", "width":"100%"}),
         dbc.Col([
            dcc.RadioItems(options=["graph"], value="graph", id="radio-btn9")
         ],className="d-none"),
         dbc.Col([
            dcc.Graph(id='line-graph9', figure={})
         ],className="d-flex justify-content-center bg-black", style={"padding-top":"80px"}),

         html.Div([

        html.H1("Distribution of Price by NYC borough", style={
                "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top":"50px"}),

        html.P("Upon analyzing the pricing data for Airbnb listings in New York City, it appears that all of the boroughs exhibit a similar distribution of prices, with only slight variations in the median prices."

        "This suggests that, on average, the prices of Airbnb listings in New York City are relatively consistent across all boroughs. The prices do not vary significantly, despite the fact that each borough has its own unique character, attractions, and amenities. This could be due to various factors, such as the prevalence of standardized pricing models, competitive pricing strategies, or regulatory frameworks."

        "Additionally, the similar distribution of prices across all boroughs suggests that Airbnb hosts are taking a comparable approach to pricing their listings, regardless of their location. This could be a result of the platform's pricing tools and guidelines, which provide hosts with recommendations and insights into pricing strategies based on factors such as demand, competition, and location."

        "Overall, the data indicates that the prices of Airbnb listings in New York City are generally consistent across all boroughs, with only minor differences in the median prices. This could have implications for both hosts and guests on the platform, as it suggests that pricing strategies may need to be adjusted to account for local market conditions and competition.", style={
               "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})

], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph9', component_property='figure'),
    Input(component_id='radio-btn9', component_property='value')
)
def update_graph(stock_slctd):
    return dp.distribution_of_price_by_nyc_borough