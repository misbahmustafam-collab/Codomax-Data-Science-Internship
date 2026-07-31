import pandas as pd

# load dataset
df = pd.read_csv("FastFoodRestaurants.csv")

# Display first 5 rows
print("original dataset:")
print(df.head())

# display column names
print("\ncolumns:")
print(df.columns)

# 1. filter rows
# Example: filter restaurants from California (CA)
filtered_df = df[df["province"] == "CA"]
print("\nFiltered restaurants from California:")
print(filtered_df.head())

#2. select columns
selected_df = df[['name', 'city', 'province']]
print("\nSelected columns:")
print(selected_df.head())

#3.sort Dataset
sorted_df = df.sort_values(by='name')
print("\nSorted dataset by Restaurant Name:")
print(sorted_df.head())

#save filtered dataset
sorted_df.to_csv("filtered_FastFoodRestaurants.csv,index=false")
print("\nfiltered dataset saved successfully")