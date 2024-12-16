# Chat-with-PDF-Using-RAG-Pipeline

This script extracts tables from a PDF file, cleans up multi-line rows, and saves the cleaned data as a CSV file. It uses the tabula library for extracting the table data and pandas for handling and cleaning the data.

###Requirements
Before running this script, make sure you have the following libraries installed:
```sh
1. tabula-py (Tabula's Python wrapper for PDF table extraction)
2. pandas (for data manipulation)
3. numpy (for handling missing data)
```

You can install these libraries using pip:
```sh
pip install tabula-py pandas numpy
```
###Features
```sh
1.Extracts table data from a specified page of a PDF.
2.Cleans and merges multi-line rows where labels span across multiple lines.
3.Saves the cleaned data into a CSV file for further analysis.
4.Displays the cleaned data in the console for verification.
```
