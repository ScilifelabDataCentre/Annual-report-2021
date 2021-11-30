import pandas as pd

# get the data
infra = pd.read_excel(
    "Data/test.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# filter as needed (just 2021, only need a couple of columns)

infra_2021 = infra[(infra["Year"] == 2021)]
infra_2021 = infra_2021[["DOI", "Labels"]]

# Replace string values with respect to the rules set out by OO

infra_2021["Labels"] = infra_2021["Labels"].apply(
    lambda x: x.replace("NGI Uppsala (SNP&SEQ Technology Platform)", "")
)

infra_2021["Labels"] = infra_2021["Labels"].apply(
    lambda x: x.replace("NGI Uppsala (Uppsala Genome Center)", "")
)

infra_2021["Labels"] = infra_2021["Labels"].apply(
    lambda x: x.replace("NGI Stockholm (Genomics Applications)", "")
)

infra_2021["Labels"] = infra_2021["Labels"].apply(
    lambda x: x.replace("NGI Stockholm (Genomics Production)", "")
)

infra_2021["Labels"] = infra_2021["Labels"].apply(lambda x: x.replace("||||", "|"))

infra_2021["Labels"] = infra_2021["Labels"].apply(lambda x: x.replace("|||", "|"))

infra_2021["Labels"] = infra_2021["Labels"].apply(lambda x: x.replace("||", "|"))

# Count was incorrect when NGI at front because it often started with "|"" after others deleted
# corrected this by conditionally replacing based on start value

infra_2021["Labels"] = infra_2021["Labels"].apply(
    lambda x: f"National Genomics Infrastructure"
    if x.startswith("|National Genomics Infrastructure")
    else x
)

# split values to different columns, so there is one unit per column

new_bits = infra_2021["Labels"].str.split("|", expand=True)

# Now count the number of 'non empty columns' in each row
# This will how how many units worked on a publication

new_bits["No_units"] = new_bits.count(axis=1)

# Need to work out a percantage to use in the report

Perc_collab = (
    (new_bits["No_units"].map(lambda x: x > 1).sum()) / (new_bits["No_units"].count())
) * 100

# Output percentage, so that it can be communicated to OO

print(Perc_collab)
