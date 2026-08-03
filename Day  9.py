import pandas as pd
import matplotlib.pyplot as plt

#load dataset
df=pd.read_csv("FastFoodRestaurants.csv")

plt.figure(figsize=(15,10))

#chart 1
plt.subplot(2,2,1)
top_cities=df["city"].value_counts().head(10)
plt.bar(top_cities.index,top_cities.values)
plt.title("top 10 cities")
plt.xticks(rotation=45)
plt.ylabel("Restaurant")

#chart 2
plt.subplot(2,2,3)
top_states=df["province"].value_counts().head(5)
plt.pie(
    top_states.values,
    labels=top_states.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("top 5 states")
plt.subplot(2,2,4)
country=df["country"].value_counts()

top_brands = df["brand"].value_counts().head(10)

plt.plot(country.index, country.values, marker='o')
plt.title("Restaurants by Country")
plt.xticks(rotation=45)
plt.ylabel("Count")

plt.tight_layout()
plt.show()
# Dashboard Analysis
# -----------------------------

print("========== DASHBOARD ANALYSIS ==========")
print()

print("1. City with highest restaurants :", top_cities.idxmax())
print("2. Most popular brand :", top_brands.idxmax())
print("3. State with highest restaurants :", top_states.idxmax())
print("4. Total countries :", df["country"].nunique())
print("5. Total restaurants :", len(df))