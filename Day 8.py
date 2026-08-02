import pandas as pd
import matplotlib.pyplot as plt

#load dataset
df=pd.read_csv("FastFoodRestaurants.csv")
df.head()

top_cities=df['city'].value_counts().head(10)
plt.figure(figsize=(6,4))
plt.bar(top_cities.index,top_cities.values)
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.title('Top 10 Cities with Most Fast Food Restaurants')
plt.xticks(rotation=45)
plt.show()

#line charts
top_brands=df["name"].value_counts().head(10)
plt.figure(figsize=(6,4))
plt.plot(top_brands.index,top_brands.values,marker='o')
plt.xlabel('Brand')
plt.ylabel('Number of Restaurants')
plt.title('Top 10 Fast Food Brands')
plt.xticks(rotation=45)
plt.show()


#pie chart using matplotlib
top_brands=df["name"].value_counts().head(10)
plt.figure(figsize=(6,4))
plt.pie(top_brands.values,labels=top_brands.index,autopct='%1.1f%%')
plt.title('Top 10 Fast Food Brands')
plt.show()

