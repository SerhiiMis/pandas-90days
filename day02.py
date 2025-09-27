import pandas as pd


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

print(df.head())          # first 5 rows
print(df.info())          # structure        
print(df.describe())      # quick stats

print(df.shape)         # (rows, columns)
print(df.columns)       # column names  
print(df.dtypes)        # data types of columns

print("-------------------------")

# 1. First 10 rows
print("First 10 rows:")
print(df.head(10))

# 2. Number of rows and columns
print("\nShape (rows, columms):")
print(df.shape)

# 3. Column names
print("\nColumn names:")
print(df.columns.tolist())

# 4. Summary statistics
print("\nSummary statistics:")
print(df.describe())






