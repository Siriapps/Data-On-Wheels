# The 'sidebar.py' contains the complete sidebar content, toggle action and
# navigation links for all the sidebar contents.

import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, State

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
from app import app

sidebar_header = dbc.Row([
    dbc.Col(html.Img(src="../assets/fullL.jpg", alt="fullLogo", style={'width': '12rem', 'height': '8.5rem'}),
            id="fullLogo"),
    dbc.Col(
        [
            html.Button(
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color
                style={
                    "color": "rgba(88,217,239,.5)",
                },
                id="navbar-toggle",
            ),
            html.Span(className="sidebar-toggler-icon btn", id="sidebar-toggle", ),

        ],
        # the column containing the toggle will be only as wide as the
        # toggle, resulting in the toggle being right aligned
        width="auto",
        # vertically align the toggle in the center
        align="center",
    ),
])

dropdown = html.Div([
    html.Li(
        # use Row and Col components to position the chevrons
        dbc.Row(
            [
                dbc.Col(dbc.NavLink("Dashboard", className="dashBrd", href="/page-2", id="page-2-link")),

                dbc.Col(
                    dcc.Link([
                        html.Img(src="../assets/iconDrop.jpg", alt="DropdownIcon", className="menu-icon",
                                 style={"width": "28px", "height": "30px"})
                    ], href="/page-2"), width="auto",
                ),
            ],
        ),
        id="submenu-1",
    ),
    # we use the Collapse component to hide and reveal the navigation links
    dbc.Collapse(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.NavLink("Sales Analysis",
                                        href="/page-2/1", id="page-2/1-link",
                                        style={"font-size": "14px"}),
                            width={"offset": 1}
                            ),

                    dbc.Col(
                        dcc.Link([
                            html.Img(src="data:image/png;base64,"
                                         "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP"
                                         "+gvaeTAAACXklEQVR4nO2Yy24TMRSGx6y64Q3IqjTzBoSLeAj6UohF+hhIbS59AVhRHgH2ZQMS6YRkS8XHwo4YBdsaj8c9aXU+KRt75vg/vy8n46pSFEVRFEVxAJ+AK2kdXQBqYAls3e8SqHODAjCQxmIAY6DhfxpglBP4vhiw9CS/4yIn8H0xYBMxYNM1zqOSIlNxy3oB/ALWwBx42uo3wAvgrKqqx7FQOSJEVoBL/sYzmzfAKXAGfIvMepvzHCFSBiw6JncNTIE3AcNWwJMcIVIGxPb0H5f0c8C03jkGZtiTfwOcZyXvggYNAEbYfbl1Ay6BcdaA/2LHDGiGGKOrEK8BLnnfkmtyTQAmbumGmOXETxUTMmAeEbjoOdYR8A64jc0+cJKfWXdRIQO2EZHrHuNMgK/u/VtnRA28B75jt8T8TpN3wvoYEDqkTrCn+xr44ZKr92b9CzDpofNzRE//b5mIAZeRAdtcY2v2Kf7/6jt+A2+BoxydIUoYUAcSWmFr8tQl34WfwLPeIiUMcH0j4AK7PxtsDT5u9RvsNphit0WI7LImYkBinKS6TuKeHsqAkh9DHyN9HzxtLyPPv8rU0p0BV0DowmKFp7SlzuhQK8AnfBADXKwxtpZvsKVwRuvz1jfuwRpAqbq7N+5dG2D2G3YvG2OMrz0YaO/5VFLjD6XnoG6EJFADSgUufWYMRbEz4NCeD6FbQFqANGqAtABp1ABpAdKoAdICpFEDpAVIowZIC5BGDZAWII0aIC1AGjVAWoA0aoC0AGmCl6IPlCtjzOt2g28FHMyVdQEe8uQqiqIoipLIXw2wf3+dBK8cAAAAAElFTkSuQmCC",
                                     className="menu-icon text-white",
                                     alt="sales icon",
                                     style={"width": "24px", "height": "24px", }, )
                        ], href="/page-2/1", className="navPage"), width="auto",
                    ),
                ],
                className="nav-item",
            ),
            dbc.Row(
                [
                    dbc.Col(dbc.NavLink("Factors effecting sales",
                                        href="/page-2/2", id="page-2/2-link",
                                        style={"font-size": "14px"}),
                            width={"offset": 1},
                            ),
                    dbc.Col(
                        dcc.Link([
                            html.I(className="fa-solid fa-chart-pie menu-icon text-light", )
                        ], href="/page-2/2", className="navPage", title="factorsIcon"), width="auto",
                    ),
                ],
                className="nav-item",
            ),
            dbc.Row(
                [
                    dbc.Col(dbc.NavLink("Car Specifications",
                                        href="/page-2/3", id="page-2/3-link",
                                        style={"font-size": "14px"}),
                            width={"offset": 1}
                            ),

                    dbc.Col(
                        dcc.Link([
                            html.Img(
                                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA"
                                    "/wD/AP+gvaeTAAACXklEQVR4nO2Yy24TMRSGx6y64Q3IqjTzBoSLeAj6UohF"
                                    "+hhIbS59AVhRHgH2ZQMS6YRkS8XHwo4YBdsaj8c9aXU+KRt75vg/vy8n46pSFEVRFEVxAJ"
                                    "+AK2kdXQBqYAls3e8SqHODAjCQxmIAY6DhfxpglBP4vhiw9CS/4yIn8H0xYBMxYNM1zqOSIlNxy3oB"
                                    "/ALWwBx42uo3wAvgrKqqx7FQOSJEVoBL"
                                    "/sYzmzfAKXAGfIvMepvzHCFSBiw6JncNTIE3AcNWwJMcIVIGxPb0H5f0c8C03jkGZtiTfwOcZyXvggYNAEbYfbl1Ay6BcdaA "
                                    "/2LHDGiGGKOrEK8BLnnfkmtyTQAmbumGmOXETxUTMmAeEbjoOdYR8A64jc0+cJKfWXdRIQO2EZHrHuNMgK/u"
                                    "/VtnRA28B75jt8T8TpN3wvoYEDqkTrCn+xr44ZKr92b9CzDpofNzRE//b5mIAZeRAdtcY2v2Kf7/6jt+A2+BoxydIUoYUAcSWmFr8tQl34WfwLPeIiUMcH0j4AK7PxtsDT5u9RvsNphit0WI7LImYkBinKS6TuKeHsqAkh9DHyN9HzxtLyPPv8rU0p0BV0DowmKFp7SlzuhQK8AnfBADXKwxtpZvsKVwRuvz1jfuwRpAqbq7N+5dG2D2G3YvG2OMrz0YaO/5VFLjD6XnoG6EJFADSgUufWYMRbEz4NCeD6FbQFqANGqAtABp1ABpAdKoAdICpFEDpAVIowZIC5BGDZAWII0aIC1AGjVAWoA0aoC0AGmCl6IPlCtjzOt2g28FHMyVdQEe8uQqiqIoipLIXw2wf3+dBK8cAAAAAElFTkSuQmCC",
                                alt="car spec icons",
                                className="menu-icon text-white",
                                style={"width": "24px", "height": "24px"})
                        ], href="/page-2/3", className="navPage"), width="auto",
                    ),
                ],
                className="nav-item",
            ),
        ],
        id="submenu-1-collapse",
    ),
], id="dropDown")


