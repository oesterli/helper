import pandas as pd

## Input data
d =  {"somevalues": [1.0, 2.0, 3.0, 4.0, 4.0, 7.5, 3.2, 9.0, 10.0, 1.4], 
		"morevalues": [4.0, 3.0, 8.5,2.0, 1.0, 4.0, 3.0, 8.5,2.0, 1.0], 
		"litho": ["test-Sandstein Mergel","Mergel", "Granit", "Gneis", "sandstein32", "Granit", "Tonstein", "sandiger Sandstein", "Sandstein", "Gneis"],
		}

## Searchlist
searchList = ['Sandstein', 'Mergel', 'Granit', 'Gneis', 'Tonstein']

## Create DataFrame based on input data
df = pd.DataFrame(d)

###df.at[1, 'test'] = ['mytest', 'hello']

## Selecting rows based on selectString
## df.loc[row_indexer,column_indexer]=value
#df.loc[df['litho'].str.contains(searchString, case=False, regex=False), 'myLitho'] = searchList[0]

## Loop over searchList
for i in range(len(searchList)):
	df.loc[df['litho'].str.contains(searchList[i], case=False, regex=False), 'myLitho'] = searchList[i]
	


## Printing output
print(df)
