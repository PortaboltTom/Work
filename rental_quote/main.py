import tkinter as tk
from tkinter import ttk
import pandas as pd
from jinja2 import Template
import subprocess

# Load data from the CSV files
contacts_path = 'data/contacts.csv'
accounts_path = 'data/accounts.csv'

# Load contacts and accounts data
contacts_data = pd.read_csv(contacts_path)
accounts_data = pd.read_csv(accounts_path)

# Merge contacts and accounts based on 'OwnerUserEmail' field
merged_data = pd.merge(contacts_data, accounts_data, on="OwnerUserEmail", how="left")

# Clean the merged data and keep relevant fields for the interface
merged_data_cleaned = merged_data[['Name_y', 'Name_x', 'City_y', 'CountryName_y', 'Postcode_y']]

# Group by the company name (from accounts.csv)
company_grouped_cleaned = merged_data_cleaned.groupby('Name_y')

# LaTeX template path
latex_template_path = 'latex_templates/quote_template.tex'

# Function to render the LaTeX template
def generate_quote(company_name, contact_name, system_name, price, date):
    with open(latex_template_path) as f:
        template = Template(f.read())
    
    # Render the template with the selected information
    rendered_latex = template.render(
        company_name=company_name,
        contact_name=contact_name,
        system_name=system_name,
        price=price,
        date=date
    )
    
    # Write the LaTeX to a file
    with open('quote.tex', 'w') as f:
        f.write(rendered_latex)

    # Compile the LaTeX file into PDF
    subprocess.run(['pdflatex', 'quote.tex'])

# GUI Application
class RentalAppUpdated:
    def __init__(self, root):
        self.root = root
        self.root.title("Rental Platform Quote Generator")

        # Dropdown for selecting a company
        self.company_label = tk.Label(root, text="Select a Company")
        self.company_label.pack()
        
        self.company_var = tk.StringVar()
        self.company_dropdown = ttk.Combobox(root, textvariable=self.company_var)
        self.company_dropdown['values'] = list(company_grouped_cleaned.groups.keys())
        self.company_dropdown.pack()
        self.company_dropdown.bind("<<ComboboxSelected>>", self.load_members)

        # Listbox for showing members of the selected company
        self.members_label = tk.Label(root, text="Select a Member")
        self.members_label.pack()

        self.members_listbox = tk.Listbox(root)
        self.members_listbox.pack()

        # Input fields for system, price, and date
        self.system_label = tk.Label(root, text="System")
        self.system_label.pack()
        self.system_entry = tk.Entry(root)
        self.system_entry.pack()

        self.price_label = tk.Label(root, text="Price (€)")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.date_label = tk.Label(root, text="Date")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        # Button to generate quote
        self.generate_button = tk.Button(root, text="Generate Quote", command=self.generate_quote)
        self.generate_button.pack()

    def load_members(self, event):
        selected_company = self.company_var.get()
        members = company_grouped_cleaned.get_group(selected_company)['Name_x'].tolist()

        # Clear the listbox and add new members
        self.members_listbox.delete(0, tk.END)
        for member in members:
            self.members_listbox.insert(tk.END, member)

    def generate_quote(self):
        selected_company = self.company_var.get()
        selected_member = self.members_listbox.get(tk.ACTIVE)
        system = self.system_entry.get()
        price = self.price_entry.get()
        date = self.date_entry.get()

        if selected_company and selected_member and system and price and date:
            generate_quote(selected_company, selected_member, system, price, date)
            print("Quote generated successfully!")
        else:
            print("Please fill out all fields before generating the quote.")

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = RentalAppUpdated(root)
    root.mainloop()
