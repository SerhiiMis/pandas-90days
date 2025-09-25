"""
Pandas is a Python library for data analysis and manipulation.
It's built on top of NumPy and is widely used for:
- Handling tabular data (like Excel or CSV)
- Cleaning and transforming messy data
- Performing aggregations and statistical summaries.

The Two Core Objects
1. SERIES -> A onedimensional labeled array (like a column in Excel)
2. DATAFRAME -> A two-dimensional labeled data structure (like an Excel sheet)
"""

import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Prague", "Berlin", "Vienna"]
}

df = pd.DataFrame(data)
print(df)

