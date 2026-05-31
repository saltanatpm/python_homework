from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pandas as pd
import json
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver.get(url)

time.sleep(10)

books = driver.find_elements(
    By.CSS_SELECTOR,
    "li.YOUR_RESULT_CLASS"
)

results = []

for book in books:

    try:
        title = book.find_element(
            By.CSS_SELECTOR,
            "YOUR_TITLE_SELECTOR"
        ).text
    except:
        title = ""

    author_elements = book.find_elements(
        By.CSS_SELECTOR,
        "YOUR_AUTHOR_SELECTOR"
    )

    authors = [a.text for a in author_elements]

    author_text = "; ".join(authors)

    try:
        info_div = book.find_element(
            By.CSS_SELECTOR,
            "YOUR_FORMAT_DIV_SELECTOR"
        )

        format_year = info_div.find_element(
            By.TAG_NAME,
            "span"
        ).text

    except:
        format_year = ""

    results.append({
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    })

df = pd.DataFrame(results)

print(df)

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

driver.quit()