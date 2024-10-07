# quote_generator.py
# Version 2.6: Ensure 'quotes' folder is created in the root project directory

import os
from reportlab.pdfgen import canvas
from tkinter import simpledialog

def create_quote(selected_data):
    # Hardcode the project root to 'rental-quote-interface'
    project_root = r"C:\GIT\rental-quote-interface"

    # Create 'quotes' folder in the project root
    output_dir = os.path.join(project_root, "quotes")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ask for quote details
    system = simpledialog.askstring("Input", "Enter system name:")
    price = simpledialog.askstring("Input", "Enter price:")
    date = simpledialog.askstring("Input", "Enter date:")

    if not system or not price or not date:
        return

    # Generate PDF content for the quote
    company_name = selected_data[0]  # Assuming first column is company name
    pdf_filename = os.path.join(output_dir, f"quote_{company_name}.pdf")

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