# This is the main page that is to be run
# The 'main.py' contains the overall application layout and links/paths to different pages in the application

from app import app
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

from pages.createViz import Viz
from pages.home import homePage
from pages.dashboard import d1, d2, cards, d3, page
from pages.sidebar import sidebar

navbar = html.Div([
    dbc.Col(html.Img(src="../assets/logo.jpg", style={'width': '5rem', 'border-radius': '50%'},
                     id="logo-icon", alt="logo"),
            width="auto",
            # vertically align the toggle in the center
            id="logo-toggle"
            ),

], id="header")

content = html.Div(id="page-content",
                   children=[
                   ])

app.layout = html.Div([dcc.Location(id="url"), sidebar, navbar, content],
                      style={'width': '100vw', 'overflow-x': 'hidden', 'margin': '0', 'padding': '0'})


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell the page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in [1, 2, "2/1", "2/2", "2/3", 3, 4]],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False, False, False, False, False
    if pathname == "/page-2/1":
        return False, True, True, False, False, False, False
    if pathname == "/page-2/2":
        return False, True, False, True, False, False, False
    if pathname == "/page-2/3":
        return False, True, False, False, True, False, False
    return [pathname == f"/page-{i}" for i in [1, 2, "2/1", "2/2", "2/3", 3, 4]]


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return homePage
    elif pathname == "/page-2":
        return page
    elif pathname == "/page-2/1":
        return d1
    elif pathname == "/page-2/2":
        return d2
    elif pathname == "/page-2/3":
        return d3
    elif pathname == "/page-3":
        return Viz
    # If the user tries to reach a different page, return a 404 message
    return [html.Div(
        dbc.Container(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(className="my-2"),
                html.P(f"The pathname {pathname} was not recognised...",
                       className="lead"),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )]


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
