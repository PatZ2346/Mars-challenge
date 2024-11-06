# Import necessary libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json
import time

# Set up the ChromeDriverManager and Service
service = Service(ChromeDriverManager().install())

# Set up Splinter with the Service instance
browser = Browser('chrome', service=service, headless=False)

try:
    # Visit the Mars news site
    url = 'https://static.bc-edx.com/data/web/mars_news/index.html'
    browser.visit(url)

    # Optional: Delay for loading the page
    time.sleep(5)  # Wait for 5 seconds
    browser.is_element_present_by_css('div.content_title', wait_time=1)

    # Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Extract the titles and preview texts
    articles = news_soup.find_all('div', class_='list_text')

    # Initialize the list to store the scraped data
    news_data = []

    # Loop through the articles and extract titles and previews
    for article in articles:
        title = article.find('div', class_='content_title').get_text().strip()
        preview = article.find('div', class_='article_teaser_body').get_text().strip()
        news_data.append({'title': title, 'preview': preview})

    # Print the scraped data for verification
    print("Scraped Data:")
    for item in news_data:
        print(item)

    # Export the data to a JSON file with pretty-print
    with open('mars_news.json', 'w') as json_file:
        json.dump(news_data, json_file, indent=4)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    browser.quit()

