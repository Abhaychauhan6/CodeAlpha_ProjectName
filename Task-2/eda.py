import pandas as pd

# Load Dataset
df = pd.read_csv("books_data.csv")

print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nMISSING VALUES")
print(df.isnull().sum())

# Price Cleaning
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .astype(float)
)

print("\nSTATISTICAL SUMMARY")
print(df["Price"].describe())

print("\nAVERAGE PRICE")
print(df["Price"].mean())

print("\nMAXIMUM PRICE")
print(df["Price"].max())

print("\nMINIMUM PRICE")
print(df["Price"].min())

print("\nRATING DISTRIBUTION")
print(df["Rating"].value_counts())