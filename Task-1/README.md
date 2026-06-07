# CodeAlpha Data Analytics Internship - Task 1

## Web Scraping using Python

### Project Overview

This project was completed as part of the CodeAlpha Data Analytics Internship Program.

The objective of this project is to collect book information from a website using Python-based web scraping techniques. The extracted data is stored in a CSV file for further analysis and processing.

---

## Objective

To extract book details from a website and create a structured dataset using Python.

Website Used:

https://books.toscrape.com/

---

## Technologies Used

* Python
* Requests
* BeautifulSoup (bs4)
* Pandas

---

## Features

The scraper extracts the following information:

* Book Title
* Price
* Availability Status
* Rating

The extracted data is automatically stored in a CSV file.

---

## Project Structure

CodeAlpha_WebScraping/

├── scraper.py

├── books_data.csv

├── requirements.txt

├── README.md

└── screenshots/

```
└── output.png
```

---

## Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

Or

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the following command:

```bash
python scraper.py
```

---

## Sample Output

| Title                | Price  | Availability | Rating |
| -------------------- | ------ | ------------ | ------ |
| A Light in the Attic | £51.77 | In Stock     | Three  |
| Tipping the Velvet   | £53.74 | In Stock     | One    |
| Soumission           | £50.10 | In Stock     | One    |

---

## Methodology

1. Send an HTTP request to the target website.
2. Retrieve the HTML content.
3. Parse HTML using BeautifulSoup.
4. Extract required book information.
5. Store the extracted data in a Pandas DataFrame.
6. Export the dataset into a CSV file.

---

## Output

The scraper generates:

books_data.csv

containing all extracted book information.

---

## Learning Outcomes

Through this project, I learned:

* Basics of Web Scraping
* HTML Structure Analysis
* Data Extraction using BeautifulSoup
* Data Handling with Pandas
* CSV File Generation

---

## Conclusion

This project demonstrates how Python can be used to automatically collect and organize data from websites. Web scraping is an important technique in Data Analytics for building datasets and gathering information from online sources.

---

### Author

Abhay Chauhan

CodeAlpha Data Analytics Intern
