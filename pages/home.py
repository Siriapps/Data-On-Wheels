# The 'home.py' contains the main title and content of home page (excluding sidebar)

import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

homeJumbotron = html.Div(
    dbc.Container(
        [
            dbc.Col([
                html.H1("Data On Wheels", style={"color": 'white', "font-weight": "bold"}),
                html.P(
                    "Got doubts on trends? Want to know what’s wrong and what’s right? You are at the right place! "
                    "There are several visualizations made for you after a through analysis from accurate data. Just "
                    "visualize and decide. Don’t be data driven, be analytics driven!",
                    className="col-md-11"
                ),

                html.Hr(className="my-4 text-light"),
                html.Div([
                    html.P(
                        "Click to Discover more"
                    ),
                    dbc.Button("Next", color="light", href="/page-2", outline=True, className="btn-lg"),
                ], className="")

            ],
                className="col-md-6 mx-5 my-5"

            )

        ],
        fluid=True,
        className="text-white py-5",
    ),
    className="p-2 rounded-4 gx-5",
    id="jumbo",
)

homePage = html.Div(
    [
        homeJumbotron
    ]
)
