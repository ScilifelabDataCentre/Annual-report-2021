# generates stacked barplot with units on y-axis and funding amount on x-axis,
# stacks divided by SciLifeLab, University funding and other funding

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS,
)

# Need data on SciLifeLab funding, and on 'other' funding (held in different files)
Unit_data = pd.read_excel(
    "data/Single data 2021.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fund_data = pd.read_excel(
    "data/Other funding 2021.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Now need to edit data and then combine the two

Unit_data.rename(
    columns={
        "Funding 2021 SciLifeLab (kSEK)": "Amount (kSEK)",
    },
    inplace=True,
)

# add in SciLifeLab as a financier to SLL data
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
        [
            "University hospital",
            "County council",
            "ALF",
            "Elixir",
            "Nordforsk",
            "SSF",
            "Vinnova",
            "KAW",
            "VR",
            "EU",
            "Industry",
            "Erling-Persson",
        ],
        "Other",
    ),
    regex=True,
)

# convert funding units
Funding_comb = Funding_comb.rename(columns={"Amount (kSEK)": "funds"})
Funding_comb["Mfunds"] = Funding_comb["funds"] / 1000

# check replacements
# Funding_comb.to_excel("testfilefundbar.xlsx")
# check 3 categories
# print(Funding_comb["Group_finance"].unique())

# group by the individual funding type (scilifelab, SLL instrument funding, uni, other) and unit

Funding_summed = Funding_comb.groupby(["Unit", "Group_finance"]).sum().reset_index()

SciLifeLab_fund = Funding_summed[(Funding_summed["Group_finance"] == "SciLifeLab")]
Instrument_fund = Funding_summed[
    (Funding_summed["Group_finance"] == "SciLifeLab Instrument")
]
University_fund = Funding_summed[(Funding_summed["Group_finance"] == "University")]
Other_fund = Funding_summed[(Funding_summed["Group_finance"] == "Other")]

# Make stacked bar chart
fig = go.Figure(
    data=[
        go.Bar(
            name="SciLifeLab Instrument funds",
            y=Instrument_fund.Unit,
            x=Instrument_fund.Mfunds,
            orientation="h",
            marker=dict(color=SCILIFE_COLOURS[4], line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="SciLifeLab funds",
            y=SciLifeLab_fund.Unit,
            x=SciLifeLab_fund.Mfunds,
            orientation="h",
            marker=dict(color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="University funds",
            y=University_fund.Unit,
            x=University_fund.Mfunds,
            orientation="h",
            marker=dict(color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="Other funds",
            y=Other_fund.Unit,
            x=Other_fund.Mfunds,
            orientation="h",
            marker=dict(color=SCILIFE_COLOURS[8], line=dict(color="#000000", width=1)),
        ),
    ]
)
# fig.update_layout(xaxis=go.layout.XAxis(tickangle=45))
fig.update_layout(
    barmode="stack",
    plot_bgcolor="white",
    font=dict(size=40),
    autosize=False,
    margin=dict(r=0, t=50, b=0, l=50),
    width=3000,
    height=2200,
    yaxis={"categoryorder": "total ascending"},
    showlegend=True,
    legend=dict(
        itemwidth=30,
        traceorder="normal",
        orientation="h",
        yanchor="top",
        y=1.06,
        xanchor="left",
        x=-0.3,
        font=dict(size=55),
    ),
)

# modify x-axis
fig.update_yaxes(
    title=" ",
    showgrid=True,
    linecolor="black",
)

Funding_grpmax = Funding_comb.groupby(["Unit"]).sum().reset_index()
Funding_max = max(Funding_grpmax["Mfunds"])

# modify y-axis
fig.update_xaxes(
    title="Funding (MSEK)<br>",  # keep the break to give y-axis title space between graph
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    dtick=10,  # 10 will work fine with most values
    range=[0, int(Funding_max * 1.10)],
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()
fig.write_image("Plots/Unitfunding_barchart_2021.png")
fig.write_image("Plots/Unitfunding_barchart_2021.svg")
