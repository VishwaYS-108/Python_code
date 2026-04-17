import pandas as pd
df = pd.read_excel('TestFile.xlsx', index_col=0)
#print(df.index[0])
#print(df.columns[1])
print(df.loc[1].Name)
print(df.loc[1].Password)