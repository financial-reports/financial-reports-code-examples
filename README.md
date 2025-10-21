![FinancialReports Logo](https://cdn.financialreports.eu/financialreports/static/assets/logo.svg)
# FinancialReports Code Examples (Cookbook)

Welcome to the official FinancialReports code examples repository. This "cookbook" provides clients and developers with practical, production-ready scripts to accelerate integration with:

1.  The FinancialReports REST API
2.  FinancialReports data dumps

## Repository Structure

This repository is organized into self-contained examples. The main categories are:

* **`/api-examples`**: Recipes for interacting with the FinancialReports REST API.
    * `/api-examples/filings`: (e.g., `search_filings`, `get_filing_markdown`)
    * `/api-examples/companies`: (e.g., `get_company_by_isin`)
    * `/api-examples/reference-data`: (e.g., `list_countries`, `browse_isic_hierarchy`)
* **`/data-dump-processing`**: Scripts for parsing and managing bulk data dumps.
    * `/data-dump-processing/parse_metadata_jsonl`: (e.g., `parse_metadata.py`)
* **`/general-helper-scripts`**: Standalone tools for common financial analysis tasks.
    * `/general-helper-scripts/count_keywords`: (e.g., `count_keywords.py`)
    * `/general-helper-scripts/calculate_gunning_fog`: (e.g., `calculate_gunning_fog.py`)
* **`/common`**: (Reserved for) Shared Python modules that can be imported by other examples.

## Getting Started

### 1. Find Your Example

Navigate into the example folder that matches your goal. For instance:

`cd api-examples/filings/search_filings`

### 2. Install Dependencies

Each example is isolated and has its own `requirements.txt`:

`pip install -r requirements.txt`

### 3. Set Your API Key (If Required)

API-based scripts use an environment variable for security. **Never hardcode your API key.**

```bash
# On macOS / Linux
export FR_API_KEY="your_api_key_here"

# On Windows (Command Prompt)
# set FR_API_KEY="your_api_key_here"
```

### 4. Run the Script

```
python example_script_name.py
```

## Links

* **Main Website**: https://financialreports.eu/
* **API Documentation**: https://docs.financialreports.eu/
* **Python SDK (PyPI)**: https://pypi.org/project/financial-reports-generated-client/