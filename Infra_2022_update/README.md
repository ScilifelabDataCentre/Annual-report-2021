# Scripts for infrastructure report

## one_pagers

Folder contains the scripts required to produce the one pagers. You shuould run the **Data_prep.py** script first, then the **Make_plots.py** script. This will sort the data and create the required plots, respectively. The **Make_pdfs.py** script produces the pdfs (contains everything for layout and pulling the data and plots as needed). The **colour_science_2021.py** script sets the colours, it doesn't need to be run specifically.

**Academicuser_pie.py** - Produces a pie chart that summarises the unique academic users at infrastructure units in general.

**FTE_resources_user_cat.py** - Produces a pie chart that considers the allocation of resources (in terms of full time equivalents) per user categories.

**FTE_per_unit.py** - Produces a bar chart that considers full time equivalents per unit.

**Feeprofit_per_FTE.py** - Produces a bar chart that considers the profit (user fees minus reagents and consumables) per unit.

**Funding_stacked_bar.py** - Produces a stacked bar chart that considers the level of funding from different sources per unit.

**JIF_dataprep.py** - Prepares the data in the format required for the plot regarding journal impact factor.

**JIF_plot.py** - Uses the data from JIF_dataprep to produce a stacked bar chart to summarise the number of publication in different categories of journal impact factor score.

**Otherfunds_userfees.py** - Produces a pie chart that looks at sources of funding from 'other' sources.

**Resources_per_user_plot.py** - Produces a stacked bar chart that looks at the resources (in percent) for different user areas.

**circosplot.py** - script to produce the circos plot.

**colour_science_2022.py** - script defining visual identity 

**fac_map_circos.py** - essentially performs the data prep needed for the circos plot above.