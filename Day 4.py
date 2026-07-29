import pandas as pd
df=pd.read_csv("FastFoodRestaurants.csv")
print(df)

# First rows
print("First 5 rows:")
print(df.head())

# Last rows
print("Last 5 rows:")
print(df.tail())

# Last rows
print("Last 5 rows:")
print(df.tail())

# Columns
print("Columns:")
print(df.columns)

# Information
print("Dataset Information:")
print(df.info())

# Shape
print("Dataset Shape:")
print(df.shape)

# Statistics
print("Description:")
print(df.describe())
