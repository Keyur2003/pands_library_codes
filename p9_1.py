# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series(['New York', 'Chicago', 'Toronto', None, 'Rio'])

# Create the Index
sr.index = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# set the index
# sr.index = index_

# Print the series
print(sr)
# fill the values using dictionary
result = sr.fillna(value = {'City 4' : 'Lisbon', 'City 1' : 'Dublin'})

# Print the result
print(result)
