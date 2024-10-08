# create_interface.py
# Version 2.0: Set working directory to project root before loading data
# Version 2.1: Updated to use centralized configuration and utility functions for dynamic project root detection

import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from src.data_handler import load_and_merge_data
from utils import set_working_directory

set_working_directory()

# Function to create the interface window
def create_interface():
    # Set the working directory to the project root
    set_working_directory()

    # Load the merged data
    accounts_file = 'data/accounts.csv'
    contacts_file = 'data/contacts.csv'
    merged_data = load_and_merge_data(accounts_file, contacts_file)

    # Create the main window
    root = tk.Tk()
    root.title("Merged Data Viewer")

    # Dropdown menu for selecting columns to display
    dropdown_frame = ttk.Frame(root, padding="10")
    dropdown_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    selected_columns = tk.StringVar(value=[])

    # Create listbox with checkboxes for column selection
    column_listbox = tk.Listbox(dropdown_frame, listvariable=selected_columns, selectmode='multiple', height=6)
    column_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Insert columns into the listbox
    for col in merged_data.columns:
        column_listbox.insert(tk.END, col)

    # Create frame for the data table
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Add scrollbars
    x_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    y_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)

    # Create a treeview to display the data
    tree = ttk.Treeview(frame, columns=[], show='headings', xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
    
    # Place the table and configure scrollbars
    tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    x_scrollbar.config(command=tree.xview)
    y_scrollbar.config(command=tree.yview)
    x_scrollbar.grid(row=1, column=0, sticky=tk.EW)
    y_scrollbar.grid(row=0, column=1, sticky=tk.NS)

    # Button to update the table based on selected columns
    def update_table():
        selected_cols = [column_listbox.get(i) for i in column_listbox.curselection()]
        if not selected_cols:
            return
        # Clear and update the table with new columns
        tree.delete(*tree.get_children())
        tree["columns"] = selected_cols
        for col in selected_cols:
            tree.heading(col, text=col)
        for _, row in merged_data[selected_cols].iterrows():
            tree.insert("", "end", values=list(row))

    update_button = ttk.Button(dropdown_frame, text="Update Table", command=update_table)
    update_button.grid(row=1, column=0, sticky=(tk.W, tk.E))

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_interface()
