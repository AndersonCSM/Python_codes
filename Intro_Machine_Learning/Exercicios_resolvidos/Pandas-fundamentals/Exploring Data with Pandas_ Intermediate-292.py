## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500.loc[: , [ 'rank', 'revenues', 'revenue_change'] ].head(5)

## 2. Reading CSV files with pandas ##

f500 = pd.read_csv("f500.csv")

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]

company_value = f500["company"].iloc[0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500.iloc[0:3]

first_seventh_row_slice = f500.iloc[[0, 6], 0:5]

## 5. Using pandas methods to create boolean masks ##

res =f500["previous_rank"].isnull()

null_previous_rank = f500[res][["company","rank", "previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]

top5_null_prev_rank = null_previous_rank.iloc[0:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]

f500["rank_change"] = rank_change

## 8. Using Boolean Operators ##

large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits

big_rev_neg_profit = f500.loc[combined]

## 9. Using Boolean Operators Continued ##

mask_b = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")

brazil_venezuela = f500.loc[mask_b]

tech_outside_usa = f500[(f500["sector"] == "Technology") & (f500["country"] != "USA")] .head(5)

## 10. Sorting Values ##

rows = f500["country"] == "Japan"
Japan = f500[f500["country"] == "Japan"].sort_values("employees", ascending=False)
# Japan["company"].iloc[0]

top_japanese_employer = Japan["company"].iloc[0]

## 11. Using Loops with pandas ##

top_employer_by_country = {}

countries = f500["country"].unique()

for i in countries:
    
    row = f500[f500["country"] == i]
    company = row.sort_values("employees", ascending=False)
               
               
    top_employer_by_country[i] = company["company"].iloc[0]
    

## 12. Challenge: Calculating Return on Assets by Sector ##

roa = f500["profits"] / f500["assets"]


f500["roa"] = roa

top_roa_by_sector = {}

for i in f500["sector"].unique():
    
    roa_sector = f500[f500["sector"] == i].sort_values("roa", ascending=False)
    
    top_roa_by_sector[i] = roa_sector["company"].iloc[0]