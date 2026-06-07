import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating = book.p["class"][1]

        data.append([
            title,
            price,
            availability,
            rating
        ])

    df = pd.DataFrame(
        data,
        columns=[
            "Title",
            "Price",
            "Availability",
            "Rating"
        ]
    )

    df.to_csv("books_data.csv", index=False)

    print(df.head())

else:
    print("Failed to fetch website")