
import os
from src.data_handler import load_and_merge_data, set_working_directory

# Set working directory to project root
set_working_directory()

def main():
    # Specify the paths to your data files
    accounts_file = 'data/accounts.csv'
    contacts_file = 'data/contacts.csv'
    
    # Load and merge the data using the data_handler script
    merged_data = load_and_merge_data(accounts_file, contacts_file)
    
    # Display the merged data
    print("Merged Data:")
    print(merged_data.head())

if __name__ == "__main__":
    main()
