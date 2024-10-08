# quote_generator.py
# Version 2.6: Ensure 'quotes' folder is created in the root project directory
# Version 3.0: Use centralized configuration and utility functions for working directory and folder creation
# Version 3.1: Use centralized configuration and utility functions for working directory and folder creation, with dynamic project root detection

import os

project_root = r"C:\GIT\rental-quote-interface"
os.chdir(project_root)

from reportlab.pdfgen import canvas
from tkinter import simpledialog
from config import QUOTES_DIR
from utils import set_working_directory



def create_quote(selected_data):
    # Set working directory using utility function
    set_working_directory()

    # Create 'quotes' folder in the project root
    if not os.path.exists(QUOTES_DIR):
        os.makedirs(QUOTES_DIR)

    # Ask for quote details
    system = simpledialog.askstring("Input", "Enter system name:")
    price = simpledialog.askstring("Input", "Enter price:")
    date = simpledialog.askstring("Input", "Enter date:")

    if not system or not price or not date:
        return

    # Generate PDF content for the quote
    company_name = selected_data[0]  # Assuming first column is company name
    pdf_filename = os.path.join(QUOTES_DIR, f"quote_{company_name}.pdf")

    # Create PDF using ReportLab
    c = canvas.Canvas(pdf_filename)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 750, f"Quote for {company_name}")

    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Date: {date}")
    c.drawString(100, 670, "Current Situation:")
    c.drawString(100, 650, "[Description of the current situation]")

    c.drawString(100, 620, "Solution:")
    c.drawString(100, 600, f"We propose the following system: {system}")

    c.drawString(100, 570, "Offer:")
    c.drawString(100, 550, f"The total price for the system is: {price}")

    # Save the PDF
    c.save()

    print(f"Quote saved as {pdf_filename}")
