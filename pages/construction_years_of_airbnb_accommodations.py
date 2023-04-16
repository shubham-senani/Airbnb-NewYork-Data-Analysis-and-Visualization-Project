import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/construction_years_of_airbnb_accommodations',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
        "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn3")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph3', figure={})
    ], className="d-flex justify-content-center", style={"padding-top": "80px"}),

    html.Div([

        html.H1("Construction years of Airbnb accommodations", style={
                "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("According to the available data, the year 2014 witnessed the highest number of new accommodations built on the Airbnb platform, with a total of 5,220 listings. This indicates that there was a significant surge in construction activity in that year to meet the growing demand for Airbnb accommodation."

               "Apart from 2014, there were other years when a relatively high number of accommodations were built, such as 2006, 2008, and 2019. This suggests that these were also years of high growth and expansion for the Airbnb platform."

               "In contrast, the periods of 2010-2013 and 2015-2017 saw the least amount of construction activity, with their lowest years being 2013 and 2016, respectively. Specifically, in 2013 and 2016, only 4,995 and 4,990 new accommodations were built, respectively."

               "These trends in construction activity reflect the changing demand and supply dynamics of the Airbnb platform. During periods of high growth and expansion, such as in 2014 and other years with relatively high construction activity, there was a need to build more accommodations to meet the increasing demand from travelers. Conversely, during periods of slower growth, such as in 2010-2013 and 2015-2017, there was less demand for new listings, leading to a decrease in construction activity."

               "Overall, these findings highlight the importance of monitoring trends in construction activity on the Airbnb platform, as they can provide insights into the changing dynamics of the platform and the evolving needs of travelers.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})


], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph3', component_property='figure'),
    Input(component_id='radio-btn3', component_property='value')
)
def update_graph(stock_slctd):
    return dp.construction_years_of_airbnb_accommodations
