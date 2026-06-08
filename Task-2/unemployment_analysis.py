import pandas as pd

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Average Unemployment Rate
avg_rate = df['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate:")
print(round(avg_rate, 2))

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))

sns.histplot(
    df['Estimated Unemployment Rate (%)'],
    bins=20,
    kde=True
)

plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")

plt.savefig("unemployment_distribution.png")

print("GRAPH 1 SAVED")

# ===== GRAPH 2 =====

region_data = df.groupby('Region')[
    'Estimated Unemployment Rate (%)'
].mean().sort_values(ascending=False)

plt.figure(figsize=(15,8))

region_data.plot(kind='bar')

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()

plt.savefig("region_analysis.png")

print("GRAPH 2 SAVED")

# ===== GRAPH 3 =====

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

monthly_data = df.groupby('Date')[
    'Estimated Unemployment Rate (%)'
].mean()

plt.figure(figsize=(14,6))

monthly_data.plot()

plt.title("Monthly Unemployment Trend")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()

plt.savefig("monthly_trend.png")

print("GRAPH 3 SAVED")

# ===== GRAPH 4 =====

covid_data = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(14,6))

covid_monthly = covid_data.groupby('Date')[
    'Estimated Unemployment Rate (%)'
].mean()

covid_monthly.plot()

plt.title("Covid-19 Impact on Unemployment")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()

plt.savefig("covid_analysis.png")

print("GRAPH 4 SAVED")

# ===== GRAPH 5 =====

numeric_df = df[[
    'Estimated Unemployment Rate (%)',
    'Estimated Employed',
    'Estimated Labour Participation Rate (%)'
]]

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("heatmap.png")

print("GRAPH 5 SAVED")