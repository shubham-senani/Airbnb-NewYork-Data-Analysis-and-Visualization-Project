from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navbar
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', title="Data Analysis and Visualization",
                   description="learning simplified", image='logo2.png')

layout = html.Div(children=[
    html.Div([navbar.navbar], style={"position":"fixed", "width":"100%"}),
    dbc.Row([
        #
        dbc.Col([
            html.Img(src=dash.get_asset_url(
                'airbnb.svg'), height="200px",style={"margin-top":"160px", "margin-right":"36px"}),
            html.Div([
                html.Div([
                    html.H1("C S", style={"font-family": "serif"}),
                    html.H1(" 3 1 2", style={
                            "margin-left": "8px", "color": "red", "font-family": "serif"})
                ], style={"display": "flex"}),
                html.H5("Data Visualization and Analysis",
                        style={"font-size": "10px"})
            ], style={"display": "flex", "flex-direction": "column", "align-items": "center", "margin-right":"40px"})
        ], className="d-flex flex-column align-items-center justify-content-between ", style={"padding-block": "100px", "width": "20%", "height": "100vh", "background": "linear-gradient(180deg, rgba(238,157,154,1) 10%, rgba(250,250,250,1) 68%)"}),
        #
        dbc.Col([
            html.H1("airbnb", style={"color": "#e44848", "font-size": "65px",
                    "font-weight": "700", "text-align": "end", "margin-right": "80px"}),
            html.H1("Analyzing US dataset of airbnb", style={
                    "color": "#954040", "text-align": "end", "margin-right": "80px"}),
            html.P("After moving to San Francisco in October 2007, roommates and former schoolmates Brian Chesky and Joe Gebbia came up with the idea of putting an air mattress in their living room and turning it into a bed and breakfast.In Februray 2008, Nathan Blecharczyk", style={
                   "text-align": "end", "margin-left": "30%", "margin-right": "80px", "color": "#d46565"})
        ], className="col-9 d-flex flex-column justify-content-center", style={"margin-bottom": "160px"})

    ], className="d-flex align-items-center justify-content-between", style={"height": "100vh"}),
], style={"padding":"0px", "margin":"0px","width": "100vw","background": "linear-gradient(180deg, rgba(238,157,154,1) 10%, rgba(250,250,250,1) 38%)"})
