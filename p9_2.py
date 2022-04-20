# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# Printing the first 10 rows of the data frame for visualization
df[:10]
print(df)

# this will replace "keyur sanghani" with "deep rupapara"
print(df.replace(to_replace ="keyur sanghani",
				value ="deep rupapara"))

