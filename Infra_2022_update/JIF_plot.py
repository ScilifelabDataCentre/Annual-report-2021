# This plot

import pandas as pd
import os
import plotly.graph_objects as go

from colour_science_2022 import (
    SCILIFE_COLOURS,
)

# infrastructure data
from JIF_dataprep import JIF_sub_group_inf

JIF_sub_group_inf16 = JIF_sub_group_inf[JIF_sub_group_inf["Year"] > 2015]


def JIF_1321_graph_func(input):
    JIFcounts = input
    # split down dataframes to enable stacking
    UnknownJIF = JIFcounts[(JIFcounts["JIFcat"] == "JIF unknown")]
    Undersix = JIFcounts[(JIFcounts["JIFcat"] == "JIF <6")]
    sixtonine = JIFcounts[(JIFcounts["JIFcat"] == "JIF 6-9")]
    ninetotwentyfive = JIFcounts[(JIFcounts["JIFcat"] == "JIF 9-25")]
    overtwentyfive = JIFcounts[(JIFcounts["JIFcat"] == "JIF >25")]
    # Make stacked bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                name="JIF unknown",
                x=UnknownJIF.Year,
                y=UnknownJIF.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[17], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF < 6",
                x=Undersix.Year,
                y=Undersix.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF 6 - 9",
                x=sixtonine.Year,
                y=sixtonine.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[4], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF 9 - 25",
                x=ninetotwentyfive.Year,
                y=ninetotwentyfive.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF > 25",
                x=overtwentyfive.Year,
                y=overtwentyfive.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[8], line=dict(color="#000000", width=1)
                ),
            ),
        ]
    )

    fig.update_layout(
        barmode="stack",
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=45),  # 58 for fellows
        margin=dict(r=250, t=0, b=0, l=0),
        width=2000,
        height=1200,
        showlegend=False,
    )
    # List years to use in x-axis
    Years = JIFcounts["Year"].unique().astype(str)
    Years_int = JIFcounts["Year"].unique()
    # modify x-axis
    fig.update_xaxes(
        title=" ",
        showgrid=True,
        linecolor="black",
        # add more years as needed
        ticktext=[
            "<b>" + Years[0] + "</b>",
            "<b>" + Years[1] + "</b>",
            "<b>" + Years[2] + "</b>",
            "<b>" + Years[3] + "</b>",
            "<b>" + Years[4] + "</b>",
            "<b>" + Years[5] + "</b>",
            "<b>" + Years[6] + "</b>",
            "<b>" + Years[7] + "</b>",
            "<b>" + Years[8] + "</b>",
        ],
        tickvals=[
            Years[0],
            Years[1],
            Years[2],
            Years[3],
            Years[4],
            Years[5],
            Years[6],
            Years[7],
            Years[8],
        ],
    )

    Year_one = JIFcounts[(JIFcounts["Year"] == Years_int[0])]
    Year_two = JIFcounts[(JIFcounts["Year"] == Years_int[1])]
    Year_three = JIFcounts[(JIFcounts["Year"] == Years_int[2])]
    Year_four = JIFcounts[(JIFcounts["Year"] == Years_int[3])]
    Year_five = JIFcounts[(JIFcounts["Year"] == Years_int[4])]
    Year_six = JIFcounts[(JIFcounts["Year"] == Years_int[5])]
    Year_seven = JIFcounts[(JIFcounts["Year"] == Years_int[6])]
    Year_eight = JIFcounts[(JIFcounts["Year"] == Years_int[7])]
    Year_nine = JIFcounts[(JIFcounts["Year"] == Years_int[8])]

    highest_y_value = max(
        Year_one["Count"].sum(),
        Year_two["Count"].sum(),
        Year_three["Count"].sum(),
        Year_four["Count"].sum(),
        Year_five["Count"].sum(),
        Year_six["Count"].sum(),
        Year_seven["Count"].sum(),
        Year_eight["Count"].sum(),
        Year_nine["Count"].sum(),
    )

    if highest_y_value < 10:
        yaxis_tick = 1
    if highest_y_value > 10:
        yaxis_tick = 2
    if highest_y_value > 20:
        yaxis_tick = 5
    if highest_y_value > 50:
        yaxis_tick = 10
    if highest_y_value > 100:
        yaxis_tick = 20
    if highest_y_value > 150:
        yaxis_tick = 40
    if highest_y_value > 500:
        yaxis_tick = 100
    if highest_y_value > 1000:
        yaxis_tick = 100

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, int(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/infra_1321_JIF.png")
    fig.write_image("Plots/infra_1321_JIF.svg")


def JIF_1621_graph_func(input):
    JIFcounts = input
    # split down dataframes to enable stacking
    UnknownJIF = JIFcounts[(JIFcounts["JIFcat"] == "JIF unknown")]
    Undersix = JIFcounts[(JIFcounts["JIFcat"] == "JIF <6")]
    sixtonine = JIFcounts[(JIFcounts["JIFcat"] == "JIF 6-9")]
    ninetotwentyfive = JIFcounts[(JIFcounts["JIFcat"] == "JIF 9-25")]
    overtwentyfive = JIFcounts[(JIFcounts["JIFcat"] == "JIF >25")]
    # Make stacked bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                name="JIF unknown",
                x=UnknownJIF.Year,
                y=UnknownJIF.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[17], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF < 6",
                x=Undersix.Year,
                y=Undersix.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF 6 - 9",
                x=sixtonine.Year,
                y=sixtonine.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[4], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF 9 - 25",
                x=ninetotwentyfive.Year,
                y=ninetotwentyfive.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF > 25",
                x=overtwentyfive.Year,
                y=overtwentyfive.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[8], line=dict(color="#000000", width=1)
                ),
            ),
        ]
    )

    fig.update_layout(
        barmode="stack",
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=55),  # 58 for fellows
        margin=dict(r=250, t=0, b=0, l=0),
        width=2000,
        height=1200,
        showlegend=False,
    )
    # List years to use in x-axis
    Years = JIFcounts["Year"].unique().astype(str)
    Years_int = JIFcounts["Year"].unique()
    # modify x-axis
    fig.update_xaxes(
        title=" ",
        showgrid=True,
        linecolor="black",
        # add more years as needed
        ticktext=[
            "<b>" + Years[0] + "</b>",
            "<b>" + Years[1] + "</b>",
            "<b>" + Years[2] + "</b>",
            "<b>" + Years[3] + "</b>",
            "<b>" + Years[4] + "</b>",
            "<b>" + Years[5] + "</b>",
            # "<b>" + Years[6] + "</b>",
            # "<b>" + Years[7] + "</b>",
            # "<b>" + Years[8] + "</b>",
        ],
        tickvals=[
            Years[0],
            Years[1],
            Years[2],
            Years[3],
            Years[4],
            Years[5],
            # Years[6],
            # Years[7],
            # Years[8],
        ],
    )

    Year_one = JIFcounts[(JIFcounts["Year"] == Years_int[0])]
    Year_two = JIFcounts[(JIFcounts["Year"] == Years_int[1])]
    Year_three = JIFcounts[(JIFcounts["Year"] == Years_int[2])]
    Year_four = JIFcounts[(JIFcounts["Year"] == Years_int[3])]
    Year_five = JIFcounts[(JIFcounts["Year"] == Years_int[4])]
    Year_six = JIFcounts[(JIFcounts["Year"] == Years_int[5])]
    # Year_seven = JIFcounts[(JIFcounts["Year"] == Years_int[6])]
    # Year_eight = JIFcounts[(JIFcounts["Year"] == Years_int[7])]
    # Year_nine = JIFcounts[(JIFcounts["Year"] == Years_int[8])]

    highest_y_value = max(
        Year_one["Count"].sum(),
        Year_two["Count"].sum(),
        Year_three["Count"].sum(),
        Year_four["Count"].sum(),
        Year_five["Count"].sum(),
        Year_six["Count"].sum(),
        # Year_seven["Count"].sum(),
        # Year_eight["Count"].sum(),
        # Year_nine["Count"].sum(),
    )

    if highest_y_value < 10:
        yaxis_tick = 1
    if highest_y_value > 10:
        yaxis_tick = 2
    if highest_y_value > 20:
        yaxis_tick = 5
    if highest_y_value > 50:
        yaxis_tick = 10
    if highest_y_value > 100:
        yaxis_tick = 20
    if highest_y_value > 150:
        yaxis_tick = 40
    if highest_y_value > 500:
        yaxis_tick = 100
    if highest_y_value > 1000:
        yaxis_tick = 100

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, int(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/infra_1621_JIF.png")
    fig.write_image("Plots/infra_1621_JIF.svg")


# make plots by applying function

JIF_1321_graph_func(JIF_sub_group_inf)
JIF_1621_graph_func(JIF_sub_group_inf16)
