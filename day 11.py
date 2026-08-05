import pandas as pd

# Load Dataset
df = pd.read_csv("StudentsPerformance.csv")

print("="*50)
print("Students Performance Dataset Analysis")
print("="*50)

# 1. Average Scores
print("\n1. Average Scores")
print(df[['math score', 'reading score', 'writing score']].mean())

# 2. Average Scores by Gender
print("\n2. Average Scores by Gender")
print(df.groupby('gender')[['math score', 'reading score', 'writing score']].mean())

# 3. Average Scores by Lunch Type
print("\n3. Average Scores by Lunch Type")
print(df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean())

# 4. Average Scores by Test Preparation Course
print("\n4. Average Scores by Test Preparation")
print(df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean())

# 5. Average Scores by Parent Education
print("\n5. Average Scores by Parental Education")
print(df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean())

# Correlation
print("\n6. Correlation Matrix")
print(df[['math score', 'reading score', 'writing score']].corr())

print("\nAnalysis Completed Successfully!")