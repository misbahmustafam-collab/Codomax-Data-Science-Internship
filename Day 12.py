# ============================================
# Day 12 - Project Improvement
# Data Science Internship
# Name: Misbah Mustafa
# ============================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset.csv")

# Display first five rows
print("First Five Rows")
print(df.head())

# Dataset Information
print("\nDataset Information")
print(df.info())

# Check Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Remove Duplicate Values
df = df.drop_duplicates()

# Fill Missing Values
df = df.fillna(method="ffill")

# Summary Statistics
print("\nSummary Statistics")
print(df.describe())

# ============================================
# Bar Chart
# Replace 'column_name' with your categorical column
# ============================================
df['column_name'].value_counts().plot(kind='bar')
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# ============================================
# Line Chart
# Replace 'numeric_column' with your numeric column
# ============================================
df['numeric_column'].plot(kind='line')
plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# ============================================
# Pie Chart
# Replace 'column_name' with your categorical column
# ============================================
df['column_name'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie Chart")
plt.ylabel("")
plt.show()

print("\nProject Improved Successfully!")