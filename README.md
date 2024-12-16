# Chat-with-PDF-Using-RAG-Pipeline

This project demonstrates how to extract tables from a PDF file, clean and merge multi-line rows, and use FAISS for retrieving relevant data from those tables based on a user query. The pipeline is built using the tabula, pdfplumber, sentence-transformers, and faiss libraries.
### Requirements

 - Before running this script, make sure you have the following libraries installed:
```sh
1. pip install tabula-py pandas numpy sentence-transformers faiss-cpu pdfplumber

```

```
### Overview

This script performs the following tasks:
```sh
Extract Tables from PDF: Using the tabula library, it extracts tables from a specified page of the PDF.
Clean and Merge Multi-Line Rows: Ensures that multi-line rows in the table are merged correctly.
Build FAISS Index: The tables are processed into text documents, and embeddings are generated using the SentenceTransformer model to build a FAISS index.
Retrieve Relevant Data: Using the FAISS index, the system retrieves rows relevant to a user query.
Return as Table: The relevant rows are returned as a DataFrame, where each row corresponds to the data relevant to the user query.
```
