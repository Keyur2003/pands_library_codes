# importing pandas as pd
import pandas as pd
import numpy as np
# Creating the first dataframe
df = pd.DataFrame({"A":[14, 4, 5, 7, 1],
				"B":["Sam", "olivia", "terica", "megan", "amanda"],
				"C":[20 + 5j, 20 + 3j, 7, 3, 8],
				"D":[14, 3, 6, 2, 6]})

# Print the dataframe
print(df)
print(df.notnull())
