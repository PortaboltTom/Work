import pandas as pd
from io import StringIO

def process_data(csv_content):
    # Read the CSV content into a list of lines
    lines = csv_content.strip().split('\n')
    
    # Check if there are at least three lines
    if len(lines) < 3:
        raise ValueError("CSV content does not have enough lines to set header to the third line.")
    
    # Reconstruct the CSV content from the third line onward
    csv_content_from_third_line = '\n'.join(lines[2:])
    
    # Read the CSV content from the third line as header
    df = pd.read_csv(StringIO(csv_content_from_third_line))
    
    # Print the headers
    print("Headers:", df.columns.tolist())
    
    # Convert timestamp to datetime and set as index
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df.set_index('timestamp', inplace=True)

    # Return the DataFrame for inspection
    return df

# Example usage
csv_content = """Your CSV content here"""
df = process_data(csv_content)
