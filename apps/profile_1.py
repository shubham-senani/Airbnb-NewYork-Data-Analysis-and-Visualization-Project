import dash_bootstrap_components as dbc
from dash import html

card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="assets\lakshya.png",
                        className="m-3 mt-3 img-fluid rounded-circle",
                    ),
                    className="col-md-4 d-flex align-items-center",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("LAKSHYA LAKSHYAA", className="card-title mx-4"),
                            html.P(
                                "Data Analysis and Visualization"
                                "Team Captian"
                                "",
                                className="card-text mx-4",
                            ),
                            
                            dbc.Button("Github", href="/", color="danger", className="mx-4"),
                            dbc.Button("LinkedIn", href="/", color="danger", className="mx-4"),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 pr-5",
    style={"border-radius":"20px","maxWidth": "650px", "border":"none", "background": "linear-gradient(rgb(271, 159, 154) -40%, rgb(250, 250, 250) 90%)"},
)