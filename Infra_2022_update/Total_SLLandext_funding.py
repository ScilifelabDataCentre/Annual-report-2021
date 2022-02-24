# Script creates a pie chart with amount of funding

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS,
)

Unit_data = pd.read_excel(
    "data/Single data 2021.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fund_data = pd.read_excel(
    "Data/Other funding 2021.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Need to also add instrument data

Unit_data.rename(
    columns={
        "Funding 2021 SciLifeLab (kSEK)": "Amount (kSEK)",
    },
    inplace=True,
)

SLL_funding = Unit_data[["Unit", "Platform", "Amount (kSEK)"]]
SLL_funding.insert(loc=2, column="Financier", value="SciLifeLab")

# Separate SciLifeLab instrument funding to add
instru_funding = Unit_data[["Unit", "Platform", "SciLifeLab Instrument Funding 2021"]]
instru_funding.rename(
    columns={
        "SciLifeLab Instrument Funding 2021": "Amount (kSEK)",
    },
    inplace=True,
)
instru_funding.insert(loc=2, column="Financier", value="SciLifeLab Instrument")

# Remove platform number from data on other funding
other_funding = fund_data[["Unit", "Platform", "Financier", "Amount (kSEK)"]]

# combine the two datasets
Funding_comb = pd.concat([SLL_funding, instru_funding, other_funding])

# Need to make a new column to enable grouping of financiers into University/other

Funding_comb["Group_finance"] = Funding_comb["Financier"].replace(
    dict.fromkeys(
        [
            "Universities",
            "UU",
            "Chalmers",
            "LiU",
            "SLU",
            "LU",
            "UmU",
            "KTH",
            "SU",
            "GU",
            "KI",
            "ÖRU",
        ],
        "University",
    ),
    regex=True,
)

Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
    dict.fromkeys(
        ["University hospital", "County council", "ALF"],
        "Healthcare",
    ),
    regex=True,
)

Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
    dict.fromkeys(
        ["Elixir", "Nordforsk", "SSF", "Vinnova", "Industry", "Erling-Persson", "EU"],
        "Other",
    ),
    regex=True,
)
# print(Funding_comb["Group_finance"].unique())

colours = [
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[16],
]

Funding_comb_group = Funding_comb.groupby(["Group_finance"]).sum().reset_index()
Funding_comb_group["Funding_MSEK"] = (
    (Funding_comb_group["Amount (kSEK)"] / 1000).round().astype(int)
)

# print(Funding_comb_group)

fig = go.Figure(
    go.Pie(
        values=Funding_comb_group["Funding_MSEK"],
        labels=Funding_comb_group["Group_finance"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} <br>(%{value})",
)
fig.update_layout(
    margin=dict(l=100, r=100, b=100, t=100),
    font=dict(size=34),
    showlegend=False,
    width=1000,
    height=1000,
    autosize=False,
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()

fig.write_image("Plots/total_funding_summary_pie.png", scale=3)
fig.write_image("Plots/total_funding_summary_pie.svg", scale=3)
