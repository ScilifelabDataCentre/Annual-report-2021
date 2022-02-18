"""This script will generate a pie chart (like figure 6 in IEC report)"""

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2022 import (
    SCILIFE_COLOURS_NOGREY,
)

Facility_data = pd.read_excel(
    "Data/Single data 2021.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fund_data = pd.read_excel(
    "Data/Other funding 2021_mod.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Need to also potentially add instrument data

# Facility_data.rename(
#     columns={
#         "Funding 2020 SciLifeLab (kSEK)": "Amount (kSEK)",
#     },
#     inplace=True,
# )

# SLL_funding = Facility_data[["Facility", "Platform", "Amount (kSEK)"]]
# SLL_funding.insert(loc=2, column="Financier", value="SciLifeLab")

# Funding_comb = pd.concat([SLL_funding, fund_data])


# Funding_comb["Group_finance"] = Funding_comb["Financier"]


# Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
#     dict.fromkeys(
#         [
#             "Universities",
#             "UU",
#             "Chalmers",
#             "LiU",
#             "SLU",
#             "LU",
#             "UmU",
#             "KTH",
#             "SU",
#             "GU",
#             "KI",
#             "ÖRU",
#         ],
#         "University",
#     ),
#     regex=True,
# )

# Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
#     dict.fromkeys(
#         ["University hospital", "County council", "ALF"],
#         "Healthcare",
#     ),
#     regex=True,
# )

# Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
#     dict.fromkeys(
#         ["Elixir", "Nordforsk", "SSF", "Vinnova"],
#         "Other",
#     ),
#     regex=True,
# )


# colours = [
#     SCILIFE_COLOURS_NOGREY[2],
#     SCILIFE_COLOURS_NOGREY[14],
#     SCILIFE_COLOURS_NOGREY[4],
#     SCILIFE_COLOURS_NOGREY[0],
#     SCILIFE_COLOURS_NOGREY[12],
#     SCILIFE_COLOURS_NOGREY[8],
# ]

# Funding_comb_group = Funding_comb.groupby(["Group_finance"]).sum().reset_index()
# Funding_comb_group["Funding_MSEK"] = (
#     (Funding_comb_group["Amount (kSEK)"] / 1000).round().astype(int)
# )


# fig = go.Figure(
#     go.Pie(
#         values=Funding_comb_group["Funding_MSEK"],
#         labels=Funding_comb_group["Group_finance"],
#         hole=0.6,
#         marker=dict(colors=colours, line=dict(color="#000000", width=1)),
#         direction="clockwise",
#         sort=True,
#     )
# )

# fig.update_traces(
#     textposition="outside",
#     texttemplate="%{label} <br>(%{value})",
# )
# fig.update_layout(
#     margin=dict(l=100, r=100, b=100, t=100),
#     font=dict(size=34),
#     showlegend=False,
#     width=1000,
#     height=1000,
#     autosize=False,
# )
# if not os.path.isdir("Plots"):
#     os.mkdir("Plots")
# # fig.show()

# fig.write_image("Plots/total_fund_SLLandext.png", scale=3)
# fig.write_image("Plots/total_fund_SLLandext.svg", scale=3)
