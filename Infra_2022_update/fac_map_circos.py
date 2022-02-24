import pandas as pd
import numpy as np


### FAC MAP
# to their labels in the publication database
fac_map_input = pd.read_excel(
    "data/Reporting Units 2021_circos.xlsx",
    sheet_name="Reporting units",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_map_input["PDB label"] = (
    fac_map_input["PDB label"]
    .replace(to_replace="\(", value="", regex=True)
    .replace(to_replace="\)", value="", regex=True)
)

fac_map_input = fac_map_input[["Unit", "PDB label"]]
fac_map_input = fac_map_input.replace("", np.nan)
fac_map_input["PDB label"] = fac_map_input["PDB label"].fillna(fac_map_input["Unit"])
fac_map_input.rename(columns={"PDB label": "Label"}, inplace=True)

fac_map = dict(zip(fac_map_input.Label, fac_map_input.Unit))
# print(fac_map)

# Now input data from publications (filter for just 2021 needed)
df = pd.read_excel(
    "data/infra_1921_comblab_mod.xlsx", sheet_name="Publications", engine="openpyxl"
)

# In this case, want just data from 2021
df = df[(df["Year"] == 2021)]

# convert labels to be the same as those used for reporting
df["Labels"] = (
    df["Labels"]
    .replace(to_replace="\(", value="", regex=True)
    .replace(to_replace="\)", value="", regex=True)
)
df = df.replace(fac_map, regex=True)
df = (
    df.replace(
        to_replace="Affinity Proteomics\|Affinity Proteomics",
        value="Affinity Proteomics",
        regex=True,
    )
    .replace(
        to_replace="NGI Short-read and Genotyping\|NGI Short-read and Genotyping\|NGI Short-read and Genotyping",
        value="NGI Short-read and Genotyping",
        regex=True,
    )
    .replace(
        to_replace="NGI Short-read and Genotyping\|NGI Short-read and Genotyping",
        value="NGI Short-read and Genotyping",
        regex=True,
    )
)


# You can do a check of this here
df.to_excel("test.xlsx")

# do not worry if there are labels that you would not use remaining, these will not be selected by the circos plot script
