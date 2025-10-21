![FinancialReports Logo](https://cdn.financialreports.eu/financialreports/static/assets/logo.svg)
# The FinancialReports Code Cookbook

Welcome to the official FinancialReports code cookbook. This repository provides practical, production-ready solutions to accelerate your financial data analysis. Our goal is to help you go from raw data to actionable insights in minutes.

This "cookbook" provides clients and developers with scripts and notebooks to accelerate integration with:

1.  **The FinancialReports REST API**
2.  **FinancialReports Data Dumps**

## Getting Started

### 1. Set Your API Key (For API Examples)

All API-based scripts use the `FR_API_KEY` environment variable for security. **Never hardcode your API key.**

```bash
# On macOS / Linux
export FR_API_KEY="your_api_key_here"

# On Windows (Command Prompt)
# set FR_API_KEY="your_api_key_here"
```

### 2. Find Your Recipe

Browse the Recipe Index below to find a solution that matches your goal.

### 3. Run the Example

Every example is self-contained. Navigate to its directory, install its minimal dependencies, and run it.

```bash
# Example: Navigate to a recipe
cd use-cases/find_competitor_filings_api

# Install its specific dependencies
pip install -r requirements.txt

# Run the script or open the notebook
jupyter notebook find_competitor_filings.ipynb
```

## Recipe Index

Find your goal below and navigate to the corresponding recipe.

| Goal / Use Case | Recipe | Technology |
| :--- | :--- | :--- |
| **Data Dump Quickstart** | | |
| I have a data dump CSV. How do I make it queryable? | `data-dump-processing/load_metadata_csv_to_sqlite` | Python, Pandas, SQLite |
| **Workflows & Advanced Use Cases** | | |
| [API] Find all filings from a company's competitors. | `use-cases/find_competitor_filings_api` | Jupyter, SDK, Pandas |
| [Data Dump] Analyze readability for all 10-K filings. | `use-cases/analyze_dump_readability` | Jupyter, Pandas, SQLite |
| **Data Analysis & NLP** | | |
| Calculate the readability (Gunning Fog) of a filing. | `analysis/calculate_gunning_fog` | Jupyter, NLTK |
| Count keyword mentions (e.g., "ESG", "AI") in a filing. | `analysis/count_keywords` | Jupyter, Pandas |
| **Core API Examples** | | |
| Find a company by its ISIN or LEI. | `api-examples/companies/get_company_by_isin` | Python, SDK |
| Search for recent filings by date, type, or country. | `api-examples/filings/search_filings` | Python, SDK |
| Get the full list of all countries or filing types. | `api-examples/reference-data/` | Python, SDK |
| Download the raw Markdown content of a filing. | `api-examples/filings/get_filing_markdown` | Python, SDK |
| **Core Data Dump Examples** | | |
| Parse the `metadata.jsonl` file. | `data-dump-processing/parse_metadata_jsonl` | Python, Pandas |

## Repository Structure

While the Recipe Index is your main guide, here is a high-level overview of the repository's structure:

* `/api-examples`: Atomic, standalone Python scripts for common API endpoints (e.g., `get_company`, `search_filings`).
* `/data-dump-processing`: Production-ready Python scripts for handling bulk data dumps (e.g., loading a CSV into a database).
* `/analysis`: Standalone Jupyter Notebooks for common analytical tasks (e.g., NLP, metric calculations).
* `/use-cases`: Advanced Jupyter Notebooks that combine multiple tools to solve a complex, real-world problem (e.g., competitor analysis).

## Links & Support

* **Main Website**: https://financialreports.eu/
* **API Documentation**: https://docs.financialreports.eu/
* **Python SDK (PyPI)**: https://pypi.org/project/financial-reports-generated-client/
* **Support**: Contact `support@financialreports.eu` for questions.

## Contributing

We welcome contributions! Please see our `CONTRIBUTING.md` file for detailed guidelines on code standards, pull requests, and our "self-contained example" philosophy.