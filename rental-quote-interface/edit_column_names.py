# edit_column_names_scroll.py
# Version 1.1: Interface to view, scroll, and edit column names side by side

import os
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import json
from utils import set_working_directory

# Set working directory to project root
set_working_directory()

# Load the dataset to extract column names
accounts_file = 'data/accounts.csv'
contacts_file = 'data/contacts.csv'
merged_data = pd.read_csv(accounts_file, sep=';').merge(pd.read_csv(contacts_file, sep=';'), left_on='Name', right_on='Website', how='left')

# File to store updated column names
column_names_file = 'data/column_names.json'

# Load existing column names if available
if os.path.exists(column_names_file):
    with open(column_names_file, 'r') as file:
        updated_column_names = json.load(file)
else:
    updated_column_names = merged_data.columns.tolist()

# Function to edit column names
def edit_column_names():
    root = tk.Tk()
    root.title("Edit Column Names")

    # Create a scrollable frame
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Display current and editable column names side by side
    current_names_label = ttk.Label(scrollable_frame, text="Current Column Names", font=("Helvetica", 12, "bold"))
    current_names_label.grid(row=0, column=0, padx=10, pady=10)
    new_names_label = ttk.Label(scrollable_frame, text="New Column Names", font=("Helvetica", 12, "bold"))
    new_names_label.grid(row=0, column=1, padx=10, pady=10)

    entry_widgets = []

    for idx, current_name in enumerate(merged_data.columns):
        # Current column name
        ttk.Label(scrollable_frame, text=current_name).grid(row=idx + 1, column=0, padx=10, pady=5, sticky="w")

        # Entry widget for new column name
        new_name_var = tk.StringVar(value=updated_column_names[idx])
        entry = ttk.Entry(scrollable_frame, textvariable=new_name_var, width=30)
        entry.grid(row=idx + 1, column=1, padx=10, pady=5, sticky="w")
        entry_widgets.append(new_name_var)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Save button to store updated column names
    def save_column_names():
        new_names = [entry.get() for entry in entry_widgets]
        with open(column_names_file, 'w') as file:
            json.dump(new_names, file)
        messagebox.showinfo("Success", "Column names updated successfully!")

    save_button = ttk.Button(root, text="Save Changes", command=save_column_names)
    save_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    edit_column_names()