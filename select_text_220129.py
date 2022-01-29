import pandas as pd
import numpy as np

## Input data
d =  {"somevalues": [1.0, 2.0, 3.0, 4.0, 4.0, 7.5, 3.2, 9.0, 10.0, 1.4], 
		"morevalues": [4.0, 3.0, 8.5,2.0, 1.0, 4.0, 3.0, 8.5,2.0, 1.0], 
		"litho": ["test-Sandstein Mergel","Mergel", "Granit", "Gneis", "sandstein32", "Granit", "Tonstein", "sandiger Sandstein, Tonstein", "Sandstein", "Gneis"],
		}

## Searchlist
searchList = ['Sandstein', 'Mergel', 'Granit', 'Gneis', 'Tonstein']

## Create DataFrame based on input data
df = pd.DataFrame(d)

## Create new column with empty list
df['myLitho'] = [[] for _ in range(df.shape[0])]

## Selecting rows based on selectString
## df.loc[row_indexer,column_indexer]=value

## Loop over searchList
for i in range(len(searchList)):
	print('----', i)
	## write indices of selected rows into list
	idx = df.loc[df['litho'].str.contains(searchList[i], case=False, regex=False)].index.tolist()
	print('indices of ', searchList[i], ' : ', idx)
	
	## Loop over list of indices of selected rows
	for j in idx:
		df.loc[j, 'myLitho'].append(searchList[i])

## Printing output
print(df)

