# generates barplot with units on y-axis and number of FTEs on x-axis
# stacks divided by SciLifeLab, University funding and other funding

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS,
)

# Add data
FTEs_Unit = pd.read_excel(
    "data/FTEs per Unit 2021.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Make stacked bar chart
fig = go.Figure(
    data=[
        go.Bar(
            name="FTEs per Unit",
            y=FTEs_Unit.Unit,
            x=FTEs_Unit.FTEs,
            orientation="h",
            marker=dict(color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)),
        ),
    ]
)

# fig.update_layout(xaxis=go.layout.XAxis(tickangle=45))
fig.update_layout(
    plot_bgcolor="white",
    font=dict(size=33),
    autosize=False,
    margin=dict(r=0, t=0, b=0, l=0),
    width=3000,
    height=2000,
    yaxis={"categoryorder": "total ascending"},
)

# modify x-axis
fig.update_yaxes(
    title=" ",
    showgrid=True,
    linecolor="black",
)

FTEs_max = max(FTEs_Unit["FTEs"])

# modify y-axis
fig.update_xaxes(
    title="<br>Number of FTEs per Unit",  # keep the break to give y-axis title space between graph
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    dtick=20,  # 10 will work fine with most values
    range=[0, int(FTEs_max * 1.05)],
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()
fig.write_image("Plots/FTEs_per_Unit_2021.png")
fig.write_image("Plots/FTEs_per_Unit_2021.svg")
