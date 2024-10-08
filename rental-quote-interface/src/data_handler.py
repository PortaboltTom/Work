# data_handler.py
# Version 1.2: Update column names based on the saved configuration file

import os
import pandas as pd
import json
from utils import set_working_directory

# Set working directory to project root
set_working_directory()

# File to store updated column names
column_names_file = 'data/column_names.json'

def load_and_merge_data(accounts_file_path, contacts_file_path):
    # Load the CSV files
    accounts_df = pd.read_csv(accounts_file_path, sep=';')
    contacts_df = pd.read_csv(contacts_file_path, sep=';')

    # Merge contacts with their respective companies
    merged_df = pd.merge(contacts_df, accounts_df, left_on='Website', right_on='Name', how='left')

    # Load updated column names if available
    if os.path.exists(column_names_file):
        with open(column_names_file, 'r') as file:
            updated_column_names = json.load(file)
        merged_df.columns = updated_column_names

    return merged_df

if __name__ == "__main__":
    # Specify the correct paths relative to the project root
    accounts_file = 'data/accounts.csv'
    contacts_file = 'data/contacts.csv'
    
    # Load and merge the data
    merged_data = load_and_merge_data(accounts_file, contacts_file)
    print(merged_data.head())
