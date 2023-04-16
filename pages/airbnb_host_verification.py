import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/airbnb_host_verification',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn1")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph1', figure={})
    ], className="d-flex justify-content-center", style={"padding-top": "80px"}),

    html.Div([

        html.H1("Airbnb host verification", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("According to recent statistics, the total number of Airbnb host accounts is comprised of 51,200 unconfirmed accounts, representing 50.04% of the total host population. Additionally, there are 51,110 verified hosts, which is only slightly lower than the number of unconfirmed accounts."

               "It is concerning to note that half of the Airbnb hosts have not yet verified their status, which is a relatively high percentage. The lack of verification raises questions about the reliability and safety of these listings, as there is no guarantee that the hosts are who they claim to be."

               "To ensure a secure and trustworthy platform for all users, it is crucial that Airbnb takes proactive measures to encourage hosts to verify their accounts. This could involve incentivizing verification through rewards or penalties for unverified accounts, and promoting the importance of verification through targeted education campaigns. By taking these steps, Airbnb can help to mitigate potential risks and build greater trust in the platform among both hosts and guests.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})

], style={"background-color": "black"})


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph1', component_property='figure'),
    Input(component_id='radio-btn1', component_property='value')
)
def update_graph(stock_slctd):
    return dp.airbnb_host_verification
