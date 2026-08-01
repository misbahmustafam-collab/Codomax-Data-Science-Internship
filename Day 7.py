import pandas as pd
#load dataset
df=pd.read_csv("FastFoodRestaurants.csv")
#check coulmns
print(df.columns)
#Data Analysis
print("Total latitude:", df["latitude"].sum())
print("Average latitude:",df["latitude"].mean())
print("Minimum latitude:", df["latitude"].min())
print("Maximum latitude:", df["latitude"].max())
print("count:",df["latitude"].count())