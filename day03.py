# Single column → returns a Series
df['sepal_length']

# Multiple columns → returns a DataFrame
df[['sepal_length', 'species']]

df.iloc[0]        # first row
df.iloc[0:5]      # first 5 rows

df.loc[0]         # row with index 0
df.loc[0:4]       # rows 0 to 4 (inclusive)

# rows 0-4, only 'sepal_length' and 'species'
df.loc[0:4, ['sepal_length', 'species']]

# All rows where sepal_length > 5.0
df[df['sepal_length'] > 5.0]

# Multiple conditions (AND / OR)
df[(df['sepal_length'] > 5.0) & (df['species'] == 'setosa')]


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Select a single column
print(df['species'].head())

# Select multiple columns
print(df[['sepal_length', 'sepal_width']].head())

# Select rows by position
print(df.iloc[10:15])

# Select rows by condition
print(df[df['petal_length'] > 1.5].head())

# Select specific rows & columns
print(df.loc[0:4, ['sepal_length', 'species']])
