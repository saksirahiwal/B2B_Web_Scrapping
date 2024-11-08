# main.py

from scraper import scrape_data
from utils import save_to_csv
from dataprocessing import clean_data, save_cleaned_data
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

def main():
    # Specify the category and location
    category = "IT Services"
    location = "New York, NY"
    
    # Scrape data
    scraped_data = scrape_data(category, location)
    
    # Save data to CSV
    if scraped_data:
        save_to_csv(scraped_data, 'b2b_directory_data.csv')
        print("Data scraping complete. Saved to b2b_directory_data.csv")
    else:
        print("No data scraped.")

    # load the data into frame
    df = pd.read_csv('b2b_directory_data.csv')
    cleaned_data=clean_data(df)
    # Save cleaned data to CSV
    save_cleaned_data(cleaned_data)

    print("Data Processing complete")

if __name__ == "__main__":
    main()
