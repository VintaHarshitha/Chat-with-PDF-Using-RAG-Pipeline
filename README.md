# Chat-with-PDF-Using-RAG-Pipeline

This script extracts tables from a PDF file, cleans up multi-line rows, and saves the cleaned data as a CSV file. It uses the tabula library for extracting the table data and pandas for handling and cleaning the data.

Requirements
Before running this script, make sure you have the following libraries installed:

tabula-py (Tabula's Python wrapper for PDF table extraction)
pandas (for data manipulation)
numpy (for handling missing data)

You can install these libraries using pip:
pip install tabula-py pandas numpy

Features
Extracts table data from a specified page of a PDF.
Cleans and merges multi-line rows where labels span across multiple lines.
Saves the cleaned data into a CSV file for further analysis.
Displays the cleaned data in the console for verification.
