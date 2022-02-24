# Chart will generate global pie chart looking at unique acadmic users by university

# Note: need to trim out data from xlsx file
import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS,
)

Acaduser_data = pd.read_excel(
    "data/Unique Academic Users per University.xlsx",
    sheet_name="Användare per lärosäte",
    header=5,
    engine="openpyxl",
    keep_default_na=False,
)

Acaduser_data.drop(Acaduser_data.columns[0], axis=1, inplace=True)

# OO requested percentages rounded to nearest percent for this graph
Acaduser_data["Round_perc"] = (Acaduser_data["Percent"] * 100).round().astype(int)
# print(Acaduser_data)

colours = [
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[1],
    SCILIFE_COLOURS[15],
    SCILIFE_COLOURS[18],
    SCILIFE_COLOURS[9],
    SCILIFE_COLOURS[16],
    SCILIFE_COLOURS[17],
]

# Edited this to fit more nicely
Acaduser_data["Affiliation"] = Acaduser_data["Affiliation"].replace(
    "Swedish University of Agricultural Sciences",
    "Swedish University of <br>Agricultural Sciences",
)
# Acaduser_data["Affiliation"] = Acaduser_data["Affiliation"].replace(
#     "Karolinska Institutet",
#     "Karolinska Institute",
# )
Acaduser_data["Affiliation"] = Acaduser_data["Affiliation"].replace(
    "University of Gothenburg",
    "University of<br> Gothenburg",
)
Acaduser_data["Affiliation"] = Acaduser_data["Affiliation"].replace(
    "Uppsala University",
    "Uppsala<br> University",
)

fig = go.Figure(
    go.Pie(
        values=Acaduser_data["Round_perc"],
        labels=Acaduser_data["Affiliation"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} <br>(%{value}%)",
)
fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    font=dict(size=23),
    showlegend=False,
    width=1000,
    height=1000,
    autosize=False,
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()

fig.write_image("Plots/Acaduser_data_pie.svg", scale=3)
fig.write_image("Plots/Acaduser_data_pie.png", scale=3)
