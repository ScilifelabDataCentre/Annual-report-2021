# generates barplot with units on y-axis and user income per FTE on x-axis

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS,
)

# Add data
Userfee_FTE = pd.read_excel(
    "data/Total User Fee per FTE 2021.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Userfee_FTE = Userfee_FTE.rename(columns={"User Fee/FTE (kSEK)": "Fee_per_FTE"})

Userfee_FTE["Mfunds"] = Userfee_FTE["Fee_per_FTE"] / 1000
# print(Userfee_FTE)

# Make stacked bar chart
fig = go.Figure(
    data=[
        go.Bar(
            name="User Fee per FTE",
            y=Userfee_FTE.Unit,
            x=Userfee_FTE.Mfunds,
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

Userfee_FTE_max = max(Userfee_FTE["Mfunds"])

# modify y-axis
fig.update_xaxes(
    title="<br>Total User Fee Income per FTE (MSEK)",  # keep the break to give y-axis title space between graph
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    dtick=0.5,  # 10 will work fine with most values
    range=[0, int(Userfee_FTE_max * 1.05)],
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()
fig.write_image("Plots/Userfee_per_FTE_2021.png")
fig.write_image("Plots/Userfee_per_FTE_2021.svg")
