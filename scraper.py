import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Define financial news websites and their URLs
sources = {
    "Yahoo Finance": "https://finance.yahoo.com",
    "CNBC": "https://www.cnbc.com/finance/",
    "Bloomberg": "https://www.bloomberg.com/markets",
}

# Store scraped data
news_data = []

# Headers to mimic a real browser (some sites block bots)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Function to scrape Yahoo Finance
def scrape_yahoo():
    url = sources["Yahoo Finance"]
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("h3")[:10]  # Increase limit
    for article in articles:
        link = article.a["href"] if article.a else None
        headline = article.get_text(strip=True)
        if link:
            news_data.append(["Yahoo Finance", headline, f"https://finance.yahoo.com{link}"])

# Function to scrape CNBC
def scrape_cnbc():
    url = sources["CNBC"]
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("a", class_="Card-title")[:10]  # Increase limit
    for article in articles:
        link = article["href"]
        headline = article.get_text(strip=True)
        news_data.append(["CNBC", headline, link])

# Function to scrape Bloomberg
def scrape_bloomberg():
    url = sources["Bloomberg"]
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("a", class_="story-package-module__story__headline-link")[:10]  # Increase limit
    for article in articles:
        link = article["href"]
        headline = article.get_text(strip=True)
        news_data.append(["Bloomberg", headline, f"https://www.bloomberg.com{link}"])

# Run all scrapers
scrape_yahoo()
time.sleep(random.uniform(1, 3))  # Random delay
scrape_cnbc()
time.sleep(random.uniform(1, 3))
scrape_bloomberg()

# Save to CSV
df = pd.DataFrame(news_data, columns=["website", "headline", "link"])
df.to_csv("scraped_news.csv", index=False)
print("✅ Scraping complete! Data saved to scraped_news.csv")
