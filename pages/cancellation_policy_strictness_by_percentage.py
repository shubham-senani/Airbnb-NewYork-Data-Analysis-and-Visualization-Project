import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps import navbar
import da_project as dp

dash.register_page(__name__, path='/cancellation_policy_strictness_by_percentage',
                   title="Data Analysis and Visualization", description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    dbc.Col([
        dcc.RadioItems(options=["graph"], value="graph", id="radio-btn2")
    ], className="d-none"),
    dbc.Col([
        dcc.Graph(id='line-graph2', figure={})
    ], className="d-flex justify-content-center", style={"padding-top": "80px"}),

    html.Div([

        html.H1("Cancellation policy strictness by percentage", style={
            "margin-inline": "50px", "margin-bottom": "25px", "text-align": "center", "color": "white", "font-weight": "600", "margin-top": "50px"}),

        html.P("Based on the analysis of Airbnb's accommodation cancellation policies, it is evident that the strictness of these policies is evenly distributed among three categories. Each category represents slightly above 33% of the total accommodation listings."

               "The 'moderate policy' category has the highest proportion of listings, accounting for 33.5% of all accommodations on the platform. This suggests that a significant proportion of hosts have opted for a policy that offers some level of flexibility for guests while still providing them with some protection against last-minute cancellations."

               "The other two categories, 'flexible' and 'strict,' each account for just over 33% of the remaining listings. This indicates that hosts on Airbnb have a relatively equal preference for different levels of strictness in their cancellation policies."

               "The distribution of these policies is likely to reflect the diverse needs and preferences of both hosts and guests on the platform. For example, hosts may choose a more flexible policy to attract guests who value convenience and are less likely to cancel their bookings, while others may prefer a stricter policy to minimize the risk of cancellations and maximize their earnings."

               "Overall, the even distribution of Airbnb's accommodation cancellation policies across the three categories highlights the importance of offering guests a range of options to choose from, based on their individual needs and preferences. It also emphasizes the need for hosts to carefully consider the trade-offs between flexibility and protection when setting their cancellation policies.", style={
                   "margin-inline": "50px", "margin-bottom": "0", "color": "white", "font-size": "20px", "line-height": "35px"}),
        html.H1("skipper", style={"visibility": "hidden"})
    ], style={})


], className="bg-black")


# Callback section: connecting the components
@dash.callback(
    Output(component_id='line-graph2', component_property='figure'),
    Input(component_id='radio-btn2', component_property='value')
)
def update_graph(stock_slctd):
    return dp.cancellation_policy_strictness_by_percentage
