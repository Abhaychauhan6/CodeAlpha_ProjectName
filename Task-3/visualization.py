import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_data.csv")

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .astype(float)
)

plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=10)
plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig("price_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
df["Rating"].value_counts().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("rating_distribution.png")
plt.show()

print("Charts Generated Successfully!")