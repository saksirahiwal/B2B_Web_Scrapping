# scraper.py

import requests
from bs4 import BeautifulSoup
import time
import random
from utils import get_headers, handle_errors

def scrape_data(category, location):
    base_url = "https://www.yellowpages.com/search"
    headers = get_headers()
    data = []

    for page in range(1, 4):  # Scrape 2-3 pages
        params = {
            'search_terms': category,
            'geo_location_terms': location,
            'page': page
        }
        
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        listings = soup.find_all('div', class_='result')

        for listing in listings:
            try:
                company_info = {
                    'Company Name': listing.find('a', class_='business-name').text.strip() if listing.find('a', class_='business-name') else None,
                    'Website URL': listing.find('a', class_='track-visit-website')['href'] if listing.find('a', class_='track-visit-website') else None,
                    'Contact Number': listing.find('div', class_='phones phone primary').text.strip() if listing.find('div', class_='phones phone primary') else None,
                    'Location/Address': listing.find('div', class_='adr').text.strip() if listing.find('div', class_='adr') else None,
                    'Industry/Category': category,
                    'Company Description': listing.find('p', class_='body').text.strip() if listing.find('p', class_='body') else None,
                    'Email Address': None  # Generally unavailable
                }
                data.append(company_info)
            except Exception as e:
                handle_errors(e)

        # Delay to prevent blocking
        time.sleep(random.uniform(2, 4))

    return data
