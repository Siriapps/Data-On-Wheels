# The 'dashboard.py' defines the main page of dashboard and all the contents of
# the three sub parts of the dashboard.

import pathlib
from dash.dependencies import Input, Output, State
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

app.scripts.config.serve_locally = True

# The d1Head, d2Head and d3Head define the page title of each of the three dashboard contents.
d1Head = html.Div([
    html.Header(
        dbc.Container(
            html.Div(
                dbc.Row(
                    dbc.Col(
                        [html.H1(
                            [
                                html.Img(
                                    src="data:image/png;base64,"
                                        "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP"
                                        "+gvaeTAAAOPklEQVR4nO1baXiUVZZ"
                                        "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",
                                    className="page-header-icon", alt="headIcon"),
                                " Sales Analysis"
                            ],
                            className="page-header-title"
                        ),
                            html.Div(
                                "Sales Analysis by brand -",

                                className="page-header-subtitle"
                            )
                        ],
                        className="col-auto mt-4"
                    ),
                    className="row align-items-center justify-content-between"
                ),
                className="pt-4"
            ),
            className="px-4"
        ),
        className="page-header page-header-dark bg-gradient-primary-to-secondary pb-10 m-4"
    )
])
d2Head = html.Div([
    html.Header(
        dbc.Container(
            html.Div(
                dbc.Row(
                    dbc.Col(
                        [html.H1(
                            [
                                html.Img(
                                    src="data:image/png;base64,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",
                                    className="page-header-icon", alt="headIcon"),
                                " Factors affecting sales"
                            ],
                            className="page-header-title"
                        ),
                            html.Div(
                                "Below is the analysis of the factors that are most likely to effect sales -",

                                className="page-header-subtitle"
                            )
                        ],
                        className="col-auto mt-4"
                    ),
                    className="row align-items-center justify-content-between"
                ),
                className="pt-4"
            ),
            className="px-4"
        ),
        className="page-header page-header-dark bg-gradient-primary-to-secondary pb-10 m-4"
    )
])
d3Head = html.Div([
    html.Header(
        dbc.Container(
            html.Div(
                dbc.Row(
                    dbc.Col(
                        [html.H1(
                            [
                                html.Img(
                                    src="data:image/png;base64,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",
                                    className="page-header-icon", alt="headIcon"),
                                " Car Specifications"
                            ],
                            className="page-header-title"
                        ),
                            html.Div(
                                "Below is the analysis of most popular car specifications -",

                                className="page-header-subtitle"
                            )
                        ],
                        className="col-auto mt-4"
                    ),
                    className="row align-items-center justify-content-between"
                ),
                className="pt-4"
            ),
            className="px-4"
        ),
        className="page-header page-header-dark bg-gradient-primary-to-secondary pb-10 m-4"
    )
])

# d1, d2, d3 define the three dashboards
d1 = html.Div([
    d1Head,
    html.Iframe(srcDoc='''
    <div class='tableauPlaceholder' id='viz1653315520308' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SalesAnalysis_16532472068720&#47;Overpast3years_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SalesAnalysis_16532472068720&#47;Overpast3years_1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SalesAnalysis_16532472068720&#47;Overpast3years_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1653315520308');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>                ''',
                style={"height": "100vh", "width": "100vw", }),
], className="mx-4")

d2 = html.Div([
    d2Head,
    html.Iframe(srcDoc='''
            <div class='tableauPlaceholder' id='viz1653280857848' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ef&#47;EffectingFactors&#47;Modelcount&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='EffectingFactors&#47;Modelcount' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ef&#47;EffectingFactors&#47;Modelcount&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1653280857848');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='900px';vizElement.style.height='950px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='900px';vizElement.style.height='950px';} else { vizElement.style.width='100%';vizElement.style.height='1050px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        ''', style={"height": "100vh", "width": "100vw"}),
], className="mx-4")

d3 = html.Div([
    d3Head,
    html.Iframe(srcDoc='''
    <div class='tableauPlaceholder' id='viz1653302251472' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;Carspecifications&#47;Gears&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Carspecifications&#47;Gears' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ca&#47;Carspecifications&#47;Gears&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1653302251472');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='900px';vizElement.style.height='750px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='900px';vizElement.style.height='750px';} else { vizElement.style.width='100%';vizElement.style.height='750px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>        ''',
                style={"height": "100vh", "width": "100vw"}),
], className="mx-4")