# this function is used to toggle the is_open property of each Collapse
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# this function applies the "open" class to rotate the chevron
def set_navitem_class(is_open):
    if is_open:
        return "open"
    return ""


for i in [1, 2]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

sidebar = html.Div(
    [
        sidebar_header,
        # sidebar_menu,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen

        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.Row(
                        [
                            dbc.Col(dbc.NavLink("Home", active=True, href="/page-1", id="page-1-link"), ),
                            dbc.Col(
                                dcc.Link([
                                    html.I(className="home-icon mr-3 menu-icon", )
                                ], href="/page-1", className="navPage", title="homeIcon"), width="auto",
                            ),
                        ],
                        className="my-1",
                    ),
                    dbc.Nav(dropdown, vertical=True),
                    dbc.Row(
                        [
                            dbc.Col(dbc.NavLink("Create Viz", href="/page-3", id="page-3-link"), ),
                            dbc.Col(
                                dcc.Link([
                                    html.I(className="create-icon mr-3 menu-icon", )
                                ], href="/page-3", className="navPage", title="interactIcon"), width="auto",
                            ),
                        ],
                        className="my-1",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(dbc.NavLink("Find your car",
                                                href="https://engage.kb.us-central1.gcp.cloud.es.io:9243/app"
                                                     "/dashboards#/view/d80aa910-de50-11ec-8bcb-2b59f6170ad5?embed"
                                                     "=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),"
                                                     "time:(from:now-15m,to:now))&_a=",
                                                id="page-4-link", target="_blank"), ),
                            dbc.Col(
                                dcc.Link([
                                    html.Img(
                                        src="data:image/png;base64,"
                                            "iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP"
                                            "+gvaeTAAAB0UlEQVRoge2awUoDMRCG/xHv9qBIlaIiiAfx2IO+RUt9IsH3EA9CQW"
                                            "/6ACJq30JtEdRi9az9PZiC1TbJ7GbbLZvv0tL8mcy"
                                            "/00lyWCBSEEjWSb7wP88ka9POzxuSnREmBrSnnZ83g4x9f0"
                                            "/LXOiA0yIayRsqIyQ3STZJflga2asHXPNJvpM8JbmR3N54E6O2U5Uh7Xz"
                                            "+bNfrrvw0FTkCsKgxH4glAIcukfhGI9kDsKDNQkSG1hhVJQ+6ImJ9iBojwfd"
                                            "+BV8iMm8TFHPXyjPRSN7IwsgDgBqAkowBQAlAHcBjBuvb8Ty8"
                                            "+iR3FDF3zRwXn5M20jLaCsm2RdchWTHaVggjof9aZ+bzAMCqRbcCoGG"
                                            "+nwfOwY5nRbaN9tZDe2O0WyEqEuxk/3sV0eKIH092Nb+fKMlrklcW7dC4q9o"
                                            "+ZFWRPgBbcq5xNUFvv0n7xCN2cXrE6jINJBu2cRFpZrW2Fc9zpGy05cDayZ0jGVOcHolGZhZLI+4FXGM/abOHqEiqy2KoWHHXmllij0woVuyRvBGN5A2NkV5mWbh5cwk0Ri5TJJKWC5dAs2utAbgDsJwmowQ8AaiKiPW1D++KiMg9gCqAEwDddLl58QrgGB4mInnkGxmclNixDrhJAAAAAElFTkSuQmCC",
                                        alt="car find icons",
                                        className="menu-icon text-white",
                                        style={"width": "24px", "height": "24px"})
                                ],
                                    href="https://engage.kb.us-central1.gcp.cloud.es.io:9243/app/dashboards#/view"
                                         "/d80aa910-de50-11ec-8bcb-2b59f6170ad5?embed=true&_g=(filters:!(),"
                                         "refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=",
                                    className="navPage", title="interactIcon", target="_blank"), width="auto",
                            ),
                        ],
                        className="my-1",
                    ),

                ],
                vertical=True,
                pills=True,
            ),

            id="collapse",
        ),
    ],
    id="sidebar",
)
