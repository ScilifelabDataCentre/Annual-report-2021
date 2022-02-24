# Chart will generate global pie chart looking at funding and user fees across units (global analyses)

# Note: need to trim out data from xlsx file
import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS,
)

# header set to skip a few rows, as data not at top
Othfund_fee_data = pd.read_excel(
    "data/Other Funding and User Fees 2021.xlsx",
    sheet_name="RAW från Lars_funding categorie",
    header=2,
    engine="openpyxl",
    keep_default_na=False,
)
# delete first two (empty) columns
Othfund_fee_data.drop(Othfund_fee_data.columns[0:2], axis=1, inplace=True)

# values should be rounded to integers
Othfund_fee_data["Total_int"] = Othfund_fee_data["Total (MSEK)"].round().astype(int)
# print(Othfund_fee_data)

colours = [
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[16],
]

# Edited this to fit more nicely
Othfund_fee_data["Financier"] = Othfund_fee_data["Financier"].replace(
    "Swedish Governmental Funding Agencies",
    "Swedish Gov.<br>Funding Agencies<br>",
)
Othfund_fee_data["Financier"] = Othfund_fee_data["Financier"].replace(
    "Private Swedish Funding Agencies",
    "Private Swedish<br>Funding Agencies<br>",
)
Othfund_fee_data["Financier"] = Othfund_fee_data["Financier"].replace(
    "User Fees",
    "User Fees<br>",
)
Othfund_fee_data["Financier"] = Othfund_fee_data["Financier"].replace(
    "Universities",
    "Universities<br>",
)
Othfund_fee_data["Financier"] = Othfund_fee_data["Financier"].replace(
    "Healthcare",
    "Healthcare<br>",
)

fig = go.Figure(
    go.Pie(
        values=Othfund_fee_data["Total_int"],
        labels=Othfund_fee_data["Financier"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} (%{value})",
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

fig.write_image("Plots/Otherfunds_userfees_pie.svg", scale=3)
fig.write_image("Plots/Otherfunds_userfees_pie.png", scale=3)
