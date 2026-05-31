from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://owasp.org/www-project-top-ten/")

time.sleep(5)
links = driver.find_elements(
    By.XPATH,
    "//a[contains(@href,'A0')]"
)

results = []

for link in links:
    title = link.text.strip()
    href = link.get_attribute("href")
    if title:
        results.append({
            "Title": title,
            "Link": href
        })

df = pd.DataFrame(results)

df.to_csv(
    "owasp_top_10.csv",
    index=False
)

print(df)
print("CSV file created successfully.")

driver.quit()