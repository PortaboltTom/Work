# main.py
# Version 1.6: Use absolute import path and add project root to sys.path

import os
import sys

# Hardcode the project root directory and add it to sys.path
project_root = r"C:\GIT\rental-quote-interface"
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from utils import set_working_directory
except ImportError as e:
    print(f"ImportError: {e}")
    print(f"sys.path: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")
    raise

# Set working directory to project root
set_working_directory()

from src.data_handler import load_and_merge_data

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
