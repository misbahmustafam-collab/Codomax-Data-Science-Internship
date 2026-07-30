import pandas as pd
#load dataset
df=pd.read_csv("FastFoodRestaurants.csv")
print("original data")
print(df.head())
#Missing values
print("Missing values")
print(df.isnull().sum)
#remove missing values
df=df.dropna()
#remove duplicates
print("duplicate record:")
print(df.duplicated().sum())
df=df.drop_duplicates()
#check data types
print("Data Types:")
print(df.dtypes)
#final dataset
print("clean dataset:")
print(df.info())
print(df.head())
