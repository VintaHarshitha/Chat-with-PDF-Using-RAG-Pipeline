import tabula
import pandas as pd
import numpy as np

# Function to clean and merge multi-line rows
def clean_and_merge_table(df):
    """
    Cleans and merges rows where a single label spans multiple lines.
    
    Parameters:
    - df: DataFrame, raw extracted table
    
    Returns:
    - DataFrame with cleaned and merged rows
    """
    # Replace NaN with empty strings for clean concatenation
    df = df.replace(np.nan, "", regex=True)

    # Initialize a new list for clean rows
    cleaned_data = []

    # Combine multi-line rows into single rows
    current_row = []
    for _, row in df.iterrows():
        if current_row and row[0] == "":  # Continuation of previous row
            current_row = [f"{a} {b}".strip() for a, b in zip(current_row, row)]
        else:
            if current_row:  # Append the completed row
                cleaned_data.append(current_row)
            current_row = list(row)
    cleaned_data.append(current_row)  # Add the last row

    # Convert cleaned data back into a DataFrame
    cleaned_df = pd.DataFrame(cleaned_data)

    # Assign proper column headers
    headers = cleaned_df.iloc[0]
    cleaned_df = cleaned_df[1:]
    cleaned_df.columns = headers

    return cleaned_df.reset_index(drop=True)

# Function to extract and clean table data
def extract_clean_table(pdf_path, page_number, output_csv):
    """
    Extracts table data from a PDF, cleans multi-line rows, and saves to CSV.
    
    Parameters:
    - pdf_path: str, path to the input PDF file
    - page_number: int, page number to extract data from
    - output_csv: str, file path to save the cleaned data
    """
    print("Extracting table data from PDF...")
    tables = tabula.read_pdf(pdf_path, pages=page_number, multiple_tables=True, pandas_options={"header": None})

    if tables:
        raw_df = pd.concat(tables, ignore_index=True)
        print("Raw table data extracted. Cleaning the data...")

        # Clean and merge multi-line rows
        cleaned_df = clean_and_merge_table(raw_df)

        # Save cleaned data to CSV
        cleaned_df.to_csv(output_csv, index=False)
        print(f"Cleaned data saved to '{output_csv}'")
        print("\nCleaned Data:")
        print(cleaned_df)
    else:
        print("No tables found on the specified page.")

# Path to the PDF file and output CSV
pdf_path = "C:/Users/Subhkar/sithafal/Tabless.pdf"  # Replace with your PDF file path
output_csv = "cleaned_gdp_data.csv"

# Extract, clean, and save table data from page 6
extract_clean_table(pdf_path, page_number=6, output_csv=output_csv)




