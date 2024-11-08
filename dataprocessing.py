# data_processing.py

import pandas as pd

def clean_data(df):
    """Cleans the data by handling missing values and duplicates."""

    # Drop email column because email address is empty column
    df.drop(columns=['Email Address'], inplace=True, errors='ignore')

    #Drop rows with missing 'Contact Number' (assuming it's essential)
    df.dropna(subset=['Contact Number'], inplace=True)

     # Fill missing values in 'Website URL' and 'Location/Address' with placeholders
    df['Website URL'].fillna('Not Available', inplace=True)
    df['Location/Address'].fillna('Not Provided', inplace=True)

    #fill missing values in 'Company Description' with a placeholder
    df['Company Description'].fillna('Description Not Available', inplace=True)

    

    return df

def save_cleaned_data(df, filename='cleaned_companies_data.csv'):
    """Saves cleaned data to a CSV file."""
    df.to_csv(filename, index=False)
