import pandas as pd

# ==============================
# Day 10 - Export Data Task
# ==============================

# Step 1: Load Dataset
df = pd.read_csv("RealEstate-USA.csv")

# Step 2: Display Original Dataset Information
print("Original Dataset Shape:", df.shape)
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 3: Data Cleaning
# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Step 4: Display Cleaned Dataset Information
print("\nCleaned Dataset Shape:", df.shape)
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 5: Export Cleaned Dataset
output_file = "Cleaned_RealEstate-USA.csv"
df.to_csv(output_file, index=False)

# Step 6: Success Message
print(f"\n✅ Cleaned dataset has been successfully exported as '{output_file}'")