# These cards depict a brief overview of the data used for making the dashboards
cards = html.Div([
    dbc.Row([
        dbc.Col(className="col-2"),
        dbc.Col(
            html.H3("Data Brief"),
            className="text-center",
        ),
        dbc.Col(className="col-2")
    ]),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    html.Div(
                        [
                            html.H5("Brands", className="m-b-20 fw-bolder"),
                            html.H2(
                                [html.I(className="fa-solid fa-car-side f-right",
                                        style={"font-size": "50px"}),
                                 html.Span("15+", className="fw-bold")],
                            )
                        ],
                        className="card-block"
                    ),
                    className="card bg-c-blue order-card"
                ),
                className="col-md-5 col-xl-3 col-sm-4 col-12"
            ),
            dbc.Col(
                dbc.Card(
                    html.Div(
                        [
                            html.H5("Years", className="m-b-20 fw-bolder"),
                            html.H2(
                                [html.I(className="fa-regular fa-calendar-days f-right",
                                        style={"font-size": "50px"}),
                                 html.Span("3", className="fw-bold")],
                            )
                        ],
                        className="card-block"
                    ),
                    className="card bg-c-green order-card"
                ),
                className="col-md-5 col-xl-3 col-sm-4 col-12"
            ),
            dbc.Col(
                dbc.Card(
                    html.Div(
                        [
                            html.H5("Customer Data", className="m-b-20 fw-bolder"),
                            html.H2(
                                [html.I(className="fa-solid fa-users f-right",
                                        style={"font-size": "50px"}),
                                 html.Span("8000+", className="fw-bold")],
                            )
                        ],
                        className="card-block"
                    ),
                    className="card bg-c-yellow order-card"
                ),
                className="col-md-5 col-xl-3 col-sm-4 col-12"
            ),
            dbc.Col(
                dbc.Card(
                    html.Div(
                        [
                            html.H5("Graphs", className="m-b-20 fw-bolder"),
                            html.H2(
                                [html.I(className="fa-solid fa-chart-column f-right",
                                        style={"font-size": "50px"}),
                                 html.Span("20+", className="fw-bold")],
                            )
                        ],
                        className="card-block"
                    ),
                    className="card bg-c-pink order-card"
                ),
                className="col-md-5 col-xl-3 col-sm-4 col-12"
            ),

        ]
    )],
    className="mx-5 my-2"
)

# table defines the dashboard contents(a brief index of the three dashboards)
table = html.Div(
    [
        dbc.Row([
            dbc.Col(className="col-2"),
            dbc.Col(
                html.H3("Dashboard Contents"),
                className="text-center"
            ),
            dbc.Col(className="col-2")
        ]),

        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.Div(
                            dcc.Link([
                                html.H4("Sales Analysis", className="m-b-20 fw-bolder")
                            ], href="/page-2/1", className="card-title")
                        ),
                        dbc.Row(
                            [
                                dbc.Col([
                                    html.Img(
                                        src="data:image/png;base64,"
                                            "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP"
                                            "+gvaeTAAANaElEQVR4nO1baXRUx5X"
                                            "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",
                                        className="f-left", height="inherit",
                                        alt="subcontent"
                                    ),
                                    dbc.Col([
                                        html.P("- over past 3 Years"),
                                        html.P("- Yearly"),
                                        html.P("- Monthly by Brand"),
                                        html.P("- Brand by Month sales"),
                                        html.P("- Market share"),

                                    ],
                                        align="center",
                                        width={'offset': 4}
                                    )

                                ]),
                            ], className="cardText"
                        )
                    ],
                        className="p-5"
                    )

                ), className="col-md-6 col-xl-6 col-sm-6 col-12", align="center"
            ),
            justify="center", className="mt-1"
        ),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.Div(
                            dcc.Link([
                                html.H4("Factors effecting sales", className="m-b-20 fw-bolder")
                            ], href="/page-2/2", className="card-title")
                        ),
                        dbc.Row(
                            [
                                dbc.Col([
                                    html.Img(
                                        src="data:image/png;base64,"
                                            "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP"
                                            "+gvaeTAAANaElEQVR4nO1baXRUx5X"
                                            "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",
                                        className="f-left", height="inherit",
                                        alt="subcontent"
                                    ),
                                    dbc.Col([
                                        html.P("- Model count"),
                                        html.P("- Price"),
                                        html.P("- Advertising"),
                                        html.P("- Customers"),

                                    ],
                                        align="center",
                                        width={'offset': 4}
                                    )

                                ]),
                            ], className="cardText"
                        )
                    ],
                        className="p-5"
                    )

                ), className="col-md-6 col-xl-6 col-sm-6 col-12", align="center"
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.Div(
                            dcc.Link([
                                html.H4("Car Specifications", className="m-b-20 fw-bolder")
                            ], href="/page-2/3", className="card-title")
                        ),
                        dbc.Row(
                            [
                                dbc.Col([
                                    html.Img(
                                        src="data:image/png;base64,"
                                            "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP"
                                            "+gvaeTAAANaElEQVR4nO1baXRUx5X"
                                            "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",
                                        className="f-left", height="inherit",
                                        alt="subcontent"
                                    ),
                                    dbc.Col([
                                        html.P("- Body Type"),
                                        html.P("- Fuel Type"),
                                        html.P("- Seat fabric"),
                                        html.P("- Gear"),

                                    ],
                                        align="center",
                                        width={'offset': 4}
                                    )

                                ]),
                            ], className="cardText"
                        )
                    ],
                        className="p-5"
                    )

                ), className="col-md-6 col-xl-6 col-sm-6 col-12", align="center"
            ),

        ],
            className="mt-3"
        )

    ],
    className="px-5 pb-5 pt-1", style={'background-color': 'rgba(234, 232, 253,0.1)'}
)

page = html.Div(
    [cards,
     table]
)
