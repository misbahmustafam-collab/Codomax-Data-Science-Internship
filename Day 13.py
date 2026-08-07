import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Bar Chart
df['column_name'].value_counts().plot(kind='bar')
plt.title("Bar Chart")
plt.savefig("bar_chart.png")
plt.show()

# Pie Chart
df['column_name'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie Chart")
plt.savefig("pie_chart.png")
plt.show()

# Line Chart
df['numeric_column'].plot(kind='line')
plt.title("Line Chart")
plt.savefig("line_chart.png")
plt.show()