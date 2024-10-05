import os
import pandas as pd

# Set the working directory to the project root
def set_working_directory():
    project_root = r'C:\GIT\rental-quote-interface'
    os.chdir(project_root)
    print(f"Working directory set to: {os.getcwd()}")

def load_and_merge_data(accounts_file_path, contacts_file_path):
    # Load the CSV files
    accounts_df = pd.read_csv(accounts_file_path, sep=';')
    contacts_df = pd.read_csv(contacts_file_path, sep=';')

    # Rename 'Website' to 'CompanyName' in contacts_df for clarity
    contacts_df.rename(columns={'Website': 'CompanyName'}, inplace=True)

    # Merge contacts with their respective companies
    merged_df = pd.merge(contacts_df, accounts_df, left_on='CompanyName', right_on='Name', how='left')

    return merged_df

if __name__ == "__main__":
    # Set working directory to the project root
    set_working_directory()
    
    # Specify the correct paths relative to the project root
    accounts_file = 'data/accounts.csv'
    contacts_file = 'data/contacts.csv'
    
    # Load and merge the data
    merged_data = load_and_merge_data(accounts_file, contacts_file)
    print(merged_data.head())
