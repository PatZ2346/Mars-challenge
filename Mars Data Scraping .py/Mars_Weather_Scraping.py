# Import necessary libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Set up the ChromeDriverManager and Service
service = Service(ChromeDriverManager().install())

# Set up Splinter with the Service instance
browser = Browser('chrome', service=service, headless=False)

try:
    # Visit the Mars Temperature Data site
    url = 'https://static.bc-edx.com/data/web/mars_facts/temperature.html'
    browser.visit(url)

    # Optional: Delay for loading the page
    time.sleep(5)  # Wait for 5 seconds
    browser.is_element_present_by_css('table', wait_time=1)

    # Convert the browser html to a soup object
    html = browser.html
    weather_soup = soup(html, 'html.parser')

    # Scrape the data from the HTML table
    table = weather_soup.find('table')
    rows = table.find_all('tr')

    # Initialize the list to store the scraped data
    weather_data = []

    # Loop through the rows and extract the data
    for row in rows[1:]:
        cols = row.find_all('td')
        weather_data.append({
            'id': int(cols[0].get_text()),
            'terrestrial_date': cols[1].get_text(),
            'sol': int(cols[2].get_text()),
            'ls': float(cols[3].get_text()),
            'month': int(cols[4].get_text()),
            'min_temp': float(cols[5].get_text()),
            'pressure': float(cols[6].get_text())
        })

    # Convert the list to a DataFrame
    weather_df = pd.DataFrame(weather_data)

    # Print the DataFrame for verification
    print(weather_df.head())

    # Export the DataFrame to a CSV file
    weather_df.to_csv('mars_weather.csv', index=False)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    browser.quit()
