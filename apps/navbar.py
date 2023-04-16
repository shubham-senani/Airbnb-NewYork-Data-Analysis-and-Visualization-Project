import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
import dash

Graph = ["Missing Values Count", "Top 10 most given names for accommodation", "Airbnb host verification", "Count of NYC Airbnb accommodation by neighborhood group", "Percentage of NYC Airbnb accommodation by neighborhood group", "NY Airbnb Accommodation by Room Type", "Construction years of Airbnb accommodations",
         "Cancellation policy strictness by percentage", "Relation between Minimum of nights and number of Reviews", "Distribution of Availability 365", "Distribution of Accommodation price", "Distribution of Service fee", "Distribution of Price by NYC borough", "Distribution of Price by Host verification status", "Relation between Minimum of nights and price", "Relationship between Price and Service Fee"]

dropdown_items = []

for item in Graph:
    url = item.replace(" ", "_")
    dropdown_items.append(dbc.DropdownMenuItem(item, href="/"+url.lower()))

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.Col([
                    html.Img(src=dash.get_asset_url(
                        'logo2.png'), height="40px"),
                    dbc.NavbarBrand(
                        "Data Analysis and Visualization", className="ms-3")
                ],
                    width={"size": "auto"})
            ],
                align="center",
                className="g-0"),

            dbc.Row([
                dbc.Col([
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink("Home", href="/"),
                                    style={'margin-left': 50}),
                        dbc.NavItem(dbc.NavLink("About", href="/about"),
                                    style={'margin-left': 50}),
                        dbc.NavItem(dbc.NavLink(
                            "Time Line", href="/timeline"), style={'margin-left': 50}),
                        dbc.NavItem(dbc.DropdownMenu(
                            children=dropdown_items,
                            nav=True,
                            in_navbar=True,
                            label="Visual Representation"

                        ), style={'margin-left': 50})
                    ],
                        navbar=True
                    )
                ],
                    width={"size": "auto"})
            ],
                align="center"),
            dbc.Col(dbc.NavbarToggler(
                id="navbar-toggler", n_clicks=0)),

            dbc.Row([
                dbc.Col(
                    dbc.Collapse(
                        dbc.Nav([
                        ]
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True
                    )
                )
            ],
                align="center")
        ],
        fluid=True
    ),
    color="rgb(139 54 54)",
    dark=True
)


@ dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
