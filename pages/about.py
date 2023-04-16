
# import dash_html_components as html
from dash import html
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navbar
import dash
from apps import profile_6
from apps import profile_5
from apps import profile_4
from apps import profile_3
from apps import profile_2
from apps import profile_1

dash.register_page(__name__, path='/about', title="Data Analysis and Visualization",
                   description="Deep learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={
             "z-index": "111", "position": "fixed", "width": "100%"}),
    html.P("Airbnb, a popular home-sharing platform, has grown significantly in recent years, connecting hosts and guests in New York City and around the world. As the platform has grown, Airbnb has faced various challenges related to taxes, safety, security, and compliance with local regulations. To address these challenges, Airbnb has implemented measures such as collecting and remitting local taxes, implementing safety measures like identity verification and guest reviews, and partnering with local organizations to promote responsible hosting.",
           style={"padding-top": "100px", "padding-inline": "50px", "font-size": "20px"}),

    html.P("This dataset contains information on over 100,000 Airbnb listings in New York City. The dataset includes 26 columns with data on various aspects of the listings, such as host information, property details, pricing, reviews, and availability. The dataset also includes information on Airbnb's efforts to comply with local regulations and address concerns about safety, security, and housing affordability.",
           style={"padding-top": "10px", "padding-inline": "50px", "font-size": "20px"}),

    html.P("The data provides valuable insights into the operation of Airbnb in New York City and the challenges faced by the platform. It can be used to analyze trends in pricing, occupancy rates, and customer reviews, as well as to assess Airbnb's compliance with local regulations and safety measures. The dataset can also be used to understand the impact of Airbnb on the local economy and housing affordability, and to identify areas where further improvements may be needed.",
           style={"padding-top": "10px", "padding-inline": "50px", "font-size": "20px"}),

    html.P("By analyzing this dataset, we can gain a better understanding of how Airbnb operates in New York City, its impact on the local economy, and the challenges it faces in complying with local regulations and ensuring safety and security for hosts and guests. This analysis can provide valuable insights for policymakers, regulators, and stakeholders interested in the home-sharing industry and its effects on communities.",
           style={"padding-top": "10px", "padding-inline": "50px", "font-size": "20px"}),
    html.H1("Contributors", style={
            "margin-block": "50px", "color": "#954040", "text-align": "center"}),

    html.Div([
        html.Div([
            profile_1.card,
        ]),
        html.Div([
            profile_2.card,
        ], style={"margin-top": "150px"}),
    ], style={"display": "flex", "justify-content": "space-between", "padding-inline": "20px"}),

    html.Div([
        html.Div([
            profile_3.card,
        ]),
        html.Div([
            profile_4.card,
        ], style={"margin-top": "150px"}),
    ], style={"display": "flex", "justify-content": "space-between", "padding-inline": "20px", "margin-top": "60px"}),

    html.Div([
        html.Div([
            profile_5.card,
        ]),
        html.Div([
            profile_6.card,
        ], style={"margin-top": "150px"}),
    ], style={"display": "flex", "justify-content": "space-between", "padding-inline": "20px", "margin-top": "60px"})




], style={"background": "linear-gradient(180deg, rgba(238,157,154,1) 10%, rgba(250,250,250,1) 38%)"})
