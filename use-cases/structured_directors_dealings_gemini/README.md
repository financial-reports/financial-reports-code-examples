# Extract Structured Insider Trades (Directors' Dealings) with AI

This use-case notebook demonstrates how to solve a common problem for financial analysts: converting unstructured insider trade filings (also known as Directors' Dealings or DIRS) into clean, structured, and analyzable data.

We will use the FinancialReports API to find the filings and Google's Gemini Flash (`gemini-flash-latest`) AI model to perform the data extraction.

## Goal

The goal of this script is to take a company ISIN as an input, find all its recent insider trade filings, and convert the raw text of those filings into a structured JSON object. We will then flatten this data into a `pandas` DataFrame, ready for analysis or export to a CSV file.

This workflow is ideal for clients who need structured data from DIRS filings but do not have the technical resources to build and maintain complex, rule-based parsers for different filing formats.

## What This Notebook Demonstrates

This notebook provides a complete, end-to-end workflow:

1.  **Find Filings**: How to use the FinancialReports API to find all filings of type `DIRS` for a specific company ISIN.
2.  **Fetch Content**: How to retrieve the full, clean markdown content for each of those filings.
3.  **Define Schema**: How to define a rigid JSON schema that tells the AI *exactly* what data to extract (e.g., person, position, transaction type, price, currency, volume).
4.  **Extract with AI**: How to use Google's Gemini Flash model in "JSON Mode" to parse the markdown and return data that perfectly matches our schema.
5.  **Aggregate & Flatten**: How to loop through all filings, aggregate the structured data, and use `pandas.json_normalize` to convert the nested JSON into a simple, flat table for analysis.

## Setup & Configuration

### 1. Install Dependencies

Before running the notebook, you must install the required Python libraries.

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

This notebook requires API keys for both FinancialReports and the Google Gemini service. For security and best practices, these should be set as environment variables, not hardcoded in the notebook.

You can set them in your terminal:

```bash
# On macOS / Linux
export FR_API_KEY="your_financial_reports_api_key_here"
export GEMINI_API_KEY="your_google_ai_studio_api_key_here"

# On Windows (Command Prompt)
# set FR_API_KEY="your_financial_reports_api_key_here"
# set GEMINI_API_KEY="your_google_ai_studio_api_key_here"
```

Alternatively, you can create a file named `.env` in this directory and the script will load them from there:

**`.env` file:**

```
FR_API_KEY="your_financial_reports_api_key_here"
GEMINI_API_KEY="your_google_ai_studio_api_key_here"
```