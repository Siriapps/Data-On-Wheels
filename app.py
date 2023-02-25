# The 'app.py' helps initialize the server and load external style sheets

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    external_stylesheets=[dbc.icons.FONT_AWESOME,dbc.icons.BOOTSTRAP,dbc.themes.BOOTSTRAP,'./assets/dashbrd.css','./assets/analytics.css','./assets/sidebarStyle.css','./assets/home.css','https://codepen.io/chriddyp/pen/bWLwgP.css',
                          'https://fonts.googleapis.com/css?family=Merriweather|Roboto|Exo|Nunito Sans'],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.config.suppress_callback_exceptions = True

server = app.server

server.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE=None,
)