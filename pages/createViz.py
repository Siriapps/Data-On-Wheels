# The 'createVis.py' implements the functionality for the users to implement
# custom data and plot graphs.

import base64
import io

from app import app
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# page title
d1Head = html.Div([
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
                                " Create Visualization"
                            ],
                            className="page-header-title"
                        ),
                            html.Div(
                                "Upload a .csv or .xls file and plot graphs",

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

# upload files feature
Viz = html.Div([
    d1Head,
    html.Center([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '75vw',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
    ]),
    html.Div(id='output-data-upload')
], className="pl-3")


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    # parsing the uploaded file
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    global dff
    dff = df  # making a copy of dff to use it further throughout the code

    # displaying the data from uploaded file
    return html.Div([
        html.H5(filename, className="m-b-20 fw-bolder", style={'color': '#03387d'}),
        html.Center(
            dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
                                 style_header={
                                     'backgroundColor': '#010624',
                                     'color': 'white',
                                     'font-weight': 'bold',
                                     'font-family': 'Arial',
                                 },
                                 style_data={
                                     'backgroundColor': 'rgba(146, 193, 253,0.1)',
                                     'color': 'black',
                                     'font-family': 'Arial',
                                 },
                                 style_table={'overflowX': 'auto', 'width': '75vw'},
                                 page_action='native',
                                 page_size=10,

                                 )),

        # selecting graph type
        html.Div([
            html.H5("Select a Graph type", className="m-b-20 fw-bolder", style={'color': '#03387d'}),
            dbc.Row(dbc.Col(dcc.Dropdown(['Bar graph', 'Histogram', 'Pie chart'], id='demo-dropdown'),
                            className="col-sm-4 col-xl-8 col-md-6 mx-5")),

        ], className="mt-5 my-3"),

        # radio items for axes values
        dbc.Row([
            dbc.Col(
                [
                    html.Div([
                        html.Label(['Select a field'], style={'font-weight': 'bold'}),
                        dcc.RadioItems(
                            id='xaxis_raditem',
                            options=df.columns,
                            value=df.columns[0],
                            style={"width": "50%"}
                        ),
                    ]),
                ], class_name="", align="center"
            ),
            dbc.Col(
                [
                    html.Div([
                        html.Br(),
                        html.Label(['Select a field'], style={'font-weight': 'bold'}),
                        dcc.RadioItems(
                            id='yaxis_raditem',
                            options=df.columns,
                            # value=df.columns[1],
                            style={"width": "50%"}
                        ),
                    ]),
                ], class_name="", align="center"
            )
        ]),

        html.Div(id='dd-output-container', className="mx-4")

    ], className="m-5")


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    global val
    val = value
    return html.Div([
        dcc.Graph(id='the_graph')
    ]),


@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value'), ]
)
def update_graph(x_axis, y_axis):
    graph = px.bar(
        data_frame=dff,
        x=x_axis,
        y=y_axis,

    )

    if val == "Bar graph":
        graph = px.bar(
            data_frame=dff,
            x=x_axis,
            y=y_axis,
        )
    elif val == "Histogram":
        graph = px.histogram(
            data_frame=dff,
            x=x_axis,
        )
    elif val == "Pie chart":
        graph = px.pie(
            data_frame=dff,
            values=x_axis,
            names=y_axis,
        )

    return graph
